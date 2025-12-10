"""User Acceptance Tests using Selenium."""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUAT:
    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    def test_add_food_functionality(self, driver):
        driver.get("http://localhost:8000")
        
        # Add food item
        food_input = driver.find_element(By.NAME, "food")
        calories_input = driver.find_element(By.NAME, "calories")
        
        food_input.send_keys("Apple")
        calories_input.send_keys("100")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Verify food appears
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "meal"))
        )
        assert "Apple: 100 calories" in driver.page_source
        assert "Total: 100 calories" in driver.page_source

    def test_reset_functionality(self, driver):
        driver.get("http://localhost:8000")
        
        # Add food first
        driver.find_element(By.NAME, "food").send_keys("Banana")
        driver.find_element(By.NAME, "calories").send_keys("200")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(1)
        
        # Reset
        driver.find_element(By.XPATH, "//button[contains(text(), 'Reset')]").click()
        driver.switch_to.alert.accept()
        
        # Verify reset
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "Total: 0 calories")
        )
        assert "Total: 0 calories" in driver.page_source