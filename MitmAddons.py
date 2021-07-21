#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MitmAddons.py
@Author  :   Billy Zhou
@Time    :   2021/07/21
@Version :   0.1.0
@Desc    :   None
'''


import logging


class CountNum:
    def __init__(self):
        self.request_num = 0
        self.response_num = 0
        print('inited')

    def request(self, flow):
        self.request_num += 1
        print('send request. count: {0}'.format(self.request_num))

    def response(self, flow):
        self.response_num += 1
        print('get response. count: {0}'.format(self.response_num))


my_addons = [
    CountNum()
]


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
