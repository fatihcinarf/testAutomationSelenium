from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path
from datetime import date
# prefix => Ön Ek test_
# postfix


class Test_DemoClass:
    # her testten önce çağırılır...
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur

    # her testten sonra çağırılır...

    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        # 3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"

    def test_demo2(self):
        assert True

    # @pytest.mark.skip() #ilgili fonksiyonu çalıştırma...
    @pytest.mark.parametrize("username,password", [("1", "1"), ("kullanıcıadim", "sifrem")])
    def test_invalid_login(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(
            f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

    