from playwright.sync_api import sync_playwright 
import time



def test_goto_leetcode(page):
    # firefox = playwright.firefox
    # browser = firefox.launch()
    # page = browser.new_page()
    page.goto("https://www.google.com/")
    page.get_by_title("search").fill("leetcode")
    page.keyboard.press('Enter')
    time.sleep(3)
    #browser.close()

# with sync_playwright() as playwright:
#     test_goto_leetcode(playwright)

