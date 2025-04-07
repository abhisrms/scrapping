# import requests
# from bs4 import BeautifulSoup

# # Target URL
# url = "http://quotes.toscrape.com"

# try:
#     # Fetch webpage
#     response = requests.get(url)
#     response.raise_for_status()  # Check for HTTP errors

#     # Parse HTML
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extract quotes and authors
#     quotes = soup.find_all('div', class_='quote')
    
#     for quote in quotes:
#         text = quote.find('span', class_='text').text
#         author = quote.find('small', class_='author').text
#         print(f"Quote: {text}\nAuthor: {author}\n{'-'*50}")

# except requests.exceptions.RequestException as e:
#     print(f"Error fetching the page: {e}")

import requests
 
from bs4 import BeautifulSoup
import csv
from time import sleep
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(url)
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# Set headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Create a CSV file
with open('xiaomi_phones.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price', 'Rating', 'Specifications', 'URL'])

        # Scrape multiple pages
    for page in range(1, 6):  # First 5 pages
        url = f'https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy%2C4io&q=xiaomi&otracker=categorytree&page={page}'
            
        try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all product containers
                products = soup.find_all('div', {'class': 'cPHDOP col-12-12'})  # Update class if needed
                # print(products)
                for product in products:
                    # Extract name
                    name = product.find('div', {'class': 'KzDlHZ'})
                    name = name.text if name else None
                    if name:
                        # Extract price
                        price = product.find('div', {'class': 'Nx9bqj'})
                        price = price.text if price else 'N/A'
                        
                        # Extract rating
                        rating = product.find('div', {'class': '_5OesEi'})
                        rating = rating.text if rating else 'N/A'
                        
                        # Extract specifications
                        specs = product.find('div', {'class': '_6NESgJ'})
                        specs = specs.text.replace('\n', ', ') if specs else 'N/A'
                        
                        # Extract product URL
                        product_url_tag = product.find('a', {'class': 'CGtC98'})
                        product_url = f"https://www.flipkart.com{product_url_tag['href']}" if product_url_tag else 'N/A'
                        
                        # Print formatted output
                        # print(f"Name: {name}")
                        # print(f"Price: {price}")
                        # print(f"Rating: {rating}")
                        # print(f"Specs: {specs}")
                        # print(f"URL: {product_url}")
                        # print("-" * 50)
                        writer.writerow([name, price, rating, specs, product_url])
                print(f'Page {page} scraped.')
                sleep(10)  # Avoid overwhelming the server
                
        except Exception as e:
                print(f'Error on page {page}: {str(e)}')

# import os
# print(f"CSV will be saved to: {os.getcwd()}")