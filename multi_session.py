#!/usr/bin/env python3
import logging, threading
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Festivus():

    def __init__(self):
        self.opened_sessions = []

    def start(self, url, browser):
        while True:
            if browser['browser'].session_id not in self.opened_sessions:
                logging.info("Checking if session {} is past splash".format(browser['browser'].session_id))

                try :
                    captcha = WebDriverWait(browser['browser'], 15).until(lambda l : browser['browser'].find_element_by_class_name('g-recaptcha'))

                    # If g-recaptcha is found, then append the driver to opened_session
                    if captcha:
                        self.opened_sessions.append(browser['browser'])
                        threading.Thread(target=self.transfer_session, kwargs={ 'browser' : browser }).start()
                except:
                    # Delete the cookies and try again. Many people thinks this a useful technique
                    browser['browser'].delete_all_cookies()
                    browser['browser'].refresh()

    def transfer_session(self):
        pass
