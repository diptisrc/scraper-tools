
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Web Scraper - Read Me</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.5;
      padding: 20px;
    }
css
Copy code
h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

h2 {
  font-size: 18px;
  margin-bottom: 15px;
}

code {
  background-color: #f5f5f5;
  padding: 2px 4px;
  border-radius: 4px;
}
  </style>
</head>
<body>
  <h1>Web Scraper</h1>
  <p>This Python script is a web scraper that extracts data from specific websites. It uses the <code>requests</code> library to fetch web pages and the <code>BeautifulSoup</code> library to parse the HTML content. The script supports scraping data from two websites: 'virginiasports' and 'yalebulldogs'.</p>
  <h2>Features</h2>
  <ul>
    <li>Retrieves web pages using customizable headers and timeouts</li>
    <li>Extracts links from web pages</li>
    <li>Scrapes information from web pages based on predefined patterns</li>
    <li>Saves scraped data to CSV, Excel, HTML, or SQLite database</li>
    <li>Provides logging functionality to track executed actions</li>
  </ul>
  <h2>Usage</h2>
  <ol>
    <li>Install the required dependencies: <code>requests</code>, <code>beautifulsoup4</code>, and <code>pandas</code>.</li>
    <li>Run the script using <code>python web_scraper.py</code>.</li>
    <li>Enter the URL of the website you want to scrape.</li>
    <li>Provide the desired output file name and file type (CSV, Excel, HTML, or database).</li>
    <li>The script will execute the appropriate scraping functions based on the provided URL and save the data to the specified output file.</li>
    <li>A log file (<code>log_file.txt</code>) will be generated to track the actions performed.</li>
  </ol>
  <p><strong>Note:</strong> This script currently supports scraping only the 'virginiasports' and 'yalebulldogs' websites.</p>
</body>
</html>
