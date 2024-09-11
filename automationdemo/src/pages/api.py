# api_page.py
from playwright.sync_api import Page

class APIPage:
    def __init__(self, page: Page):
        self.page = page
        self.cookies = None

    def login_and_get_cookies(self):
        login_url = 'https://opensource-demo.orangehrmlive.com'
        username = 'Admin'
        password = 'admin123'

        self.page.goto(login_url)

        # Fill in the login form and submit
        self.page.fill('[name="username"]', username)
        self.page.fill('[name="password"]', password)
        self.page.click('[type="submit"]')
        self.page.wait_for_selector('//span[@class="oxd-topbar-header-breadcrumb"]')

        self.cookies = self.page.context.cookies()

    def fetch_user_details(self):
        if not self.cookies:
            self.login_and_get_cookies()

        cookie_header = '; '.join([f'{cookie["name"]}={cookie["value"]}' for cookie in self.cookies])
        headers = {
            'Cookie': cookie_header
        }

        response = self.page.request.get(
            'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC',
            headers=headers
        )
        return response
