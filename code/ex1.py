from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.wikipedia.org/")
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium (software)")
    search_box.send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 1) 
    first_paragraph_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
    )
    first_paragraph = first_paragraph_element.text
    print("First Paragraph:", first_paragraph)
except TimeoutException:
    print("Error: The page took too long to load or the element wasn't found.")
finally:
    time.sleep(10)
    driver.quit()
