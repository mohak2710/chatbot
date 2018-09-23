import xml.dom.minidom
import xml.etree.ElementTree as ET
CONFIG_URI = 'MYSQL'
# CONFIG_URI = 'SQLALCHEMY'


if CONFIG_URI == 'MYSQL':
    dbhost = "localhost"
    dbuser = "root"
    dbpass = "mohak27102893"
    dbname = "chatbot"
    DB_URI = 'mysql+pymysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname
elif CONFIG_URI == 'SQLALCHEMY':
    DB_URI = 'sqlite:///retail.db'



#
# tree = ET.parse('app/config.xml')
# root = tree.getroot()
#
# # for database in root.findall('database'):
# #     dbname = database.get('name') # database name
# #     dbhost = database.find('dbhost').text  #ip address
# #     dbuser = dbuser.find('dbuser')
# #
# #     print dbuser
# #
#
# # use the parse() function to load and parse an XML file
# doc = xml.dom.minidom.parse("app/config.xml");
#
# # print out the document node and the name of the first child tag
# print doc.nodeName
# print doc.firstChild.tagName
#
#
# # get a list of XML tags from the document and print each one
# database = doc.getElementsByTagName("database")
# print database.dbuser




#============================================================
#  MYSQL database conectivity**************************

##  How to start MYSQL server of PhpMyadmin
##    sudo /opt/lampp/lampp start  ( XAMP server)


#============================================================
# def mysqlconnection():
#
#     try:
#         conn = MySQL.connect(
#                     host='127.0.0.1',
#                     port=3303,
#                     user='root',
#                     passwd='',
#                     db='chatbot'
#                 )
#         print("MYSQL database connected successful")
#         c = conn.cursor()
#         return c, conn
#
#     except Exception as e1:
#         print("database not connected: please start before mysql server")


# mysqlconnection()