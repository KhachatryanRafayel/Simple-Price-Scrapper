from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from config import css_selectors #dict with css selectors
import time

def get_item_price(item_nubmer):
    """
    Gets the price of a product from Wildberries

    Args:
        item_number (int or string): product code used to identify an item on an online marketplace
        
    Returns:
        str: Product price or None if there's an error
    """
    
    url = f"https://www.wildberries.am/catalog/{item_nubmer}/detail.aspx"

    try:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        driver.get(url)
        
        # Waiting for content to load
        time.sleep(3)
        
        price_css_selector = "ins.priceBlockFinalPrice--iToZR.redPrice--iueN6"

        # We use WebDriverWait for reliability
        price_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(By.CSS_SELECTOR, price_css_selector)
        )
        
        price_text = price_element.text

        if price_text:
            clean_price = price_text.replace('драм', '').replace(' ', '')
            return clean_price
        else:
            return None
            
    except Exception as e:
        print(f" Parsing error: {str(e)}")
        return None
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error when closing the browser: {e}")

def main():
    example_article = 268131354
    print(get_item_price(example_article))

if __name__ == "__main__":
    main()