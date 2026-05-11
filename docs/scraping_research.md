# Web Scraping vs. API Scraping with Python

<br>

### 1. Definitions
*   **Web Scraping (HTML Extraction):** This involves downloading the source code (HTML) of a webpage and parsing it to extract specific information. It is essentially an automated way of copying and pasting data that is displayed to human users. It is used when a website does not provide an official data export method.
*   **API Scraping (Service Consumption):** Modern websites often fetch data from an API (Application Programming Interface). Instead of parsing HTML, your script communicates directly with the server to request structured data, typically in **JSON** format. This method is faster, more reliable, and more efficient than traditional scraping.

<br>

### 2. How it is done with Python
Python is the industry standard for these tasks due to its powerful library ecosystem:

*   **For APIs:** The **Requests** library is the go-to tool. The process involves identifying the API endpoint (often found via the browser's "Network" tab), sending a request (GET/POST), and processing the JSON response into Python dictionaries.
*   **For Static Web Scraping:** Developers use **Requests** to fetch the HTML and **BeautifulSoup** to navigate the document tree (finding tags, classes, or IDs).
*   **For Dynamic Web Scraping:** Sites that rely on JavaScript (where content loads as you scroll or click) require browser automation tools like **Selenium** or **Playwright**. These tools control a real browser instance to render the page before extracting data.
*   **For Large-Scale Projects:** **Scrapy** is a professional-grade framework designed for high-performance crawling, handling data pipelines, and managing concurrent requests.

<br>

### 3. Critical Considerations
*   **Ethics and Legality:** Always check a site's `/robots.txt` file to understand their crawling policies. Respect terms of service and avoid "Denial of Service" (DoS) behavior by not overloading servers.
*   **Fragility:** Web scraping is highly dependent on the site's UI. If the website's layout or CSS classes change, the scraper will likely break and require maintenance.
*   **Anti-Bot Measures:** Many sites use CAPTCHA or IP rate-limiting. Strategies to bypass these include using proxies, rotating User-Agents, and implementing random delays between requests.
