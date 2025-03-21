import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Name is" + getData["Name"])
        homepage.getName().send_keys(getData["Name"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.checkBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        homepage.clickSubmit().click()
        alert = homepage.checkSuccessMessage().text
        assert "Success" in alert
        self.driver.refresh()
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param