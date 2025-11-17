import pytest
from utilities.base_driver import get_driver

@pytest.fixture
def driver(request):
    browser = request.c
    driver = get_driver()
    yield driver
    driver.quit()