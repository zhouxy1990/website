# -*- coding:utf-8 -*-
import os

class BaseConfig(object):
    #项目根目录
    BASE_PATH = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )


class DBConfig(BaseConfig):
    CMDB ={
       "HOST": "127.0.0.1",
        "USER":"root",
        "PASSWORD" : "root1234",
        "DBNAME" : "cmdb",
        "PORT" : 3306,
    }

    SQL_FILE_PATH = os.path.join(BaseConfig.BASE_PATH,"models/sqlConf/cmdb.yaml")
    PAGE_DICT = {
        "1" : "host_detail.html",
        "2" : "switch_detail.html",
    }