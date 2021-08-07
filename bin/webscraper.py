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

from src.manager.ConfManager import conf  # noqa: E402
from src.driver.WebDriver import Driver  # noqa: E402


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        # filename=os.path.basename(__file__) + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log',
        # filemode='a',
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('start DEBUG')
    logging.debug('==========================================================')

    driver = Driver(connect_existing=False, existing_port='9222').driver
 
    url = conf.conf_dict['scrapy']['base-url']
    driver.get(url)
    print(driver.title)

    a = input('Wait for inputing.\n')

    driver.quit()

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
