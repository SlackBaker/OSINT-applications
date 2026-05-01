from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import asyncio
import time

sites = [
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.youtube.com",
    "https://www.linkedin.com",
    "https://www.reddit.com",
    "https://www.pinterest.com",
]

async def check():
    nickname = str(input("write nickname:"))
    for site in sites:
        driver = webdriver.Chrome()
        driver.get(site)

        time.sleep(5)

        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search Facebook']")
        search_box.send_keys(nickname)
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)
