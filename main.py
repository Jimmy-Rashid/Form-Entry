from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.EdgeOptions()
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_argument("--remote-allow-origins=*")
options.add_argument("--disable-extensions")

driver = webdriver.Edge(options=options)

driver.get("https://www.remax.ca/bc/vancouver-real-estate-agents?pageNumber=1")
title = driver.title

index = 1
driver.implicitly_wait(1)
css_selector = f"#__next > div.base-layout_root__gpH78.globalBodyPadding > div > div > div:nth-child({index}) > div.card-with-buttons_buttonWrapper__dvc9K > button.MuiButtonBase-root.MuiButton-root.commercialOutlined.agent-office-search-card-base_blueButton__unMZ4.MuiButton-text.remax-button_buttonText__saWK7 > span"


def send_message():
    # Press contact button
    contact_button = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
    contact_button.click()

    # Enter name
    name_entry = driver.find_element(by=By.NAME, value="name")
    name_entry.send_keys("Kevin Barrett")

    # Enter email
    email_entry = driver.find_element(by=By.NAME, value="email")
    email_entry.send_keys("kevinbarrett@packbuildings.com")

    # Find message box
    message_entry = driver.find_element(by=By.NAME, value="message")
    message_copy = message_entry.text
    words = message_copy.split(" ")[:2]
    message_entry.send_keys(Keys.CONTROL + "a")  # Select all text
    message_entry.send_keys(Keys.DELETE)  # Delete selected text

    greeting = " ".join(words)
    message = (
        greeting
        + " I am reaching out as the VP of Sales for Pack Buildings. We are a technology powered developer with an innovative new product coming out to service the laneway home space. I would like to buy you a coffee to tell you more about how you can use this to generate more clients and increase the yield on your listings. Feel free to text or email. Have a great day. "
        + "\n\nKevin Barrett\nkevinbarrett@packbuildings.com\nhttps://www.linkedin.com/in/kevinbarrett76/"
    )

    message_entry.send_keys(message)

    close_button = driver.find_element(
        by=By.CSS_SELECTOR,
        value='[aria-label="Close"]',
    )
    close_button.click()


send_message()

if driver.find_elements(By.CSS_SELECTOR, css_selector):
    index += 1
    send_message()

time.sleep(5)

driver.quit()
