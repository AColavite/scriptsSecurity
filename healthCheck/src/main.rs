use axum::Router;
use std::net::SocketAddr;
use dotenv::dotenv;
use sqlx::postgres::PgPoolOptions;

mod config;
mod db;
mod handlers;
mod models;
mod routes;
mod scheduler;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    dotenv().ok();

    let db_url = std::env::var("DATABASE_URL")?;
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect(&db_url)
        .await?;

    scheduler::start(pool.clone()).await;

    let app = Router::new().nest("/sites", routes::site_routes::site_routes(pool));

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Server running at http://{}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await?;

    Ok(())
}
