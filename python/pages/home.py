from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Home(Page):

    homePage = "https://duckduckgo.com"

    searchInput = (By.ID, "search_form_input_homepage")
    menuBar = (By.CLASS_NAME, "js-side-menu-open")
    closeMenuBar = (By.CLASS_NAME, "js-side-menu-close")
    bangSearchShortcuts = (By.XPATH, "//a[text()='!Bang Search Shortcuts']")
    ddgBadge = (By.CLASS_NAME, "js-badge-link-dismiss")
    ddgPrivacyBadge = (By.CLASS_NAME, "js-badge-link-close")

    def performSearch(self, query):
        searchBar = self.driver.find_element(*self.searchInput)
        searchBar.send_keys(query)
        searchBar.send_keys(Keys.RETURN)