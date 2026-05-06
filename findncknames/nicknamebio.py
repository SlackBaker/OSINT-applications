import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FacebookBio:
    def __init__(self, driver, username):
        self.driver = driver
        self.username = username

    def checkbio(self):
        print(f"Checking Facebook for: {self.username}")
        self.driver.get(f"https://www.facebook.com/{self.username}")
        time.sleep(30)  # Даємо час завантажитись


class InstaBio:
    def __init__(self, driver, username):
        self.driver = driver
        self.username = username

    def checkbio(self):
        print(f"Checking Instagram for: {self.username}")
        self.driver.get(f"https://www.instagram.com/{self.username}/")
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, "//meta[@property='og:description']")))
            bio = self.driver.find_element(By.XPATH, "//meta[@property='og:description']").get_attribute("content")
            print("[+] Bio found:", bio)
        except:
            print("[-] Bio not found")


def nicknamebio():
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    try:
        driver = webdriver.Chrome(options=options)
    except:
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    username = input("Enter username: ")

    fb = FacebookBio(driver, username)
    insta = InstaBio(driver, username)

    insta.checkbio()
    fb.checkbio()

    input("press enter to exit...")
    driver.quit()