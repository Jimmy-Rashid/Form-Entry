from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
import pandas as amogus
import time

previous_lobby = amogus.read_excel("master.xlsx")
impostors = amogus.DataFrame(previous_lobby[["Name"]])
impostors.set_index("Name", inplace=True)
crewmate_list = []

daily_login = time.strftime("%x")

options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_argument("--remote-allow-origins=*")
options.add_argument("--disable-extensions")
options.add_argument("--guest")

driver = webdriver.Edge(
    service=EdgeService(EdgeChromiumDriverManager().install()), options=options
)

# Choose city

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Burnaby Real Estate Agents
driver.get("https://www.remax.ca/bc/burnaby-real-estate-agents?pageNumber=1")

# Vancouver Real Estate Agents
# driver.get(https://www.remax.ca/bc/vancouver-real-estate-agents?pageNumber=1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

title = driver.title

driver.implicitly_wait(1)
index = 1


def send_message(index, crewmate_list):
    # Find the realtor's information
    card_parent_css = f"#__next > div.base-layout_root__gpH78.globalBodyPadding > div > div > div:nth-child({index}) > div.card-with-buttons_content__PJCfJ > a > div.agent-search-card_textContent__lMG47"
    card_parent = driver.find_element(by=By.CSS_SELECTOR, value=card_parent_css)

    realtor_name_css = card_parent.find_element(
        by=By.CLASS_NAME, value="agent-search-card_name__FKvox"
    )
    realtor_name = realtor_name_css.text

    if realtor_name not in impostors.index:
        realtor_title_css = card_parent.find_element(
            by=By.CLASS_NAME, value="agent-search-card_title__rqNB0"
        )
        realtor_title = realtor_title_css.text

        realtor_city_css = card_parent.find_element(
            by=By.CLASS_NAME, value="agent-search-card_city__dFVTO"
        )
        realtor_city = realtor_city_css.text

        realtor_office_css = card_parent.find_element(
            by=By.CLASS_NAME, value="agent-search-card_office__Wqx3q"
        )
        realtor_office = realtor_office_css.text

        # Allow some time to wait window closure

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        time.sleep(3)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # Press contact button
        contact_button_css = f"#__next > div.base-layout_root__gpH78.globalBodyPadding > div > div > div:nth-child({index}) > div.card-with-buttons_buttonWrapper__dvc9K > button.MuiButtonBase-root.MuiButton-root.commercialOutlined.agent-office-search-card-base_blueButton__unMZ4.MuiButton-text.remax-button_buttonText__saWK7 > span"
        contact_button = driver.find_element(
            by=By.CSS_SELECTOR, value=contact_button_css
        )
        contact_button.click()

        # Enter name
        name_entry = driver.find_element(by=By.NAME, value="name")
        name_entry.send_keys("Kevin Barrett")

        # Enter email
        email_entry = driver.find_element(by=By.NAME, value="email")
        email_entry.send_keys("kevinbarrett@packbuildings.com")

        # Uncheck "Looking to buy" button
        buy_button = driver.find_element(by=By.NAME, value="buy")
        buy_button.click()

        # Find message box
        message_entry = driver.find_element(by=By.NAME, value="message")
        message_copy = message_entry.text
        words = message_copy.split(" ")[:2]
        message_entry.send_keys(Keys.CONTROL + "a")
        message_entry.send_keys(Keys.DELETE)

        greeting = " ".join(words)
        message = (
            greeting
            + " I am reaching out as the VP of Sales for Pack Buildings. We are a technology powered developer with an innovative new product coming out to service the laneway home space. I would like to buy you a coffee to tell you more about how you can use this to generate more clients and increase the yield on your listings. Feel free to text or email. Have a great day. "
            + "\n\nKevin Barrett\nkevinbarrett@packbuildings.com\nhttps://www.linkedin.com/in/kevinbarrett76/"
        )

        message_entry.send_keys(message)

        driver.implicitly_wait(1)

        # For sending message

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # Submits message to realtor
        submit_button = driver.find_element(
            by=By.CLASS_NAME, value="submit-button_topSpacing__VxWzR"
        )
        submit_button.click()

        driver.implicitly_wait(1)

        # For deployment
        close_button = driver.find_element(
            by=By.CLASS_NAME, value="cta-modal_closeButton__jsMbk"
        )
        close_button.click()

        # # For testing
        # close_button = driver.find_element(
        #     by=By.CSS_SELECTOR,
        #     value='[aria-label="Close"]',
        # )
        # close_button.click()

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

        crewmate_list.append(
            amogus.DataFrame(
                {
                    "Name": [realtor_name],
                    "Title": [realtor_title],
                    "City": [realtor_city],
                    "Office": [realtor_office],
                    "Day": [daily_login],
                }
            ),
        )

        print(realtor_name)
        print(realtor_title)
        print(realtor_city)
        print(realtor_office)
        print(daily_login)
        print(" ")

    # Change number to control amount of entries
    if index < 9:
        send_message(index + 1, crewmate_list)


send_message(index, crewmate_list)

# For saving realtor names, offices, etc.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

lobby = amogus.concat(crewmate_list, ignore_index=True)
lobby.to_excel("output.xlsx", index=False)

lobby_update = amogus.concat([previous_lobby, lobby], ignore_index=True)
lobby_update.to_excel("master.xlsx", index=False)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

time.sleep(3)

driver.quit()
