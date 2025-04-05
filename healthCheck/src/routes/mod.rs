pub mod site_routes;

use axum::Router;
use sqlx::PgPool;
use self::site_routes::site_routes;

pub fn init_routes(pool: PgPool) -> Router {
    Router::new().nest("/sites", site_routes(pool))
}
