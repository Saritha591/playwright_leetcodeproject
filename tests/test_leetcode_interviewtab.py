from libs.leetcode_interviewtab import leetcode_interview
from playwright.sync_api import Page


def test_leetcode_interview(page: Page):
    leetcode_interview(page)
