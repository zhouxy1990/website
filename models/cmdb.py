# -*- coding:utf-8 -*-
# CREATE BY Zhou Xiangyu
from tools import DBUtil
from flask import current_app
DBNAME = "CMDB"
CONN = DBUtil.MysqlConn(DBNAME)
import yaml

def loadYaml():
    with open(current_app.config.get("SQL_FILE_PATH"),'r') as f :
        loadFile = yaml.load(f)
    return loadFile


def getSchemaInfo ():

    sql =loadYaml().get("getSchemaInfo")
    result = CONN.getAll(sql)
    return result

def getDetailBySchemaId(schema_id):

    sqlStr=loadYaml().get("getDetailBySchemaId")
    value=getDetail(schema_id)
    sql = sqlStr % (value,schema_id)
    result = CONN.getAll(sql)
    #print(result)
    return result

'''
def getDetail(schema_id):
    getField = loadYaml().get("getFieldName")
    field = CONN.getAll(getField,param=(schema_id))
    sqlHead = loadYaml().get("sqlForQuery")
    sqlBody = loadYaml().get("getDetail")
    sqlTail = loadYaml().get("sqlConditions")
    sqlHeadre = map(lambda x : sqlHead.format(x.get("name"),x.get("name")),field)
    sqlBodyre = map(lambda x : sqlBody.format(schema_id,x.get("name"),x.get("name")),field)
    sqlTailre = map(lambda x : sqlTail.format(x.get("name")),field)
    querys = ",".join(sqlHeadre)
    bodys = ",".join(sqlBodyre)
    condtions = "=".join(sqlTailre)
    sql = 'select ' + querys +' from ' +bodys +' where ' +condtions
    return sql
'''

def getDetail(schema_id):

    getField = loadYaml().get("getFieldName")
    field = CONN.getAll(getField, param=(schema_id))
    if not field :
        raise ValueError()
    queryValue = loadYaml().get("sqlForQueryValue")
    queryValueList = map(lambda x: queryValue % (x.get("name"), x.get("name")), field)
    queryValueStr = ",".join(queryValueList)
    return queryValueStr