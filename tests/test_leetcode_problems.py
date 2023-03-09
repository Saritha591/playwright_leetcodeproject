from libs.leetcode_problems import problemstab
from playwright.sync_api import Page


def test_problemtab(page: Page):
    problemstab(page)
