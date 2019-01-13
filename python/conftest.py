# -*- coding: utf-8 -*-
"""
Configuration file for pytest. This is where you can place pytest fixtures for
reuse around your testing framework
"""

import pytest
import json
import subprocess
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def pytest_addoption(parser):
    """Trying to use the built in argument parsing of python was interfering
    with the py.test library. This instead uses the parser built into py.test.
    It has to exist at the conftest level or else py.test will not read the
    parser addoptions"""
    parser.addoption("--browser", default='chrome', type='choice',
                     choices=('chrome', 'firefox'),
                     help='Define a location for tests to run')

@pytest.fixture
def driver_setup(request):
    """driver configuration for the tests. It refers to function it calls
    and then returns it for use in pytest. The yield acts a pseudo teardown
    for the tests"""
    browser = request.config.getoption('browser')
    request.instance.driver = driver_config(browser.lower())
    yield request.instance.driver
    request.instance.driver.quit()


@pytest.fixture
def mobile_driver_setup(request):
    """
    Uses Chrome's mobile emulation mode to run rests against an emulated device
    """
    mobile_emulation = {
        "deviceMetrics": {
            "width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU OS 11_0 like Mac OS X) "
                     "AppleWebKit/604.1.25 (KHTML, like Gecko) "
                     "Version/11.0 Mobile/15A372 Safari/604.1"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation",
                                           mobile_emulation)
    driver = webdriver.Chrome(
        desired_capabilities=chrome_options.to_capabilities())

    request.instance.driver = driver
    yield request.instance.driver
    request.instance.driver.quit()

def driver_config(browser):
    """Based on the param passed through configure the webdriver"""
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return driver