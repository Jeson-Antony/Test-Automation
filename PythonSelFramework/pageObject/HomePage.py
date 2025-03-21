from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")
    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def checkBox(self):
        return self.driver.find_element(*HomePage.check)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def checkSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)
