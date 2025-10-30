from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
time.sleep(10)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

# ✅ Wait until results are visible
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
)

results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]
for r in results:
    print(r.text)

driver.quit()
