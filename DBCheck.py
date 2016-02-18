__author__ = 'saipc'

import MySQLdb
import DB


def getopenconnection():
    return MySQLdb.connect('129.219.234.194', 'saipc', '',
                                   'ejection')

