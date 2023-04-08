from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec

class Test_Sauce:
    
    # def initializeDriver(self):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get("https://www.saucedemo.com/") 


    def test_invalid_login(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(1)
        userNameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(1)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(3)
        errorMessage = self.driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Hatalı Giriş..."
        print(f"test sonucu : {testResult}")

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(
        ec.visibility_of_element_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(
        ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(3)

        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
       
        sleep(1)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(20)


testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()
