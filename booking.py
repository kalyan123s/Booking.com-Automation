import os
import time

from selenium.webdriver.chrome.options import Options
import booking.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driverPath="D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

#this three lines are used for preventing automatically quit the chrome
browserOptions = webdriver.ChromeOptions()                                   
browserOptions.add_experimental_option('detach', True)                               
browserOptions.add_experimental_option('excludeSwitches', ['enable-logging'])       

#service=chromeService specifies that we want to use the custom ChromeDriver service whose path is in driver path
#inside the bracket we have to necessarily give argument as browser option so that chrome don't quit automatically
browser=webdriver.Chrome(service=Service(driverPath), options = browserOptions)    


class Booking(webdriver.Chrome):
    def __init__(self, driverpath="D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"):
        self.driverpath=driverpath
        # os.environ['PATH'] +=self.driverpath
        # super(Booking, self).__init__()
        
    #open booking.com website
    def land_homepage(self): 
        browser.maximize_window()
        browser.get(const.base_url)
        print('landpage calling')
        
    try:
      def remove_signin_popup(self):
        browser.implicitly_wait(20)
        popup_signin = browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        time.sleep(1.5)
        popup_signin.click()
        print('signin-popup calling')
    except:
        pass
        
       
    # currency selection
    def change_currency(self): 
        # browser.implicitly_wait(15)
        btn_currency=browser.find_element(By.CSS_SELECTOR, "button[data-testid='header-currency-picker-trigger']")
        time.sleep(1)
        btn_currency.click()
        print('change_currency calling')
        selected_currency=browser.find_element(By.CSS_SELECTOR, "button[data-testid='selection-item']")
        time.sleep(1)
        selected_currency.click()
            
     # Destination selection
    def destination(self): 
        search_destination=browser.find_element(By.CSS_SELECTOR, "input[id=':re:']")
        #clears the destination
        browser.implicitly_wait(10)
        search_destination.clear()
        search_destination.send_keys('Ayodhya')
        first_place=browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/ul/li[1]/div/div")
        time.sleep(3)
        first_place.click()
        print('destination calling')
    
    try:
        # Check in Check out date selection
        def checkin_checkout(self):
            time.sleep(3)
            checkin_checkout_box=browser.find_element(By.CSS_SELECTOR, "button[data-testid='date-display-field-start']")
            # browser.implicitly_wait(4)
            # checkin_checkout_box.click()
        
            time.sleep(1.3)
            checkin=browser.find_element(By.CSS_SELECTOR, "span[aria-label='11 October 2023']")
            browser.implicitly_wait(5)
            checkin.click()
        
            time.sleep(1)
            checkout=browser.find_element(By.CSS_SELECTOR, "span[aria-label='14 October 2023']")
            browser.implicitly_wait(5)
            checkout.click()
            print('checkin_checkout calling')
            time.sleep(1.2)   
    except:
        pass

    #no of people and room selection
    def no_0f_people_room(self):
        people_room_box=browser.find_element(By.CSS_SELECTOR, "button[data-testid='occupancy-config']")
        browser.implicitly_wait(5)
        people_room_box.click()
        
        ###$$$$$no of adults wanna checkin
        while True:
            # first decrease no of adults to one
            decrease_adults=browser.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]")
            time.sleep(0.5)
            decrease_adults.click()
            # if the no of adult become 1 then we should get out of this while loop
            adults_checkin=browser.find_element(By.ID, "group_adults")
            #this line gives n of adults
            adults_value=adults_checkin.get_attribute('value')
            if int(adults_value)==1:
                break
            
        adults_checkin=browser.find_element(By.ID, "group_adults")
        #this line gives no of adults
        adults_value=adults_checkin.get_attribute('value')
        adults_value=10
        for _ in range(int(adults_value)-1):           #this "-" shows we are not going to use that variable in for loop
            increase_adults=browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]")
            time.sleep(0.6)
            increase_adults.click()
        
        
  # @@@@@@Note I am commenting this code since i wanted to put children as zero  
        # ###$$$$$no of children wanna checkin
        # while True:
        #     # first decrease no of adults to 0
        #     decrease_children=browser.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[2]/div[2]/button[1]")
        #     browser.implicitly_wait(5)
        #     decrease_children.click()
        #     # if the no of adult become 1 then we should get out of this while loop
        #     children_checkin=browser.find_element(By.ID, "group_children")
        #     #this line gives n of adults
        #     children_value=children_checkin.get_attribute('value')
        #     if int(children_value)==0:
        #         break
         
            
        no_of_room=browser.find_element(By.ID, "no_rooms")
        #this line gives no of adults
        room_value=no_of_room.get_attribute('value')
        room_value=4
        for _ in range(room_value-1):           #this "-" shows we are not going to use that variable in for loop
            increase_room=browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[3]/div[2]/button[2]")
            time.sleep(.5)
            increase_room.click()  
        # children=browser.find_element(By.CSS_SELECTOR,"")
        # browser.implicitly_wait(5)
        # children.click()
        
        time.sleep(2)
        done_button=browser.find_element(By.CSS_SELECTOR, "button[type='button'][class*='a83ed08757'][class*='c21c56c305'][class*='bf0537ecb5'][class*='ab98298258'][class*='d2529514af'][class*='af7297d90d'][class*='c213355c26'] > span.e4adce92df")
        browser.implicitly_wait(5)
        done_button.click()
        
        print('no_of_people_room calling')
        
    def search_button(self):
        search=browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/form/div[1]/div[4]/button")
        browser.implicitly_wait(4)
        search.click()
        print('search_button calling')
    # def __exit__(self,exc_type, exc_val, exc_tb):
    #     driver.quit()
  

# time.sleep(20)