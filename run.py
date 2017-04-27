#!/usr/bin/env python3
import sys, logging
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from multi_session import Festivus
from utils import *

version = '0.1'
# PRODUCT_URL = 'http://www.adidas.com/yeezy'
PRODUCT_URL = 'http://adidas.bot.nu/yeezy'
# PRODUCT_URL = 'http://www.adidas.com/us/alphabounce-reigning-champ-shoes/CG4301.html'

if sys.version_info <= (3, 0):
    sys.stdout.write("Could not start: requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    print("\nAdidas Waiting Room Festivus (V{}) by joshgenao (BETA) special thanks to yzy.io ".format(version))

    # Create drivers
    faceless_browsers = []

    total_headless_browsers = 3

    for i in range(total_headless_browsers):
        try:
            # Get user agent
            user_agent = get_user_agent()
            chrome_options = get_headless_chrome(user_agent=user_agent)
            browser = webdriver.Chrome(executable_path=find_path('chromedriver'), chrome_options=chrome_options)
            #browser.set_window_size(0,0)
            browser.get(PRODUCT_URL)

            if ('you have been blocked' in browser.page_source.lower()) or ('a security issue was automatically identified' in browser.page_source.lower()):
                logging.error('[{}/{}] Banned on {}'.format(i + 1, total_headless_browsers, PRODUCT_URL))
                continue

            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "div")))
            if not element:
                logging.error('[{}/{}] Browser could not load URL: {}'.format(i + 1, total_headless_browsers, PRODUCT_URL))

            logging.info('[{}/{}] Browser Test Success'.format(i + 1, total_headless_browsers))

            faceless_browsers.append({
                'browser': browser,
                'user_agent': user_agent
            })

        except Exception as e:
            logging.error('[{}/{}] {}'.format(i + 1, total_headless_browsers, e))
            continue

    if len(faceless_browsers) > 0:
        print("\nWorking Headless Browsers: {} - starting script..".format(len(faceless_browsers)))
        george_costanza = Festivus()
        george_costanza.run_festivus(PRODUCT_URL, faceless_browsers)
    else:
        print("\nNo working browsers found.")