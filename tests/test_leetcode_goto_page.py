from libs.goto_leetcodepage import gotoleetcode
from playwright.sync_api import Page


def test_goto_leetcode(page: Page):
    gotoleetcode(page)
