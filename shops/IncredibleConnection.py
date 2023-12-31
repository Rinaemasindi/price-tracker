from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from .SaletrackerProductManager import SaletrackerProductManager

class IncredibleConnection:

    def __init__(self):
        fireFoxOptions = Options()
        fireFoxOptions.add_argument("--headless")
        self.driver = webdriver.Firefox(options=fireFoxOptions)
        # self.wait = WebDriverWait(self.driver, 10) 
             
        # Initialize SaletrackerDB and insert the product
        self.saletracker_db = SaletrackerProductManager('localhost', 'root', '', 'saletracker')       

    def is_button_enabled(self,driver):
        try:
            driver.find_element(By.XPATH, "//a[@class='action disabled  next']")
        except NoSuchElementException:
            return False
        return True
    
    def getAllproducts(self,link):
        
        all_products = []

        self.driver.get(link)
        
        while True:
            sleep(5)
            if self.check_exists_by_class_name(self.driver, 'products-grid'):
                product_grid = self.driver.find_element(By.CLASS_NAME, 'products-grid')
                products = product_grid.find_elements(By.CLASS_NAME, 'product-item')
                
                print(len(products))
                
                for product in products:
                    if(self.check_exists_by_class_name(product, 'price-container')):
                        product_image = product.find_element(By.CLASS_NAME, 'product-image-photo').get_attribute('src')
                        product_name = product.find_element(By.CLASS_NAME, 'product-item-name').get_attribute('innerText')
                        product_link = product.find_element(By.CLASS_NAME, 'product-item-link').get_attribute('href')
                        product_price = product.find_element(By.CLASS_NAME, 'price-container').find_element(By.CLASS_NAME, 'price').get_attribute('innerText').replace('\\xa0', ' ')
                                            
                        product_dict = {
                            "name":product_name,
                            "url":product_link,
                            "image":product_image,
                            "price":product_price,
                            "shop_id":8,
                            "product_type_id":None
                        }    
                        self.saletracker_db.insert_product(product_dict) 
                
                html = self.driver.find_element(By.TAG_NAME, 'html')
                html.send_keys(Keys.END)
                
                if self.is_button_enabled(self.driver) == False:
                    self.driver.find_element(By.CLASS_NAME, 'next').click()
                else:
                    break
            else:
                break

        self.driver.quit()     
        return True
    
    def check_exists_by_class_name(self,element, class_name):
        try:
            element.find_element(By.CLASS_NAME, class_name)
        except NoSuchElementException:
            return False
        return True
