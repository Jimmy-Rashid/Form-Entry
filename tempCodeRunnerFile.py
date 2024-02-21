        # Submits message to realtor
        submit_button = driver.find_element(
            by=By.CLASS_NAME, value="submit-button_topSpacing__VxWzR"
        )
        submit_button.click()

        # For deployment
        close_button = driver.find_element(
            by=By.CLASS_NAME, value="cta-modal_closeButton__jsMbk"
        )
        close_button.click()