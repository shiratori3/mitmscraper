#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   webdriver.py
@Author  :   Billy Zhou
@Time    :   2021/08/07
@Version :   0.0.0
@Desc    :   None
'''


import sys
import logging
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))


from selenium import webdriver  # noqa: E402
from selenium.webdriver.chrome.options import Options  # noqa: E402
# chromedriver: https://chromedriver.chromium.org/downloads

from src.manager.ConfManager import conf  # noqa: E402


class Driver(object):
    def __init__(self, connect_existing=False, existing_port='9222'):
        # run the selenium driver
        chrome_opts = Options()

        # two diff ways to capture network traffic by mitmproxy
        if connect_existing and existing_port:
            # connect to existing chrome on debug mode
            chrome_opts.add_experimental_option('debuggerAddress', "127.0.0.1:" + str(existing_port))
        else:
            # start a new chromedriver
            chrome_opts.add_argument("--user-data-dir=" + conf.conf_dict['chrome']['user-data-dir'])
            chrome_opts.add_argument('--ignore-certificate-errors')
            chrome_opts.add_argument('--ignore-ssl-errors')
            chrome_opts.add_experimental_option('excludeSwitches', ['enable-automation', 'load-extension'])  # don't show the bar of automation

            # set proxy in SwitchyOmega extension or add argument for network traffic capturing
            # chrome_opts.add_argument('--proxy-server=127.0.0.1:8080')

        self.driver = webdriver.Chrome(executable_path=conf.conf_dict['path']['driver'], options=chrome_opts)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        # filename=os.path.basename(__file__) + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log',
        # filemode='a',
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('start DEBUG')
    logging.debug('==========================================================')

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
