# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 17:39 
# @Author : ZHH
import logging
import time
from Common.config import logs_dir

class Log:
   def __init__(self):
       curTime = time.strftime('%Y-%m-%d')
       self.logname = logs_dir + '\\' + 'AutoTestLog-' + curTime + '.log'
       # self.logname = os.path.join(log_path,'{0}.log'.format(time.strftime('%Y-%m-%d')))
   def getlogger(self,level,msg):

        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出日志到文件
        fh = logging.FileHandler(self.logname,'a',encoding='gbk')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出日志到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录日志
        if level == 'info':
            logger.info(msg)
        elif level == 'debug':
            logger.debug(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        logger.removeHandler(fh)
        logger.removeHandler(ch)

        # 关闭日志文件
        fh.close()
   def log_debug(self,msg):
        self.getlogger('debug',msg)

   def log_info(self,msg):
        self.getlogger('info',msg)

   def log_warning(self,msg):
        self.getlogger('warning',msg)

   def log_error(self,msg):
        self.getlogger('error',msg)

   def exception(self, param):
       pass