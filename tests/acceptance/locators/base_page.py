from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  # short way to create a tuple same as TITLE = (by.TAG_NAME, 'h1')
    NAV_LINKS = (By.CLASS_NAME, 'nav-link')
