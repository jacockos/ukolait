from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def setup_driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5173")
    return driver

def test_homepage_loads():
    driver = setup_driver()
    assert "Tour" in driver.title
    driver.quit()

def test_navigation_menu():
    driver = setup_driver()
    menu = driver.find_element(By.TAG_NAME, "nav")
    assert menu is not None
    driver.quit()

def test_click_first_link():
    driver = setup_driver()
    link = driver.find_element(By.TAG_NAME, "a")
    link.click()
    time.sleep(1)
    assert driver.current_url != "http://localhost:5173"
    driver.quit()

def test_search_bar_exists():
    driver = setup_driver()
    search = driver.find_element(By.TAG_NAME, "input")
    assert search is not None
    driver.quit()

def test_search_typing():
    driver = setup_driver()
    search = driver.find_element(By.TAG_NAME, "input")
    search.send_keys("test")
    assert search.get_attribute("value") == "test"
    driver.quit()

def test_footer_exists():
    driver = setup_driver()
    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer is not None
    driver.quit()

def test_page_scroll():
    driver = setup_driver()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.quit()

def test_multiple_links():
    driver = setup_driver()
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) > 1
    driver.quit()

def test_logo_exists():
    driver = setup_driver()
    logo = driver.find_element(By.TAG_NAME, "img")
    assert logo is not None
    driver.quit()

def test_refresh_page():
    driver = setup_driver()
    driver.refresh()
    time.sleep(1)
    assert True
    driver.quit()
