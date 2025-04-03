use std::net::{TcpStream, SocketAddr};
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

const THREADS: u16 = 50; // Número de threads para acelerar o scan

fn scan_port(ip: &str, port: u16, sender: mpsc::Sender<u16>) {
    let address = format!("{}:{}", ip, port);
    let socket: SocketAddr = address.parse().expect("Invalid address");

    if TcpStream::connect_timeout(&socket, Duration::from_millis(500)).is_ok() {
        sender.send(port).expect("Failed to send port");
    }
}

fn main() {
    let target = "192.168.1.1"; // IP alvo (altere conforme necessário)
    let port_range = 1..=65535; // Intervalo de portas scan

    let (sender, receiver) = mpsc::channel(); // Canal comunicação threads
    let mut handles = vec![];

    for chunk in port_range.clone().collect::<Vec<u16>>().chunks(THREADS as usize) {
        for &port in chunk {
            let sender = sender.clone();
            let ip = target.to_string();

            let handle = thread::spawn(move || {
                scan_port(&ip, port, sender);
            });

            handles.push(handle);
        }

        // Aguarda as threads terminarem antes de continuar
        for handle in handles.drain(..) {
            handle.join().unwrap();
        }
    }

    // Exibe as portas abertas encontradas
    println!("\n🔎 **Portas Abertas:**");
    drop(sender); // Fecha o canal de comunicação

    for port in receiver.iter() {
        println!("✔ Porta {} aberta!", port);
    }
}
