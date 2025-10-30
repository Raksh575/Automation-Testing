from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
time.sleep(10)
driver.save_screenshot("google.png")
print("Screenshot saved!")

driver.quit()
