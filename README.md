Web Scraper
This Python script is a web scraper that extracts data from specific websites. It uses the requests library to fetch web pages and the BeautifulSoup library to parse the HTML content. The script supports scraping data from two websites: 'virginiasports' and 'yalebulldogs'.

Features
Retrieves web pages using customizable headers and timeouts
Extracts links from web pages
Scrapes information from web pages based on predefined patterns
Saves scraped data to CSV, Excel, HTML, or SQLite database
Provides logging functionality to track executed actions
Usage
Install the required dependencies: requests, beautifulsoup4, and pandas.
Run the script using python web_scraper.py.
Enter the URL of the website you want to scrape.
Provide the desired output file name and file type (CSV, Excel, HTML, or database).
The script will execute the appropriate scraping functions based on the provided URL and save the data to the specified output file.
A log file (log_file.txt) will be generated to track the actions performed.
Note: This script currently supports scraping only the 'virginiasports' and 'yalebulldogs' websites.
