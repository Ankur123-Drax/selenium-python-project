from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# def get_driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     return driver

def get_driver(browser: str = "chrome"):
    if browser=="chrome":
        service = Service(ChromeDriverManager().install())  # <-- call install()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    elif browser=="edge":
        service = Service(EdgeChromiumDriverManager.install())  # <-- call install()
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    elif browser == "mozila":
        service = Service(GeckoDriverManager.install())  # <-- call install()
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Use chrome, edge, or mozila.")
