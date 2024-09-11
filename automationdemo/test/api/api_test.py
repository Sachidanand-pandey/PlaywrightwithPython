from automationdemo.src.pages.api import APIPage
from playwright.sync_api import sync_playwright

def test_user_details_api(set_up_tear_down) -> None:

    page =set_up_tear_down
    api_page = APIPage(page)
    response = api_page.fetch_user_details()
    assert response.status == 200, f"Expected status code 200 but got {response.status}"
    json_response = response.json()
    assert "data" in json_response, "Response JSON does not contain 'data' key"
    for user in json_response["data"]:
        assert "userName" in user
        assert "status" in user
        assert "employee" in user
        assert "userRole" in user







