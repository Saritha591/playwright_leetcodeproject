from playwright.sync_api import sync_playwright
import time


def goto_leetcode(page):
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    time.sleep(3)