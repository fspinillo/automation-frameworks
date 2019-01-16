var expect = require('chai').expect
import HomePage from '../pages/home'

describe('Performs tests on home page', () => {
    it('Tests performing a search', () => {
        browser.url('./');
        HomePage.performSearch('ducks');
        expect(browser.getTitle()).to.have('ducks')
    });
    it('Opens menu and goes to Bangs landing page', () => {
        browser.url('./');
        HomePage.closeBadgeCards();
        HomePage.menuBar.click();
        HomePage.bangSearchShortcuts.click();
        expect(browser.getTimeouts()).to.have('Bang')
    });
})