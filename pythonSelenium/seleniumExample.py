from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

input=driver.find_element(By.NAME,"q")
sleep(3)
input.send_keys("kodlamaio")
searchButton=driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firsResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firsResult.click()
sleep(2)

listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda : {len(listOfCourses)} tane kurs mevcut...")

while True:
    continue


# HTML LOCATORS
# web scraping





# full XPath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a
# XPath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a
