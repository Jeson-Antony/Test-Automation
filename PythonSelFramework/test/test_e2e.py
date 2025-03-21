from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.shop_items().click()
        checkout_page = CheckoutPage(self.driver)
        log.info("Getting all the card titles")
        products = checkout_page.getProductItems()
        for product in products:
            phone_name = checkout_page.getProductNames(product).text
            log.info(phone_name)
            if phone_name == "Blackberry":
                checkout_page.addItemToCart(product).click()
        checkout_page.checkOutOne().click()
        checkout_page.checkOutSuccess().click()
        confirm_page = ConfirmPage(self.driver)
        log.info("Entering country name")
        confirm_page.getCountry().send_keys("un")
        self.verifyLinkPresence("United States of America")
        countries = confirm_page.getCountryNames()
        for country in countries:
            if country.text == 'United States of America':
                country.click()
                break
        confirm_page.CheckBox().click()
        confirm_page.Purchase().click()
        success = confirm_page.successMessage().text
        log.info("Text received from application is" + success)
        assert "Success! Thank you!" in success