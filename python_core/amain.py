# from dbsettings import connection_properties
#
# try:
#     self.conn = pymysql.connect(**connection_properties)
#     self.curr = self.conn.cursor()
# except pymysql.err.OperationalError :
#     sys.exit("Invalid Input: Wrong username/database or password found, please try again")