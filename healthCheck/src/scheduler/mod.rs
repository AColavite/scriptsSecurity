use chrono::Utc;

pub async fn start(pool: PgPool) {
    let client = Client::new();

    tokio::spawn(async move {
        loop {
            match sqlx::query!("SELECT url FROM sites")
                .fetch_all(&pool)
                .await
            {
                Ok(sites) => {
                    for site in sites {
                        let url = site.url.clone();
                        let start_time = std::time::Instant::now();

                        let result = client.get(&url).send().await;

                        let (success, status_code, response_time_ms) = match result {
                            Ok(resp) => {
                                let code = resp.status().as_u16() as i32;
                                let ms = start_time.elapsed().as_millis() as i32;
                                println!("✅ {} [{}]", url, code);
                                (true, Some(code), Some(ms))
                            }
                            Err(_) => {
                                println!("❌ {} [FAILED]", url);
                                (false, None, None)
                            }
                        };

                
                        let _ = sqlx::query!(
                            "INSERT INTO site_checks (site_url, status_code, success, response_time_ms, checked_at)
                             VALUES ($1, $2, $3, $4, $5)",
                            url,
                            status_code,
                            success,
                            response_time_ms,
                            Utc::now()
                        )
                        .execute(&pool)
                        .await;
                    }
                }
                Err(e) => {
                    println!("Erro ao buscar sites: {}", e);
                }
            }

            sleep(Duration::from_secs(300)).await;
        }
    });
}
