import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def browse(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.get("https://mixitcloud.com/about")

        action = ActionChains(driver)
        time.sleep(5)

        driver.find_element(by=By.CSS_SELECTOR, value='button[data-cy="accept-cookies"]').click()

        driver.find_element(by=By.LINK_TEXT, value='Sign in').click()
# user id entry
        driver.find_element(by=By.CSS_SELECTOR, value='input#mat-input-0').send_keys("test@gmail.com")
# password entry
        driver.find_element(by=By.CSS_SELECTOR, value='input#mat-input-1').send_keys("test")
# login
        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

        time.sleep(5)
# input text in search box
        driver.find_element(by=By.CSS_SELECTOR, value='input[type="text"]').send_keys("HYR4R")

        driver.find_element(by=By.CSS_SELECTOR, value='svg[data-icon="magnifying-glass"]').click()
        time.sleep(3)
# clicking on the color chip for formula
        driver.find_element(by=By.XPATH, value='//span[@class="truncate" and text()="HYR4R (Pomegranate Red)"]').click()
        time.sleep(8)
# Selecting the required variant:
        driver.find_element(by=By.XPATH, value='//div[contains(text(),"HYR4R(B)")]').click()
        time.sleep(10)


# back arrow for the mix
        driver.find_element(by=By.CSS_SELECTOR, value='svg[data-icon="arrow-left"]').click()
# measurement section click
        driver.find_element(by=By.CSS_SELECTOR, value='a[data-cy="nav-measurements"]').click()
        time.sleep(5)
# click on date and time range
        driver.find_element(by=By.CSS_SELECTOR, value='div[data-cy="date-range-picker"]').click()
        time.sleep(3)
# click on the custom range
        driver.find_element(by=By.CSS_SELECTOR, value='button[data-cy="range-custom"]').click()
    #time.sleep(3)
# clicking on year
        driver.find_element(by=By.ID, value='mat-calendar-button-0').click()
# CLICKING RIGHT ARROW
        right_arrow= driver.find_element(by=By.CSS_SELECTOR, value="button[class*='mat-calendar-next-button']")

        action.double_click(right_arrow).perform()
        time.sleep(3)
        driver.find_element(by= By.XPATH, value='//div[contains(text(),"2022")]').click()
        time.sleep(3)
    #click on Month
        driver.find_element(by=By.XPATH, value='//div[contains(text(),"JUL")]').click()
        time.sleep(3)
    #click on start date
        driver.find_element(by=By.XPATH, value='//div[contains(text(),"13")]').click()
        time.sleep(3)
    #click on end date
        driver.find_element(by=By.XPATH, value='//div[contains(text(),"14")]').click()
        time.sleep(5)
    # Locate measurement ID
        ele = driver.find_element(by=By.XPATH, value='//span[text()="Car6"]/ancestor::app-own-measurements-card//button[@data-cy="bank-search"]')
        ele.click()
    # click on Champion color
        wait = WebDriverWait(driver, 40)
        ele = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[text()="Nutmeg Brown"]')))
        ele.click()

# clicking reports

        driver.find_element(by=By.CSS_SELECTOR, value="a[data-cy='nav-reports']").click()
# type in key letter in search field
        element = WebDriverWait(driver, 40).until(
            ec.element_to_be_clickable((By.NAME, 'WOid')))

        driver.execute_script('arguments[0].click();', element)


browse("firefox")


