#!/usr/bin/env python3
from configparser import ConfigParser
import os

c = ConfigParser()
# Get the project directory to avoid using relative paths
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
configFilePath = os.path.join(PROJECT_ROOT_DIR, 'config.ini')
c.read('config.ini')

class Config:
    # Is it headless?
    isheadless = c.getboolean('browser', 'headless')
    # What is the adidas site
    adidas_site = c.get('browser', 'adidas_url')
    # How many browsers am I loading up
    browser_amount = c.getint('browser', 'size')
    # How long should I wait to be in the queue?
    queue_wait_time = c.getint('browser', 'wait_time')
    # Use GMAIL?
    use_gmail = c.getboolean('gmail', 'use_gmail')
    # Email username
    gmail_user = c.get('gmail', 'username')
    # Using the SoleMartyr Script?
    solemartyr = c.getboolean('SoleiusMartyrium', 'solemartyr')
    # Whats the site for ///
    stripes_url = c.get('SoleiusMartyrium', 'stripes_url')

    def __init__(self):
        pass

    def print_config(self):
        '''
        Print out my config just in case if I messed up somewhere
        '''
        print("Headless: {}".format(self.isheadless))
        print("Adidas URL: {}".format(self.adidas_site))
        print("Amount of Browsers: {}".format(self.browser_amount))
        print("Queue Time: {}".format(self.queue_wait_time))
        print()
        print("GMAIL")
        print("Solemartyr: {}".format(self.solemartyr))
        print("/// url: {}".format(self.stripes_url))

# This is our config instance.
user_config = Config()