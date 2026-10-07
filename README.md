Amazon Web Scraper
A Python and Flask-based web scraping application that extracts product information from Amazon product pages and presents the results through a simple HTML interface.
Project Overview
The Amazon Web Scraper is a web application developed using Python, Flask, Requests, and BeautifulSoup. The application accepts an Amazon product URL from the user, sends a request to the webpage, processes the HTML content, extracts relevant product information, and displays the results in a user-friendly interface.
Features
• Accepts Amazon product URLs through a web interface
• Extracts product title
• Extracts product price
• Extracts product rating
• Extracts number of customer reviews
• Extracts product availability
• Provides a direct link to the Amazon product
• Handles invalid URLs and request errors
• Uses a separate scraper module for better code organization
Technologies Used
Python
Flask
Requests
BeautifulSoup4
HTML5
CSS3
Project Structure
How the Application Works
The user enters an Amazon product URL through the HTML interface. Flask receives the submitted URL and passes it to the scraping function. The Requests library retrieves the webpage content, while BeautifulSoup parses the HTML structure. The scraper identifies the required product elements and extracts their information. The extracted data is then returned to Flask and displayed on the webpage.
Installation
Clone the repository using:
git clone https://github.com/kayyanamburu0526-dev/Amazon-web-scraper.git
Navigate to the project directory:
cd Amazon-web-scraper
Install the required dependencies:
pip install -r requirements.txt
Running the Application
Start the Flask application using:
python app.py
Open a web browser and visit:
http://127.0.0.1:5000
Enter a valid Amazon product URL and submit the form to view the extracted product information.
Requirements
Python 3.x
Flask
Requests
BeautifulSoup4
Limitations
Amazon may restrict automated requests or display CAPTCHA and anti-bot verification pages. As a result, product information may not always be available through a basic HTTP scraping approach. The application is intended for educational and demonstration purposes.
Future Enhancements
Support scraping multiple products from search results
Add product images
Add price comparison and sorting
Add CSV export functionality
Improve error handling
Add a database for storing scraped information
Develop a more advanced user interface
Author
Kavya Namburu.
