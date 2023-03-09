from libs.goto_leetcodepage import goto_leetcode
from playwright.sync_api import Page


def test_goto_leetcode(page: Page):
    goto_leetcode(page)
