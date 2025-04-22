from pages.login_page import LoginPage

def test_login_valid_credentials(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(page)
    login.login("Admin", "admin123")
    assert "dashboard" in page.url.lower()


