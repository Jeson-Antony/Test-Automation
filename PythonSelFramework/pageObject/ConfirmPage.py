from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country_words = (By.ID, "country")
    get_countries = (By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
    click_checkbox = (By.CSS_SELECTOR, "div[class = 'checkbox checkbox-primary']")
    click_purchase = (By.CSS_SELECTOR, "input[class = 'btn btn-success btn-lg']")
    success_message = (By.CLASS_NAME, "alert-success")
    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country_words)
    def getCountryNames(self):
        return self.driver.find_elements(*ConfirmPage.get_countries)
    def CheckBox(self):
        return self.driver.find_element(*ConfirmPage.click_checkbox)
    def Purchase(self):
        return self.driver.find_element(*ConfirmPage.click_purchase)
    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.success_message)