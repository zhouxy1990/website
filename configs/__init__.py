# -*- coding:utf-8 -*-
import os
class BaseConfig(object):
    #项目根目录
    BASE_PATH = os.path.dirname( os.path.dirname( os.path.realpath( __file__ ) ) )


