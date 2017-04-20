#!/usr/bin/env python3
import json, logging
from selenium.webdriver import DesiredCapabilities

def get_desired_capabilities_phantom(user_agent):
    desired_capabilities = dict(DesiredCapabilities.PHANTOMJS)
    desired_capabilities['phantomjs.page.settings.userAgent'] = user_agent
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = user_agent
    desired_capabilities['phantomjs.page.customHeaders.customHeaders'] = \
        {'Accept': 'text/html', 'Content-type': 'text/html', 'Cache-Control': 'max-age=0'}

    return desired_capabilities

def write_cookies_to_file(cookies, file='cookies.txt'):
    try:
        with open(file, 'w') as f:
            f.write(json.dumps(cookies) + "\n")
            f.close()
    except Exception as e:
        logging.error(e)
        return None