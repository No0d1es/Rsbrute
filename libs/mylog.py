#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-07-16 22:31:00
@LastEditTime: 2019-12-13 15:54:57
'''

import logging
import colorlog

class MyLog(object):
    def __init__(self, loglevel, logger_name, logfile=None):
        # 创建一个 logger
        self.logger = colorlog.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        #设置日志输出等级，后面创建 Handler 然后 setLevel(logging.DEBUG) 也不能输出 WARNING 等级之下的日志
        # self.logger.setLevel(logging.WARNING)

        # 创建 stream hander
        sh = self.__stream_hander(loglevel)
        self.logger.addHandler(sh)

        # 创建 file hander
        if logfile:
            fh = self.__file_hander(logfile)
            self.logger.addHandler(fh)

    def __file_hander(self, logfile):
        # 创建一个用于写入日志文件的 handler
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.DEBUG) # 只要是写入文件的等级都为DEBUG，也可以设置为loglevel
        # formatterf = logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s] %(message)s')
        formatterf = logging.Formatter('%(asctime)s [%(name)s] %(message)s')
        fh.setFormatter(formatterf)
        return fh

    def __stream_hander(self, loglevel):
        # 创建一个用于输出到控制台的 handler
        sh = colorlog.StreamHandler()
        sh.setLevel(loglevel)
        formatter = colorlog.ColoredFormatter(
            # '%(log_color)s[%(asctime)s] [%(levelname)s] %(message)s %(reset)s',
            '%(log_color)s[%(asctime)s] %(message)s %(reset)s',
            datefmt="%H:%M:%S",
            reset=True,
            log_colors={
                'CRITICAL': 'white,bg_red',
                'ERROR': 'red',
                'WARNING': 'yellow',
                'INFO': 'green',
                'DEBUG': 'blue',
            },
            secondary_log_colors={},
            style='%'
        )
        sh.setFormatter(formatter)
        return sh

    def critical(self,msg):
        self.logger.critical(msg)

    def error(self,msg):
        self.logger.error(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def info(self,msg):
        self.logger.info(msg)

    def debug(self,msg):
        self.logger.debug(msg)


if __name__ == '__main__':
    # 等级为 INFO 则只会输出级别大于等于 INFO 的日志
    # DEBUG < INFO < WARNING < ERROR < CRITICAL

    logger = MyLog(loglevel='NOTSET', logger_name='test', logfile='log.txt')
    logger.critical('critical')
    logger.error('error')
    logger.warning('warning')
    logger.info('info')
    logger.debug('debug')
