library(tidyverse)
library(ggplot2)
library(data.table)
# Carregar log
log_file <- "auth.log"
logs <- fread(log_file, sep = " ", header = FALSE, fill = TRUE)

# Ajustar nome colunas
colnames(logs) <- c("Month", "Day", "Time", "Hostname", "Process", "Message")

# Filtrar login falha
failed_logins <- logs %>%
    filter(grepl("Failed password", Message)) %>%
    mutate(IP = str_extract(Message, "[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+")) %>%
    filter(!is.na(IP)) #Remove NAs se IP not found

failed.count <- failed_logins %>%
    group_by(IP) %>%
    summarise(Attemps = n()) %>%
print(failed.count)

brute_force_ips <- failed.count %>% filter(Attempts > 10)
print("IPs suspeitos de Brute:")
print(brute_force_ips)

ggplot(data = head(failed.count, 10), aes(x = reorder(IP, -Attempts), y = Attempts)) +
    geom_bar(stat = "Identity", fill ="red") +
    theme_minimal() +
    labs(title = "10 IPs com mais falhas de login"),
        x = "Endereço IP"
        y = "Número de Tentativas" +
    coord_flip()

# Export relatório
write.csv(failed.count, "ips_suspeitos.csv", row.names = FALSE)

cat("📊 Análise concluída. Relatório salvo em 'relatorio_ips_suspeitos.csv'.\n")