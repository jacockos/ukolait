from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5173")
    return driver

def test_homepage_loads():
    driver = setup_driver()
    assert "Think different" in driver.title
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

    # počkáme až se objeví jakýkoliv input
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
    )

    assert search is not None

def test_search_typing():
    driver = setup_driver()

    # najdeme input
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
    )

    # napíšeme text
    search.send_keys("test")

    # ověříme, že se text opravdu zapsal
    assert search.get_attribute("value") == "test"
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
