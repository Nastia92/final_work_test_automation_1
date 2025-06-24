from selenium.webdriver.common.by import By

class AboutPage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators['about_page']
        self.about_link_locator = (By.CSS_SELECTOR, self.locators['about_link'])
        self.header_locator = (By.CSS_SELECTOR, self.locators['header'])

    def click_about_link(self):
        self.driver.find_element(*self.about_link_locator).click()

    def get_header_font_size(self):
        header = self.driver.find_element(*self.header_locator)
        return header.value_of_css_property("font-size")