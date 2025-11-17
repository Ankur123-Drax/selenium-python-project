from utilities.base_driver import get_driver
from pages.LandingPage import Landing_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# driver = get_driver()
# driver.get("https://ecommerce-playground.lambdatest.io/")

# topCategory=driver.find_element(By.XPATH,("//div[@id=\"mz-product-listing-39218404\"]/div/h3"))
# actions = ActionChains(driver)
# actions.move_to_element(topCategory).perform()

# driver.execute_script("window.scrollBy(0,400);")
# time.sleep(2)
# best_seller = driver.find_element(By.XPATH,("//a[@href=\"#mz-product-tab-39218404-2\"]"))
# best_seller.click()
# time.sleep(2)
# proName = driver.find_element(By.XPATH,("(//a[@class=\"text-ellipsis-2\" and @href=\"https://ecommerce-playground.lambdatest.io/index.php?route=product/product&product_id=47\" ])[2]")).text
# proPrice = driver.find_element(By.XPATH,("(//div[@class=\"price\"]/ancestor::div[@class=\"tab-pane fade active show\"]/div/div/div/div/div/div/span[@class=\"price-new\"])[1]")).text
# time.sleep(2)
# product = driver.find_element(By.XPATH,("//div[@id=\"mz-product-tab-39218404-2\"]//div[@class=\"swiper-slide swiper-slide-active\"]"))
# product.click()
# time.sleep(2)
# proAname = driver.find_element(By.XPATH,("//div[@id=\"entry_216816\"]/h1")).text
# driver.execute_script("window.scrollBy(0,100);")
# proAprice = driver.find_element(By.XPATH,("//div[@id=\"entry_216831\"]//h3")).text
# time.sleep(2)
# assert proAname == proName, f"Product name mismatch! Expected: {proAname}, Found: {proName}"
# print("Validation Successfull")
# time.sleep(2)
# assert proAprice == proPrice, f"Product price mismatch! Expected: {proAprice}, Found: {proPrice}"
# print("Validation Successfull")
# time.sleep(5)

def test_landingPage_product(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/")

    landing_page = Landing_Page(driver)

    landing_page.autoScrollToElement()

    landing_page.click_best_seller()

    productEname,productEprice= landing_page.getProductNameANdPrice()

    landing_page.click_product()

    productAname, productAprice = landing_page.getProductActualnameAndPrice()

    assert productAname == productEname, f"Product name mismatch! Expected: {productAprice}, Found: {productEname}"
    print("Validation Successfull")

    assert productAprice == productEprice, f"Product price mismatch! Expected: {productAprice}, Found: {productEname}"
    print("Validation Successfull")
    