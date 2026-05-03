from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NetworkBio:
    def __init__(self, driver, username):
        self.driver = driver
        self.username = username

class FacebookBio(NetworkBio):
    def checkbio(self):
        self.driver.get(f"https://www.facebook.com/{self.username}")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            bio_elements = self.driver.find_elements(By.XPATH, "//div[@data-pagelet]//span")

            for b in bio_elements:
                text = b.text
                if any(keyword in text for keyword in [
                    "Lives in", "From", "Studied at", "Works at"
                ]):
                    print("[BIO]", text)

        except Exception as e:
            print("[-] Bio is not found", e)

class InstaBio(NetworkBio):
    def checkbio(self):
        self.driver.get(f"https://www.instagram.com/{self.username}")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        try:
            bio = self.driver.find_element(
                By.XPATH, "//meta[@property='og:description']"
            ).get_attribute("content")

            print("[+] Bio:", bio)

        except:
            print("[-] Bio is not found")