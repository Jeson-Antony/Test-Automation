from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class = 'card h-100']")
    product_name = (By.XPATH, "div/h4/a")
    add_item = (By.XPATH, "div[2]/button")
    checkout_one = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkout_success = (By.CSS_SELECTOR, "button[class = 'btn btn-success']")
    def getProductItems(self):
        return self.driver.find_elements(*CheckoutPage.products)
    def getProductNames(self, product):
        return product.find_element(*CheckoutPage.product_name)
    def addItemToCart(self, product):
        return product.find_element(*CheckoutPage.add_item)
    def checkOutOne(self):
        return self.driver.find_element(*CheckoutPage.checkout_one)
    def checkOutSuccess(self):
        return self.driver.find_element(*CheckoutPage.checkout_success)
