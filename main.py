from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

def test ():
    driver = webdriver.Chrome()
    driver.get("https://qa-practice.netlify.app/bugs-form")

    driver.find_element(By.ID, "firstName").send_keys("Juliana")
    driver.find_element(By.ID, "lastName").send_keys("Alarcon")
    driver.find_element(By.ID, "phone").send_keys("3205645247")
    Select(driver.find_element(By.ID, "countries_dropdown_menu")).select_by_value("Colombia")
    driver.find_element(By.ID, "emailAddress").send_keys("example@example.com")
    driver.find_element(By.ID, "password").send_keys("Prueba123")
    driver.find_element(By.ID, "exampleCheck1").click()
    driver.find_element(By.ID, "registerBtn").click()
    time.sleep(8)
