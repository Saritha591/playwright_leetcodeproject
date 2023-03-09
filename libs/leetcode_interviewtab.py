#import time
#from playwright.sync_api import sync_playwright, Page
from data import details

username = details.username
password = details.password


def leetcode_interview(page):
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    page.locator(
        "//a[@href='https://leetcode.com/']//h3[@class='LC20lb MBeuO DKV0Md']").click()
    page.locator("//span[normalize-space()='Sign in']").click()
    page.get_by_role(
        "textbox", name='Username or E-mail').fill(username)
    page.get_by_role("textbox", name='Password').fill(password)
    page.locator("//button[@id='signin_btn']").click()
    page.locator("//a[contains(text(),'Explore')]").click()
    page.locator("body > div:nth-child(12) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > canvas:nth-child(2)").click()
    page.get_by_role("link", name="Problems").click()
    page.locator("div[class='swiper-slide w-auto swiper-slide-next'] span[class='relative inline-block overflow-hidden rounded md:rounded-[13px] shadow-level1 dark:shadow-dark-level1'] img[class='object-cover md:h-full md:w-full h-[100px] w-[200px]']").click()
    #scroll down page
    #page.mouse.wheel(0,800)
    page.keyboard.down('End')
    page.keyboard.up("Home")
    page.go_back()
    page.get_by_role("button",name="Interview").click()
    page.locator("//span[normalize-space()='Assessment']").click()