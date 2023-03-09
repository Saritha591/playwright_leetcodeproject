from libs.leetcode_begginerguide import begginerguide
from playwright.sync_api import Page


def test_begginerguidetab(page: Page):
    begginerguide(page)
