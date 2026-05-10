const { chromium } = require("playwright-extra");
const stealth = require("puppeteer-extra-plugin-stealth");
const { Client } = require("pg");

chromium.use(stealth());

async function runScraper() {
  // 1. Connect to Postgres
  const client = new Client({
    connectionString: process.env.DATABASE_URL,
  });
  await client.connect();

  // Create table if it doesn't exist
  await client.query(`
    CREATE TABLE IF NOT EXISTS listings (
      id SERIAL PRIMARY KEY,
      title TEXT,
      price TEXT,
      scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  `);

  // 2. Launch Browser
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  await page.goto("https://www.yad2.co.il/realestate/rent");
  await page.waitForTimeout(5000);
  await page.waitForSelector(".feed-item");

  // 3. Scrape Data
  const data = await page.$$eval(".feed-item", (elements) => {
    return elements.map((e) => ({
      title: e.querySelector(".title")?.innerText || "No Title",
      price: e.querySelector(".price")?.innerText || "No Price",
    }));
  });

  // 4. Save to Database
  for (const item of data) {
    await client.query("INSERT INTO listings (title, price) VALUES ($1, $2)", [
      item.title,
      item.price,
    ]);
  }

  console.log(`Successfully saved ${data.length} listings!`);
  await browser.close();
  await client.end();
}

runScraper().catch(console.error);
