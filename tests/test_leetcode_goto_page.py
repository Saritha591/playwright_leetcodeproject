from playwright.sync_api import sync_playwright
import time
from data import details

username = details.username
password = details.password


def test_goto_leetcode(page):
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    time.sleep(3)

