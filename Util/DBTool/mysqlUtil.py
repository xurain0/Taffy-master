# coding=utf-8
import sys
import os
import MySQLdb

from baseUtil import *


class MysqlUtil(BaseUtil):
    """数据库工具类，提供连接池以及执行sql语句的方法"""

    def __init__(self, connection):
        """Constructor"""
        super(MysqlUtil, self).__init__(connection)
        self.cursor = self.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def executeQuery(self, sql, params=()):

        data = []
        result = self.cursor.execute(sql, params)
        data = self.cursor.fetchall()
        return data

    def executeNonQuery(self, sql, params=()):
        try:
            result = 0
            result = self.cursor.execute(sql, params)
            self.connection.commit()
            # res = self.cursor._cursor.rowcount
        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print e
        finally:
            if result:
                lastid = self.cursor.lastrowid
                if lastid:
                    result = lastid

            return result
