import requests 
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

def get_prod_details(product_url: str)->dict:
    product_details = {}
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.text, features='lxml')
    try:
        title = soup.find('span', attrs={'id': "productTitle"}).get_text().strip()
        extracted_price = soup.find(
            'span', attrs={'class': 'a-price'}).get_text().strip()
        price = '$' + extracted_price.split('$')[1]
        product_details['title'] = title
        product_details['price'] = price
        
        return product_details
    except Exception as e:
        print("Could not fetch product details")
        print(f'Failed with exception: {e}')

product_url = input("Enter the product URL: ")
product_details = get_prod_details(product_url)
print(product_details)