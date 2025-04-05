use axum::{Json, extract::State};
use sqlx::PgPool;
use crate::models::site::Site;

pub async fn list_sites(
    State(pool): State<PgPool>,
) -> Result<Json<Vec<Site>>, (axum::http::StatusCode, String)> {
    let rows = sqlx::query_as::<_, Site>("SELECT * FROM sites ORDER BY created_at DESC")
        .fetch_all(&pool)
        .await
        .map_err(|e| (axum::http::StatusCode::INTERNAL_SERVER_ERROR, e.to_string()))?;

    Ok(Json(rows))
}

pub async fn create_site(
    State(pool): State<PgPool>,
    Json(payload): Json<CreateSite>,
) -> Resut<Json<Site>, (axum::http::StatusCode, String)> {
    let row = sqlx::query_as::<_, Site>(
        "INSERT INTO sites (url) VALUES ($1) RETURNING *"
    )
    .bind(payload.url)
    .fetch_one(&pool)
    .await.map_err(|e| (axum::http::StatusCode::INTERNAL_SERVER_ERROR, e.to_string()))?;

    OK(Json(row))
}
use crate::models::site::SiteCheck;

pub async fn list_checks(
    State(pool): State<PgPool>,
) -> Result<Json<Vec<SiteCheck>>, (axum::http::StatusCode, String)> {
    let checks = sqlx::query_as::<_, SiteCheck>(
        "SELECT * FROM site_checks ORDER BY checked_at DESC LIMIT 50"
    )
    .fetch_all(&pool)
    .await
    .map_err(|e| (axum::http::StatusCode::INTERNAL_SERVER_ERROR, e.to_string()))?;

    Ok(Json(checks))
}
use axum::{response::{IntoResponse, Response}, http::header, body::Body};
use xlsxwriter::*;
use std::io::Cursor;

pub async fn export_checks_excel(
    State(pool): State<PgPool>,
) -> Result<Response, (axum::http::StatusCode, String)> {
    let checks = sqlx::query!(
        r#"
        SELECT site_url, status_code, success, response_time_ms, checked_at
        FROM site_checks
        ORDER BY checked_at DESC
        LIMIT 100
        "#
    )
    
    .fetch_all(&pool)
    .await
    .map_err(|e| (axum::http::StatusCode::INTERNAL_SERVER_ERROR, e.to_string()))?;

    let mut buffer = Cursor::new(Vec::new());
    {
        let workbook = Workbook::new(&mut buffer);
        let mut sheet = workbook.add_worksheet(None)?;

        // Cabeçalho
        let headers = ["URL", "Status Code", "Success", "Response Time (ms)", "Checked At"];
        for (col, title) in headers.iter().enumerate() {
            sheet.write_string(0, col as u16, title, None)?;
        }

        // Dados
        for (row, check) in checks.iter().enumerate() {
            sheet.write_string((row + 1) as u32, 0, &check.site_url, None)?;
            sheet.write_number((row + 1) as u32, 1, check.status_code.unwrap_or(0) as f64, None)?;
            sheet.write_boolean((row + 1) as u32, 2, check.success, None)?;
            sheet.write_number(
                (row + 1) as u32,
                3,
                check.response_time_ms.unwrap_or(0) as f64,
                None,
            )?;
            sheet.write_string(
                (row + 1) as u32,
                4,
                &check.checked_at.to_rfc3339(),
                None,
            )?;
        }

        workbook.close()?;
    }

    let bytes = buffer.into_inner();

    Ok((
        axum::http::StatusCode::OK,
        [
            (header::CONTENT_TYPE, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
            (header::CONTENT_DISPOSITION, "attachment; filename=\"healthchecks.xlsx\""),
        ],
        Body::from(bytes),
    ).into_response())
}
