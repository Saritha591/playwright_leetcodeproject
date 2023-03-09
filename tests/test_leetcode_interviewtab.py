from libs.leetcode_interviewtab import leetcodeinterview
from playwright.sync_api import Page


def test_leetcode_interview(page: Page):
    leetcodeinterview(page)
