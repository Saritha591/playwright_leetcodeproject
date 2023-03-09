from libs.weeklycontest332 import weeklycontest332
from playwright.sync_api import Page


def test_weeklycontesttab(page: Page):
    weeklycontest332(page)
