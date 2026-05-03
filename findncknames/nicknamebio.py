from findncknames import networkbio
from selenium import webdriver

def nicknamebio():
    driver = webdriver.Chrome()
    username =str(input("Enter username: "))

    bioface = networkbio.FacebookBio(driver, username)
    instabio = networkbio.InstaBio(driver, username)

    print("Facebook:",bioface)
    print("InstaBio:",instabio)