from libs.leetcode_explore import leetcode_explore
from playwright.sync_api import Page


def test_leetcode_exploretab(page: Page):
    leetcode_explore(page)
