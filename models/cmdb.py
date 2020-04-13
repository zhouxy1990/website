# -*- coding:utf-8 -*-
# CREATE BY Zhou Xiangyu
from tools import DBUtil
DBNAME = "CMDB"
CONN = DBUtil.MysqlConn(DBNAME)

def getSchemaInfo ():
    sql = "SELECT `id`,`name`,`desc` FROM `schema`;"
    res = CONN.getAll(sql)
    return res

