class Home_Page {

    public get searchInput() { return $('#search_form_input_homepage') }
    public get menuBar() { return $('.js-side-menu-open') }
    public get closeMenuBar() { return $('.js-side-menu-close') }
    public get bangSearchShortcuts() { return $('//a[text()="!Bang Search Shortcuts"]') }
    public get ddgBadge() { return $('.js-badge-link-dismiss') }
    public get ddgPrivacyBadge() { return $('.js-badge-link-close') }

    public performSearch(query: string): void {
        this.searchInput.click()
        browser.keys(query)
        browser.keys("Return")
    }

    public closeBadgeCards(): void {
        browser.waitUntil(() => {
            return this.ddgBadge.isEnabled()
        }, 2000, 'Expected the DDG privacy badge to appear');
        this.ddgBadge.click();
        browser.waitUntil(() => {
            return this.ddgPrivacyBadge.isEnabled()
        }, 2000, 'Expected second DDG privady badge to appear');
        this.ddgPrivacyBadge.click();
    }
}

const HomePage = new Home_Page();
export default HomePage;