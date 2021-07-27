#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MitmProxifier.py
@Author  :   Billy Zhou
@Time    :   2021/07/20
@Version :   1.0.0
@Desc    :   None
'''


import logging
import threading
import asyncio
from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.tools.web.master import WebMaster
from MitmAddons import my_addons


class MitmProxifier(object):
    def __init__(self):
        self.thread = None

    def loop_in_thread(self, loop, m):
        asyncio.set_event_loop(loop)
        self.m.run()

    def start(self, addons, web_client=False):
        # set the mitmproxy config
        mitm_opts = options.Options(
            listen_host='127.0.0.1', listen_port=8080, mode='upstream:http://127.0.0.1:7890')
        # mitmdump --mode upstream:http://127.0.0.1:7890
        pconf = proxy.config.ProxyConfig(mitm_opts)

        if web_client:
            self.m = WebMaster(mitm_opts)
        else:
            self.m = DumpMaster(mitm_opts, with_termlog=False, with_dumper=True)
        self.m.server = proxy.server.ProxyServer(pconf)
        for addon in addons:
            self.m.addons.add(addon)
        # print(self.m.addons)

        # create thread
        loop = asyncio.get_event_loop()
        self.thread = threading.Thread(
            target=self.loop_in_thread, args=(loop, self.m))

        try:
            self.thread.start()
        except KeyboardInterrupt:
            self.m.shutdown()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        # filename=os.path.basename(__file__) + '_' + time.strftime('%Y%m%d', time.localtime()) + '.log',
        # filemode='a',
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logging.debug('start DEBUG')
    logging.debug('==========================================================')

    my_mitmdump = MitmProxifier()
    my_mitmdump.start(my_addons, web_client=True)

    logging.debug('==========================================================')
    logging.debug('end DEBUG')
