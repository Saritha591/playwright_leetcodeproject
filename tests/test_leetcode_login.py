import time
from playwright.sync_api import sync_playwright
from data import details

username = details.username
password = details.password


def test_login_leetcode(page):
    iphone_11 = page.devices["iphone 12"]
    browser = page.firefox.launch(headedless=False)
    context = browser.new_context(
        **iphone_12,
    )
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    time.sleep(3)
    page.locator(
        "//a[@href='https://leetcode.com/']//h3[@class='LC20lb MBeuO DKV0Md']").click()
    time.sleep(3)
    page.locator("//span[normalize-space()='Sign in']").click()
    time.sleep(5)
    page.get_by_role("textbox", name='Username or E-mail').fill(username)
    time.sleep(3)
    page.get_by_role("textbox", name='Password').fill(password)
    time.sleep(3)
    page.locator("//button[@id='signin_btn']").click()
    time.sleep(3)
   