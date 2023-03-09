from libs.leetcode_discusstab import leetcodediscusstab
from playwright.sync_api import Page


def test_discusstab(page: Page):
    leetcodediscusstab(page)
