import pytest
from time import sleep
from pages.home import Home

@pytest.mark.usefixtures("driver_setup")
class TestHomePage:

    @pytest.mark.search
    def test_search(self):
        home = Home(self.driver)
        self.driver.get(home.homePage)
        home.performSearch(query="ducks")
        assert 'ducks' in self.driver.title
    
    @pytest.mark.menu
    def test_view_bangs(self):
        home = Home(self.driver)
        self.driver.get(home.homePage)
        home.wait_to_click(home.ddgBadge)
        self.driver.find_element(*home.ddgPrivacyBadge).click()
        self.driver.find_element(*home.menuBar).click()
        home.wait_to_click(home.bangSearchShortcuts)
        assert 'Bang' in self.driver.title