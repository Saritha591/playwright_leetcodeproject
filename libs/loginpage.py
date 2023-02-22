from playwright.sync_api import sync_playwright, Page
import time
from data import details

username = details.username
password = details.password


def login_leetcode(page):
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    time.sleep(3)
    page.locator(
        "//a[@href='https://leetcode.com/']//h3[@class='LC20lb MBeuO DKV0Md']").click()
    time.sleep(3)
    page.locator("//span[normalize-space()='Sign in']").click()
    time.sleep(3)
    page.get_by_role("textbox", name='Username or E-mail').fill(username)
    time.sleep(3)
    page.get_by_role("textbox", name='Password').fill(password)
    time.sleep(3)
    page.locator("//button[@id='signin_btn']").click()
    time.sleep(3)

