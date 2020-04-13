# -*- coding:utf-8 -*-
# CREATE BY Zhou Xiangyu

import pymysql
from pymysql.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
from flask import current_app


class MysqlConn(object):
    __pool = None
    def __init__(self,db):
        self.DBConfig = current_app.config.get(db)
        self._conn = MysqlConn.__getConn(self)
        self._cursor = self._conn.cursor()



    @staticmethod
    def __getConn(self):
        '''
        静态方法，从连接池中取出连接
        :param self:
        :return:
        '''
        if MysqlConn.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                              host=self.DBConfig.get("HOST"),
                              port=self.DBConfig.get("PORT"),
                              user=self.DBConfig.get("USER"),
                              passwd=self.DBConfig.get("PASSWORD"),
                              db=self.DBConfig.get("DBNAME"),
                              use_unicode=True,
                              charset="utf8",
                              cursorclass=DictCursor,
                              blocking=True)
            return __pool.connection()

    def getOne(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        self._cursor.execute(sql,param)
        result = self._cursor.fetchone()
        return result


    def getAll(self,sql,param=None):
        self._cursor.execute(sql, param)
        result = self._cursor.fetchall()
        return result

