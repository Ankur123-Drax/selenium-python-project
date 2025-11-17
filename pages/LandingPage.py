from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.Base_page import BasePage

class Landing_Page(BasePage):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    def autoScrollToElement(self):
        top_category = self.driver.find_element(
            By.XPATH, "//div[@id='mz-product-listing-39218404']/div/h3")
        self.moveToElement(top_category)
        self.scrollByPixels(0,400)
        time.sleep(2)

    def click_best_seller(self):
        best_seller = self.driver.find_element(
            By.XPATH, "//a[@href='#mz-product-tab-39218404-2']")
        best_seller.click()
        time.sleep(2)

    def getProductNameANdPrice(self):
        productNameE=self.driver.find_element(
           By.XPATH,("(//a[@class=\"text-ellipsis-2\" and @href=\"https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=47\" ])[2]")).text
        productPriceE=self.driver.find_element(
            By.XPATH, "(//div[@class='price']/ancestor::div[@class='tab-pane fade active show']/div/div/div/div/div/div/span[@class='price-new'])[1]").text
        return productNameE,productPriceE

    def click_product(self):
        product = self.driver.find_element(
            By.XPATH,(
                "//div[@id=\"mz-product-tab-39218404-2\"]//div[@class=\"swiper-slide swiper-slide-active\"]"))
        product.click()
        time.sleep(2)

    def getProductActualnameAndPrice(self):
        productAname=self.driver.find_element(
            By.XPATH, "//div[@id='entry_216816']/h1").text
        productAprice=self.driver.find_element(
           By.XPATH, "//div[@id='entry_216831']//h3").text
        return productAname,productAprice