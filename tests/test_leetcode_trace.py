import time
from playwright.sync_api import sync_playwright
from data import config

username = config.username
password = config.password



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    # start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    page.locator(
            "//a[@href='https://leetcode.com/']//h3[@class='LC20lb MBeuO DKV0Md']").click()
    time.sleep(3)
    page.locator("//span[normalize-space()='Sign in']").click()
    time.sleep(5)
    page.get_by_role(
            "textbox", name='Username or E-mail').fill(username)
    time.sleep(3)
    page.get_by_role("textbox", name='Password').fill(password)
    time.sleep(3)
    page.locator("//button[@id='signin_btn']").click()
    time.sleep(3)
    page.locator("//a[contains(text(),'Explore')]").click()
    time.sleep(3)
    page.locator("body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > canvas:nth-child(2)").click()
    time.sleep(2)
    page.get_by_role("link", name="Problems").click()
    time.sleep(4)
    page.locator("div[class='swiper-slide w-auto swiper-slide-next'] span[class='relative inline-block overflow-hidden rounded md:rounded-[13px] shadow-level1 dark:shadow-dark-level1'] img[class='object-cover md:h-full md:w-full h-[100px] w-[200px]']").click()
    time.sleep(3)
    # scroll down page
    # page.mouse.wheel(0,800)
    page.keyboard.down('End')
    page.keyboard.up("Home")
    page.go_back()
    page.get_by_role("button", name="Interview").click()
    time.sleep(3)
    page.locator("//span[normalize-space()='Assessment']").click()
    time.sleep(3)
    page.locator("//a[normalize-space()='Discuss']").click()
    time.sleep(3)
    page.keyboard.down('End')
    page.locator("//a[normalize-space()='Students']").click()
    page.screenshot(path='leetcode student.png')
    page.close()
    # stop tracing
    context.tracing.stop(path="leetcode_trace.zip")
    context.close()