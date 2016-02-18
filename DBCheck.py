__author__ = 'saipc'

import MySQLdb
import DB


def getopenconnection():
    return MySQLdb.connect(DB.ip, DB.username, DB.password,
                                   DB.database_name)

def check_conn():
    conn = getopenconnection()
    cursor = conn.cursor()
    cursor.execute('DESC `form`')
    rows = cursor.fetchall()
    print rows

check_conn()