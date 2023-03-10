import time
from playwright.sync_api import sync_playwright, Page
from data import config

username = config.username
password = config.password

def test_begginerguide(page):
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
    page.locator("//a[contains(text(),'Explore')]").click()
    time.sleep(3)
    page.locator("body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > canvas:nth-child(2)").click()
    time.sleep(2)