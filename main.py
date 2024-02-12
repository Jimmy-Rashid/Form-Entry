from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_argument("--remote-allow-origins=*")
options.add_argument("--disable-extensions")

driver = webdriver.Edge(options=options)

driver.get("https://www.remax.ca/bc/vancouver-real-estate-agents?pageNumber=1")
title = driver.title
driver.implicitly_wait(0.5)

index = 1
css_selector = f"#__next > div.base-layout_root__gpH78.globalBodyPadding > div > div > div:nth-child({index}) > div.card-with-buttons_buttonWrapper__dvc9K > button.MuiButtonBase-root.MuiButton-root.commercialOutlined.agent-office-search-card-base_blueButton__unMZ4.MuiButton-text.remax-button_buttonText__saWK7 > span"

contact_button = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
contact_button.click()

name_entry = driver.find_element(by=By.NAME, value="name")
name_entry.send_keys("Kevin Barrett")
# text_box.send_keys("I'm working ? !")

time.sleep(5)

driver.quit()
