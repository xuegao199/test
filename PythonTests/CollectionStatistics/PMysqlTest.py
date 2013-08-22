#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import MySQLdb as mdb
import sys

'''
 测试python mysql
'''

con = None

try:

    con = mdb.connect('localhost', 'root','', 'test')
    cur = con.cursor()

    #cur.execute("INSERT INTO collection_statistic(check_time,google_hk,soso,sougou,baidu,so,yahoo) VALUES(SYSDATE(),'743,000','168,824','1','1','985','939')")
    cur.execute("SELECT * FROM collection_statistic")

    rows = cur.fetchall()

    for row in rows:
        print row

except _mysql.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:

    if con:
        con.commit()
        con.close()