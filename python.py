from selenium import webdriver
from selenium.webdriver.chrome.options import Options



driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe') 

driver.get("https://www.google.com")

element=driver.find_element("xpath", '//*[@id="APjFqb"]')


element.send_keys("BMS College of Engineering")
element.submit()

while(True):
    pass
