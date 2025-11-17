import pytest
from utilities.base_driver import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser. Options: chrome, edge, mozila"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_driver()
    yield driver
    driver.quit()

