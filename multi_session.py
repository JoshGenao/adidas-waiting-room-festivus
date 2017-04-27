#!/usr/bin/env python3
import logging, threading, time,json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from utils import write_cookies_to_file, find_path
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Festivus():
    def __init__(self):
        self.opened_sessions = []

    def start_session(self, url, browser):
        while True:
            time.sleep(20)

            if browser['browser'].session_id not in self.opened_sessions:
                logging.info("Checking if session {} is past splash".format(browser['browser'].session_id))

                try:
                    html = browser['browser'].page_source
                    soup = bs(html, 'html.parser')
                    captcha = soup.find_all('div', {'class', 'g-recaptcha'})
                    # If g-recaptcha is found, then append the driver to opened_session
                    if captcha is not None and len(captcha) > 0:
                        #print(soup.prettify())
                        self.opened_sessions.append(browser['browser'])
                        logging.info("Session {} OPENED: Cookie:\n{}\n".format(browser['browser'].session_id, json.dumps(browser['browser'].get_cookies())))
                        # TODO: Print out clientID and Site-key
                        #browser['browser'].set_window_size(1200,600)
                        self.transfer_session(browser)
                        break
                except Exception as e:
                    # Delete the cookies and try again. Many people thinks this a useful technique
                    logging.error("Error in start_session with id {}. Exception: {} ".format(browser['browser'].session_id, e))

                browser['browser'].delete_all_cookies()
                browser['browser'].refresh()

    def transfer_session(self, browser):
        driver = browser['browser']
        logging.info("Transferring session {}".format(driver.session_id))

        # Save the cookies to file
        write_cookies_to_file(driver.get_cookies())

        url = driver.current_url
        chrome_options = Options()
        chrome_options.add_argument("user-agent={}".format(browser['user_agent']))
        chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        chrome_options.add_argument('window-size=1200x600')
        chrome_options.add_argument('disable-infobars')
        chrome = webdriver.Chrome(executable_path=find_path('chromedriver'), chrome_options=chrome_options)

        # open URL
        chrome.get(url)
        chrome.implicitly_wait(20)
        print("Pass implicit wait...")
        element = WebDriverWait(chrome, 1000).until(EC.presence_of_element_located((By.TAG_NAME, "div")))

        # Transfer Cookies
        chrome.delete_all_cookies()
        print(type(driver.get_cookies()))
        for cookie in driver.get_cookies():
            new_cookie = {}
            new_cookie['name'] = cookie['name']
            #print("Cookie Name: {}".format(cookie['name']))
            new_cookie['value'] = cookie['value']
            #print("Cookie Value: {}".format(cookie['value']))
            chrome.add_cookie(new_cookie)

        # Close the headless browser we don't need it anymore
        driver.close()
        chrome.refresh()
        logging.info("\nSession {} TRANSFERRED: Add To Cart NOW\n{}".format(browser['browser'].session_id))
        time.sleep(10000)

    def cookie_transform(self, cookies):
        url = ""
        #for cookie in cookies:


    def run_festivus(self, url, browsers):
        for browser in browsers:
            threading.Thread(target=self.start_session, kwargs={'url': url, 'browser': browser}).start()
