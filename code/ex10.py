import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
# Create screenshots folder if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
time.sleep(10)
driver.save_screenshot("screenshots/google.png")
print("Screenshot saved!")

driver.quit()
