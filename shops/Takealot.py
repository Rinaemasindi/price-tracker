from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Takealot:

    def __init__(self):
        fireFoxOptions = Options()
        # fireFoxOptions.add_argument("--headless")
        self.driver = webdriver.Firefox(options=fireFoxOptions)
        # self.wait = WebDriverWait(self.driver, 10)            

    def check_if_img_exits(self, element):
        try:
            element.find_element(By.TAG_NAME, 'img')
        except NoSuchElementException:
            return False
        return True    
             
    def getAllproducts(self,link):
        
        all_products = []

        self.driver.get(link)
        while True:
            sleep(5)
            product_grid = self.driver.find_element(By.CLASS_NAME, 'listings-container-module_listings-container_AC4LI')
            products = product_grid.find_elements(By.CLASS_NAME, 'product-card')
            
            print(len(products))
            
            if len(products) > 100:
                break
            
            html = self.driver.find_element(By.TAG_NAME, 'html')
            html.send_keys(Keys.END)
            
            if self.check_exists_by_class_name(self.driver, 'search-listings-module_load-more_OwyvW'):
                self.driver.find_element(By.CLASS_NAME, 'search-listings-module_load-more_OwyvW').click()      
            else:
                break
        
        for product in products:
            
            product_name = product.find_element(By.CLASS_NAME, 'product-title').get_attribute("innerText")
            product_url = product.find_element(By.CLASS_NAME, 'product-card-module_product-anchor_TUCBV').get_attribute("href")
            product_price = product.find_element(By.CLASS_NAME, 'product-card-module_price_zVU6d').get_attribute("innerText")
                
            if self.check_if_img_exits(product):
                product_image = product.find_element(By.TAG_NAME, 'img').get_attribute("src")            
            else:
                product_image = None
            
            product_dict = {
                "name":product_name,
                "url":product_url,
                "image":product_image,
                "price":product_price
            }    
            
            all_products.append(product_dict)             
        
        self.driver.quit()
        return all_products
            
    def check_exists_by_class_name(self,element, class_name):
        try:
            element.find_element(By.CLASS_NAME, class_name)
        except NoSuchElementException:
            return False
        return True
