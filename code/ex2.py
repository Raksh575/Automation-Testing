from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(10)

products = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")[:5]
for idx, product in enumerate(products, start=1):
    print(f"{idx}. {product.text}")

driver.quit()
