from playwright.sync_api import Page

def test(page:Page):
    page.goto(" https://opensource-demo.orangehrmlive.com")

def test_login_sucess(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_label("Username").fill("Admin")
    page.get_by_label("Password").fill("admin123")


