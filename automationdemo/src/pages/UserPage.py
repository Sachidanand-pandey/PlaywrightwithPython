import time
from os import times
from playwright.sync_api import Page, expect



from pyexpat.errors import messages


class UserPage:
    def __init__(self,page):
        self.page = page
        self._Admin =  page.locator('(//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"])[1]')
        self._searchUser =page.locator('(//input[@class="oxd-input oxd-input--active"])[2]')
        self._searchbtn =page.locator('//button[@type="submit"]')
        self._result =page.locator('//div[@class="oxd-table-card"]//div[2]//div')
        self._order =page.locator('(//i[@class="oxd-icon bi-pencil-fill"])[1]')
        self._addbtn =page.locator('[class="oxd-icon bi-plus oxd-button-icon"]')
        self._roledropdown =page.locator('(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]')
        self._adminoption =page.locator('(//span[text()="Admin"])[2]')
        self._empname =page.locator('[placeholder="Type for hints..."]')
        self._selectsuggection =page.locator('(//div[@role="option"])[1]')
        self._statusdropdown =page.locator('(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[2]')
        self._enabledoption =page.locator('//span[text()="Enabled"]')
        self._username =page.locator('(//input[@autocomplete="off"])[1]')
        self._password =page.locator('(//input[@type="password"])[1]')
        self._confirmpass =page.locator('(//input[@type="password"])[2]')
        self._success =page.locator('[class="oxd-toast-container oxd-toast-container--bottom"]')



    def click_Admin(self):
        self._Admin.click()

    def enter_serachbox(self,name):
        self._searchUser.fill(name)

    def click_searchbtn(self):
        self._searchbtn.click()

    def verify_serchResult(self,user):
        expect(self._result).to_have_text(user)

    def click_order(self):
        self._order.click()



    def searchuser(self,user):
        self.click_Admin()
        self.enter_serachbox(user['username'])
        self.click_searchbtn()
        self.verify_serchResult(user['username'])
        self.click_order()

    def addbtn(self):
        self._addbtn.click()

    def click_roledropdown(self):
        self._roledropdown.click()

    def click_adminoption(self):
        self._adminoption.click()

    def enter_empname(self,name):
        self._empname.fill(name)

    def select_suggestion(self):
        self._selectsuggection.click()


    def click_statusdropdown(self):
        self._statusdropdown.click();

    def click_enabledoptio(self):
        self._enabledoption.click();

    def enter_username(self,username):
        self._username.fill(username)

    def enter_password(self,password):
        self._password.fill(password)

    def enter_confirmpass(self,confirmpass):
        self._confirmpass.fill(confirmpass)



    def verify_addNewUser(self,cred):
        self.click_Admin()
        self.addbtn()
        self.click_roledropdown()
        self.click_adminoption()
        self.enter_empname(cred['empname'])
        self.select_suggestion()
        self.click_statusdropdown()
        self.click_enabledoptio()
        self.enter_username(cred['username'])
        self.enter_password(cred['pass'])
        self.enter_confirmpass(cred['conpass'])
        self.click_searchbtn()














