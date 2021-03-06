#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-09-25 21:11:15
@LastEditTime: 2019-12-13 16:36:16
'''

import pymssql
from concurrent.futures import ThreadPoolExecutor

class MsSQLBruteForce(object):
    """MsSQLBruteForce"""
    def __init__(self, targets, thread_num, timeout):
        super(MsSQLBruteForce, self).__init__()
        self.targets = targets
        self.thread_num = thread_num
        self.timeout = timeout

    def worker(self,hpup):
        host,port,user,pwd = hpup
        try:
            conn = pymssql.connect(host=host,port=port,user=user,password=pwd,
                                database="master",timeout=self.timeout,charset="utf8")
        except Exception as e:
            hook_msg((False,host,port,user,pwd))
            # logger.error(str(e))
        else:
            hook_msg((True,host,port,user,pwd))
        finally:
            conn.close()

    def run(self):
        with ThreadPoolExecutor(max_workers = self.thread_num) as executor:
            for host,port,user,pwd in self.targets:
                f = executor.submit(self.worker,(host,port,user,pwd))
                # f.add_done_callback(call_back)

bruter = MsSQLBruteForce

