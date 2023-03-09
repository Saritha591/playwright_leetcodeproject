from libs.loginpage import loginleetcode
from playwright.sync_api import Page


def test_login_leetcode(page: Page):
    loginleetcode(page)
