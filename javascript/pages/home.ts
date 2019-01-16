class Home_Page {

    public get searchInput() { return $('#search_form_input_homepage') }
    public get menuBar() { return $('js-side-menu-open') }
    public get closeMenuBar() { return $('js-side-menu-close') }
    public get bangSearchShortcuts() { return $('//a[text()="!Bang Search Shortcuts"]') }
    public get ddgBadge() { return $('js-badge-link-dismiss') }
    public get ddgPrivacyBadge() { return $('js-badge-link-close') }

    public performSearch(query: string): void {
        this.searchInput.setValue(query)
    }

    public closeBadgeCards(): void {
        if (this.ddgBadge.isDisplayed) {
            this.ddgBadge.click()
        }

        if (this.ddgPrivacyBadge.isDisplayed) {
            this.ddgPrivacyBadge.click()
        }
    }
}

const HomePage = new Home_Page();
export default HomePage;