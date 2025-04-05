use serde::{Serialize, Deserialize};
use uuid::Uuid;
use chrono::{DateTime, Utc};

#[derive(Debug, Serialize, Deserialize, sqlx::FromRow)]
pub struct Site {
    pub id: Uuid,
    pub url: String,
    pub created_at: DateTime<Utc>,
}

pub struct CreateSite {
    pub url: String,
}

use chrono::Utc;

#[derive(Debug, sqlx::FromRow, Serialize)]
pub struct SiteCheck {
    pub id: uuid::Uuid,
    pub site_url: String,
    pub status_code: Option<i32>,
    pub success: bool,
    pub response_time_ms: Option<i32>,
    pub checked_at: chrono::DateTime<Utc>,
}