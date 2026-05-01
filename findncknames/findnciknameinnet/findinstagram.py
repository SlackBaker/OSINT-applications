from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def findbio(username):
    driver = webdriver.Chrome()
    driver.get(f"https://www.instagram.com/{username}/")

    time.sleep(5)

    try:
        bio = driver.find_element(By.XPATH, "//meta[@property='og:description']").get_attribute("content")
        print("[+] Bio:", bio)
    except:
        print("[-] Не вдалося отримати біо")

    driver.quit()
