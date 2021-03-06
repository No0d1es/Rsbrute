#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-09-25 21:11:15
@LastEditTime: 2019-10-18 11:30:25
'''

from subprocess import Popen, PIPE, STDOUT
from concurrent.futures import ThreadPoolExecutor

class RdpBruteForce(object):
    """RdpBruteForce"""
    def __init__(self, targets, thread_num, timeout):
        super(RdpBruteForce, self).__init__()
        self.targets = targets
        self.thread_num = thread_num
        self.timeout = timeout
        self.result = list()
        print("RdpBruteForce...")

    def worker(self,hpup):
        host,port,user,pwd = hpup
        try:
            command = "xfreerdp /sec:nla /p:{} /u:{} /port:{} /v:{} /cert-ignore "
            p = Popen(command, shell=True)
            p.communicate()
        except Exception as e:
            logger.error(str(e))
        else:
            logger.info("[OK] {} {} {} {}".format(host, port, user, pwd))
            self.result.append((host, port, user, pwd))
        finally:
            conn.close()

    def run(self):
        logger.info("Module RdpBruteForce is Developing...")
        # ip_list = [x[0] for x in self.result]
        # with ThreadPoolExecutor(max_workers = self.thread_num) as executor:
        #     for host,port,user,pwd in self.targets:
        #         f = executor.submit(self.worker,(host,port,user,pwd))
                # f.add_done_callback(call_back)

bruter = RdpBruteForce
