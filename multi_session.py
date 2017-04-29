#!/usr/bin/env python3
import logging, threading, time,json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils import *
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support import expected_conditions as EC
from config import user_config

class Festivus():
    def __init__(self):
        self.opened_sessions = []

    def start_session(self, url, browser):
        while True:
            time.sleep(user_config.queue_wait_time)

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
                        site_key = soup.find('div', {'class', 'g-recaptcha'})['data-sitekey']
                        print("SITE KEY: {}".format(site_key))
                        if user_config.isheadless:
                            self.transfer_session(browser)
                        else:
                            self.browser_placement(browser)
                            pass
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

        chrome_options = get_chrome(browser['user_agent'])
        chrome = webdriver.Chrome(executable_path=find_path('chromedriver'), chrome_options=chrome_options)

        driver.get("http://www.google.com/404page");
        # Transfer Cookies
        chrome.delete_all_cookies()
        chrome.implicitly_wait(3)
        for cookie in driver.get_cookies():

            url = ''
            new_cookie = cookie.copy()
            '''
            if cookie['secure']:
                url += 'https://'
            else:
                url += 'http://'
            '''
            if cookie['domain'].startswith('.'):
                url += 'www'

            if 'hmac' in cookie:
                logging.info("\nHMAC FOUND\n")

            url += cookie['domain']
            new_cookie['domain'] = url
            print(new_cookie['domain'])

            chrome.add_cookie(cookie)

        # Close the headless browser we don't need it anymore
        #driver.close()
        # open URL
        chrome.implicitly_wait(5)
        if user_config.use_gmail:
            chrome.get('https://www.gmail.com')
            chrome.implicitly_wait(10)
            element = WebDriverWait(chrome, 1000).until(EC.title_contains(user_config.gmail_user))

        if user_config.solemartyr:
            chrome.get(user_config.stripes_url)

        else:
            chrome.get(user_config.adidas_site)
            logging.info("\nSession {} TRANSFERRED: Add To Cart NOW\n")

        time.sleep(10000)

    def browser_placement(self, browser):
        driver = browser['browser']
        driver.set_window_position(0, 0)
        if user_config.use_gmail:
            driver.get('https://www.gmail.com')
            driver.implicitly_wait(10)
            element = WebDriverWait(driver, 1000).until(EC.title_contains(user_config.gmail_user))

        if user_config.solemartyr:
            driver.get(user_config.stripes_url)

        else:
            driver.get(user_config.adidas_site)
            logging.info("\nSession {} TRANSFERRED: Add To Cart NOW\n")

    def run_festivus(self, url, browsers):
        for browser in browsers:
            threading.Thread(target=self.start_session, kwargs={'url': url, 'browser': browser}).start()
