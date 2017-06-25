# coding=utf-8
try:
    import MySQLdb
except:
    import pymysql

    pymysql.install_as_MySQLdb()