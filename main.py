from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.page_load_strategy = "none"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://tinder.com")
time.sleep(3)

log_in = driver.find_element(By.XPATH, '//*[@id="c24809439"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
# print(log_in.text)
# log_in = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div/div/div[3]/div/span/a/button')
log_in.click()
time.sleep(5)

more_options_path = '//*[@id="c-1703571637"]/main/div/div/div[1]/div/div/div[3]/span/button'
more_option = driver.find_element(By.XPATH, more_options_path)
more_option.click()
time.sleep(2)

continue_facebook = driver.find_element(By.XPATH, '//*[@id="c-1703571637"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
print("more option does not exist")
continue_facebook.click()
time.sleep(2)

email = driver.find_element(By.CSS_SELECTOR, "#email")
print(email.text)

