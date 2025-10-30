from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(10)
dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")
print("Selected:", dropdown.first_selected_option.text)

driver.quit()
