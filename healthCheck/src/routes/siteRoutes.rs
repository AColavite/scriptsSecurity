use axum::{
    Router,
    routing::{get, post},
};
use sqlx::PgPool;

use crate::handlers::site_handler::{
    list_sites,
    create_site,
    list_checks,
    export_checks_excel,
};

pub fn site_routes(pool: PgPool) -> Router {
    Router::new()
        .route("/", get(list_sites).post(create_site))
        .route("/checks", get(list_checks))
        .route("/checks/export", get(export_checks_excel))
        .with_state(pool)
}
