from automationdemo.src.pages.dashboard import PageDashboard


class LoginPage:
    def __init__(self,page):
        self.page = page
        self._username =  page.locator('[name="username"]')
        self._password = page.locator('[name="password"]')
        self._loginbtn = page.locator('[type="submit"]')

    def enter_username(self,username):
        self._username.fill(username)


    def enter_password(self,passw):
        self._password.fill(passw)

    def click_loginBtn(self):
        self._loginbtn.click()

    def login(self,credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_loginBtn()
        return PageDashboard(self.page)

        self.cookies = self.page.context.cookies()



