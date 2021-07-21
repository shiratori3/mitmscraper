#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   webscraper.py
@Author  :   Billy Zhou
@Time    :   2021/07/21
@Version :   0.1.0
@Desc    :   None
'''


import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chromedriver: https://chromedriver.chromium.org/downloads


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
    chrome_opts.add_argument("--user-data-dir=" + r"D:\pycharm\mitmscraper\chrome_files")
    chrome_opts.add_argument('--ignore-certificate-errors')
    chrome_opts.add_argument('--ignore-ssl-errors')
    chrome_opts.add_experimental_option('excludeSwitches', ['enable-automation', 'load-extension'])  # don't show the bar of automation

    # set proxy in SwitchyOmega extension or add argument for network traffic capturing
    # chrome_opts.add_argument('--proxy-server=127.0.0.1:8080')

    driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_opts)

    url = "https://www.google.com/"
    driver.get(url)
    print(driver.title)

    a = input('Wait for inputing.\n')

    driver.quit()

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
