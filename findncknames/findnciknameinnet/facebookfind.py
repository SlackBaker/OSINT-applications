from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def bioofuser(nickname):
    driver = webdriver.Chrome()

    # 1. відкриваємо профіль
    driver.get(f"https://www.facebook.com/{nickname}")
    time.sleep(7)

    try:
        # 2. шукаємо більш точково
        bio_elements = driver.find_elements(By.XPATH, "//div[@data-pagelet]//span")

        for b in bio_elements:
            text = b.text

            if any(keyword in text for keyword in [
                "Lives in", "From", "Studied at", "Works at"
            ]):
                print("[BIO]", text)

    except Exception as e:
        print("[-] Bio is not found", e)

    driver.quit()