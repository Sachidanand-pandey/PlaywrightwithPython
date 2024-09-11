import pytest
import random
from playwright.sync_api import Page, expect
from automationdemo.src.pages.LoginPage import LoginPage
from automationdemo.src.pages.UserPage import UserPage

rand_num = random.randint(1, 10000)

@pytest.mark.run_once
def test_UserManagementSearch(set_up_tear_down) -> None:
    page =set_up_tear_down
    credentials = {"username": "Admin", "password": "admin123"}
    login_p = LoginPage(page)
    dashboard_p = login_p.login(credentials)
    user = {"username":"Admin"}
    user_p =UserPage(page)
    user_p.searchuser(user)
    expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser/1'

    # Verify the URL
    expect(page).to_have_url(expected_url)

@pytest.mark.run_once
def test_AddNewUser(set_up_tear_down)->None:
    page = set_up_tear_down
    credentials = {"username": "Admin", "password": "admin123"}
    login_p = LoginPage(page)
    dashboard_p = login_p.login(credentials)
    cred ={"empname":"j","username":f"hello{rand_num}","pass":"Qwerty@123","conpass":"Qwerty@123","message":"Successfully Saved"}
    user_p = UserPage(page)
    user_p.verify_addNewUser(cred)



