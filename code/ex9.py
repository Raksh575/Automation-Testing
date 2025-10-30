from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(10)
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for cb in checkboxes:
    cb.click()
    # ✅ Correct: print checkbox state, not text
    print("Checked:", cb.is_selected())

driver.quit()
