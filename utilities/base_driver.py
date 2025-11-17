from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# def get_driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     return driver

def get_driver(browser: str = "chrome"):
    browser = browser.lower()

    if browser=="chrome":
        service = ChromeService(ChromeDriverManager().install())  # <-- call install()
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    elif browser=="edge":
        service = EdgeService(executable_path="drivers\msedgedriver.exe")  # <-- call install()
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    elif browser == "mozila":
        service = FirefoxService(GeckoDriverManager().install())  # <-- call install()
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    else:
        raise ValueError(f"Unsupported browser: '{browser}'. Use chrome, edge, or mozila.")
