
from data import config

username = config.username
password = config.password


def leetcodeexplore(page):
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    page.locator(
        "//a[@href='https://leetcode.com/']//h3[@class='LC20lb MBeuO DKV0Md']").click()

    page.locator("//span[normalize-space()='Sign in']").click()
    page.get_by_role("textbox", name='Username or E-mail').fill(username)
    page.get_by_role("textbox", name='Password').fill(password)
    page.locator("//button[@id='signin_btn']").click()
    page.locator("//a[contains(text(),'Explore')]").click()