import pytest
import allure

@pytest.fixture()
def set_up_tear_down(page)-> None:

    page.set_viewport_size({"width":1366, "height":768})
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield page

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        # Get the page object
        page = item.funcargs.get('page')
        if page:
            # Take a screenshot
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            # Attach the screenshot to the Allure report
            allure.attach.file(screenshot_path, name=f"Screenshot for {item.name}",
                               attachment_type=allure.attachment_type.PNG)