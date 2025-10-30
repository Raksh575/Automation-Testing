from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(10)
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = driver.find_element(By.ID, "flash").text
print("Message:", message)

driver.quit()
