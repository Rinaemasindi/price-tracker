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
    
    def phones(self,):
        self.driver.get('https://www.takealot.com/cellular-gps/cellphones-26249?sort=Price%20Descending')
        while True:
            sleep(5)
            product_grid = self.driver.find_element(By.CLASS_NAME, 'listings-container-module_listings-container_AC4LI')
            products = product_grid.find_elements(By.CLASS_NAME, 'product-card')
            
            print(len(products))
            
            html = self.driver.find_element(By.TAG_NAME, 'html')
            html.send_keys(Keys.END)
            
            if self.check_exists_by_class_name('search-listings-module_load-more_OwyvW'):
                self.driver.find_element(By.CLASS_NAME, 'search-listings-module_load-more_OwyvW').click()      
            else:
                break
            
        print(products)
            
    def check_exists_by_class_name(self, class_name):
        try:
            self.driver.find_element(By.CLASS_NAME, class_name)
        except NoSuchElementException:
            return False
        return True
