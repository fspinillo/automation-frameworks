var expect = require('chai').expect
import HomePage from '../pages/home'

describe('Performs tests on home page', () => {
    it('Tests performing a search', () => {
        browser.url('./');
        HomePage.performSearch("ducks");
        expect(browser.getTitle()).to.include("ducks")
    });
    it('Opens menu and goes to Bangs landing page', () => {
        browser.url('./');
        HomePage.closeBadgeCards();
        HomePage.menuBar.click();
        browser.waitUntil(() => {
            return HomePage.bangSearchShortcuts.isEnabled();
        }, 2000, "Expected th menu to fully load")
        HomePage.bangSearchShortcuts.click();
        browser.pause(1000)
        expect(browser.getTitle()).to.include("Bang")
    });
})