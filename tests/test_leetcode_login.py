from libs.loginpage import login_leetcode
from playwright.sync_api import Page


def test_login_leetcode(page: Page):
    login_leetcode(page)
