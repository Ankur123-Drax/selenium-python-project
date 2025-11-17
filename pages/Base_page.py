from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def moveToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scrollByPixels(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y});")