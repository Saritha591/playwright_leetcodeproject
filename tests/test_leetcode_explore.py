from libs.leetcode_explore import leetcodeexplore
from playwright.sync_api import Page


def test_leetcode_exploretab(page: Page):
    leetcodeexplore(page)
