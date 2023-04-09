from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException,NoSuchWindowException
import random

try:
    
    def play():
        x=random.randint(5000,2000000000)
        i = x%46 + 3
        search9=driver.find_element(By.XPATH,"//div[@aria-rowindex="+ str(i) +"]")
        action = ActionChains(driver)
        action.move_to_element(search9)
        action.move_by_offset(50, 10)
        action.double_click()
        action.perform()
        time.sleep(1)  
    def shuffle():
        search3=driver.find_element(By.XPATH,'//button[@class="_39234eb5c173f8b6de80ed73820b1be8-scss"]')
        if search3.is_displayed():
            search3.click()
        
    def start():
    	search3=driver.find_element(By.XPATH,'//button[@data-testid="control-button-play"]')
    	if search3.is_displayed():
        	search3.click()

    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")   
    driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2Fplaylist%2F37i9dQZF1DZ06evO3nMr04")
    driver.find_element(By.XPATH,'//input[@id="login-username"]').send_keys("youremail")
    search1=driver.find_element(By.XPATH,'//input[@id="login-password"]') 
    search1.send_keys("yourpassword")
    search1.send_keys(Keys.RETURN)
    b=1
    i=1

    time.sleep(1.)
    while True:
    	try:
    		play()
    		break
    	except:
    		pass

    time.sleep(1)
    try:
    	shuffle()
    except:
    	pass
    driver.set_window_size(650,750)
    while(b>=0):
        a=0
        while True:
            try:
                search5=driver.find_element(By.XPATH,"//a[text()='Advertisement']")
                a=1
                break
            except NoSuchElementException:
                try:
                    search7=driver.find_element(By.XPATH,"//a[text()='Spotify']")
                    a=1
                    break
                except NoSuchElementException:
                    pass     
                except:
                    b=-1
                    break
            except:
                b=-1
                break
        if(b<0):
            break
        if (a == 1):
            try:
                driver.refresh()              
                while True:
                    try:
                        play()
                        time.sleep(1)
                        shuffle()
                        break
                    except NoSuchElementException:
                        pass
            except:
                b=-1
                break
except NoSuchWindowException:
    pass

driver.quit()
