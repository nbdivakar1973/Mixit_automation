import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import ActionChains


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
    driver.find_element(by=By.CSS_SELECTOR, value='input#mat-input-0').send_keys("divakar.nb@akzonobel.com")
# password entry
    driver.find_element(by=By.CSS_SELECTOR, value='input#mat-input-1').send_keys("Guru@1972")
# login
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()

    time.sleep(5)
# input text in search box
    driver.find_element(by=By.CSS_SELECTOR, value='input[type="text"]').send_keys("Silky silver Maruti")

    time.sleep(10)
# clicking on search icon
    driver.find_element(by=By.CSS_SELECTOR, value='svg[data-icon="magnifying-glass"]').click()
    time.sleep(6)
# clicking on the color chip for formula
    driver.find_element(by=By.CSS_SELECTOR, value="span.truncate").click()
    time.sleep(6)
# back arrow for the mix
    driver.find_element(by=By.CSS_SELECTOR, value='svg[data-icon="arrow-left"]').click()
# measurement section cliclk
    driver.find_element(by=By.CSS_SELECTOR, value='a[data-cy="nav-measurements"]').click()
    time.sleep(5)
# click on date and time range
    #driver.find_element(by=By.CSS_SELECTOR, value='div[data-cy="date-range-picker"]').click()
    #time.sleep(3)
# click on the custom range
    #driver.find_element(by=By.CSS_SELECTOR, value='button[data-cy="range-custom"]').click()
    #time.sleep(3)
# clicking on year
    #driver.find_element(by=By.CSS_SELECTOR, value='span#mat-calendar-button-0').click()
    #driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-multi-year-view/table/tbody/tr[2]/td[3]/button/div[1]').click()

    #right_arrow= driver.find_element(by=By.CSS_SELECTOR, value='button.mat-calendar-next-button')
    #action.double_click(right_arrow).perform()
   # time.sleep(5)
# clicking reports

    driver.find_element(by=By.CSS_SELECTOR, value="a[data-cy='nav-reports']").click()


    driver.find_element(by=By.LINK_TEXT, value='a#mat-tab-link-19').click()


driver.close()

browse("firefox")



