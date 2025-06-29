import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")

    yield driver

    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

    driver.quit()

def pytest_runtest_makereport(item, call):
    if "driver" in item.fixturenames:
        outcome = yield
        rep = outcome.get_result()
        setattr(item, "rep_" + rep.when, rep)
