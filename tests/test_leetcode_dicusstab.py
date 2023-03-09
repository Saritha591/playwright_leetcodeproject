from libs.leetcode_discusstab import leetcode_discusstab
from playwright.sync_api import Page


def test_discusstab(page: Page):
    leetcode_discusstab(page)
