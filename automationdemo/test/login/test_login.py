import pytest
from playwright.sync_api import Page, expect

from automationdemo.src.pages.LoginPage import LoginPage
@pytest.mark.run_once
def test_Userlogin(set_up_tear_down) -> None:
    page =set_up_tear_down
    credentials ={"username":"Admin","password":"admin123"}
    login_p =LoginPage(page)
    dashboard_p=login_p.login(credentials)
    expect(dashboard_p.dashboard_header).to_have_text('Dashboard')