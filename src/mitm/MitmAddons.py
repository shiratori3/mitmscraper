#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MitmAddons.py
@Author  :   Billy Zhou
@Time    :   2021/08/06
@Version :   1.0.1
@Desc    :   None
'''


import sys
import logging
import hashlib
import json
import cgi
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))

from urllib.parse import urlparse  # noqa: E402
from mitmproxy import ctx, http  # noqa: E402
from mitmproxy import flowfilter  # noqa: E402
from src.manager.ConfManager import conf  # noqa: E402


class file_scrape:
    def __init__(self):
        self.request_num = 0
        self.response_num = 0
        self.basepath = Path(conf.conf_dict['path']['scrape_files'])
        self.dictpath = self.basepath.joinpath("scrape_files.json")
        self.scrape_dict = {}
        if self.dictpath.exists():
            with open(str(self.dictpath), encoding='utf-8') as json_f:
                self.scrape_dict = json.load(json_f)
        self.filter = conf.conf_dict['scrapy']['domain']

    def request(self, flow: http.HTTPFlow) -> None:
        if self.filter in flow.request.pretty_url:
            self.request_num += 1
            # ctx.log.info('request count: {0}'.format(self.request_num))

    def response(self, flow: http.HTTPFlow) -> None:
        domain = urlparse(flow.request.pretty_url).netloc
        ctx.log.info("get response of request {0}.".format(flow.request.pretty_url))
        if self.filter in domain:
            if not self.scrape_dict.get(domain):
                self.scrape_dict[domain] = {}

            self.response_num += 1
            # ctx.log.info('response count: {0}'.format(self.response_num))
            # ctx.log.info('request url: {0}'.format(flow.request.pretty_url))
            ctx.log.info('response headers: \n{0}'.format(flow.response.headers))
            # ctx.log.info('response content: \n\n{0}\n\n'.format(flow.response.content[:100]))

            # decode content
            url_content = flow.response.content
            if "content-type" in flow.response.headers:
                _, content_params = cgi.parse_header(flow.response.headers["content-type"])
            ctx.log.info("content_params: {0}".format(content_params))
            if 'charset' not in content_params:
                url_content_decoded = url_content.decode('utf-8')
            else:
                url_content_decoded = url_content.decode(content_params['charset'])

            # get filepath with the md5 filename of flow.response.content
            filehash = hashlib.md5(url_content).hexdigest()
            # ctx.log.info(filehash)
            domain_filepath = self.basepath.joinpath(domain)
            if not domain_filepath.exists():
                domain_filepath.mkdir(parents=True)
            filepath = domain_filepath.joinpath(domain + "_" + str(filehash) + ".txt")

            with open(str(filepath), 'w', encoding='utf-8') as f:
                f.write(url_content_decoded)
                self.scrape_dict[domain][filehash] = flow.request.pretty_url

            with open(str(self.dictpath), 'w', encoding='utf-8') as json_f:
                json.dump(self.scrape_dict, json_f)


my_addons = [
    file_scrape()
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
