#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   webscraper.py
@Author  :   Billy Zhou
@Time    :   2021/08/06
@Version :   1.0.1
@Desc    :   None
'''


import sys
import logging
from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))

from selenium import webdriver  # noqa: E402
from selenium.webdriver.chrome.options import Options  # noqa: E402
# chromedriver: https://chromedriver.chromium.org/downloads

from src.manager.ConfManager import conf  # noqa: E402
logging.info(conf.conf_dict)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        # filename=os.path.basename(__file__) + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log',
        # filemode='a',
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('start DEBUG')
    logging.debug('==========================================================')

    # run the selenium driver
    chrome_opts = Options()

    # two diff ways to capture network traffic by mitmproxy
    # connect to existing chrome on debug mode
    # chrome_opts.add_experimental_option('debuggerAddress', "127.0.0.1:9222")

    # start a new chromedriver
    chrome_opts.add_argument("--user-data-dir=" + conf.conf_dict['chrome']['user-data-dir'])
    chrome_opts.add_argument('--ignore-certificate-errors')
    chrome_opts.add_argument('--ignore-ssl-errors')
    chrome_opts.add_experimental_option('excludeSwitches', ['enable-automation', 'load-extension'])  # don't show the bar of automation

    # set proxy in SwitchyOmega extension or add argument for network traffic capturing
    # chrome_opts.add_argument('--proxy-server=127.0.0.1:8080')

    driver = webdriver.Chrome(executable_path=conf.conf_dict['path']['driver'], options=chrome_opts)

    url = conf.conf_dict['scrapy']['base-url']
    driver.get(url)
    print(driver.title)

    a = input('Wait for inputing.\n')

    driver.quit()

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
