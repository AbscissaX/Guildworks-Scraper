#Guildwork_Scraper
import requests
from bs4 import BeautifulSoup
import re
import datetime
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GuildworkScraper:

    lodestone_domain = 'na.finalfantasyxiv.com'
    lodestone_url = 'http://%s/lodestone/' % lodestone_domain
    guildwork_domain = 'ascendedfc.guildwork.com'
    guildwork_url = 'http://%s/recruitment' % guildwork_domain
    guildwork_login = 'https://%s/login' % guildwork_domain
    bot_email = 'ccb8511f@opayq.com'
    bot_password = 'bjpH97rkanmJ'

    '''
    Returns a dictionary to represent Members join date using Chrome.
    
    It's cool to see in action, but want to try to use something that
    will hide the browser.
    '''
    def get_member_apps_chrome(self):

        #Load webdriver using chrome - might want to make a new function to try out PhantomJS again
        chromedriver = '.\\ChromeDriver\\chromedriver.exe'
        browser = webdriver.Chrome(chromedriver)

        # Go to the Login page and insert creditials
        browser.get(self.guildwork_login)
        username = browser.find_element_by_id("id_email")
        password = browser.find_element_by_id("id_password")

        username.send_keys(self.bot_email)
        password.send_keys(self.bot_password)

        #Find the Login Button by using it's xpath, then simulate clicking submit
        browser.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()

        #Go to recruitment page, and get the source of the table of apps
        browser.get(self.guildwork_url)
        source = browser.find_element_by_id("applications").get_attribute('innerHTML')

        #make a soup for the app table
        soup = BeautifulSoup(source, "lxml")

        #Close browser
        browser.quit()
      
#Test Area
test = GuildworkScraper()
print (test.guildwork_login)
test.get_member_apps_chrome()
