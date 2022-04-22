import string
import pymysql

def AccessLog():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()
	query = "select * from accesslogDB"

	cur.execute(query)
	cur.commit()
	result = cur.fetchall()
	conn.close()

	print(result)


def ErrorLog():
	conn = pymysql.connect(host='localhost', user='root', password='rootPassword', db='dbName', charset='utf8')
	cur = conn.cursor()
	query = "select * from errorlogDB"

	cur.execute(query)
	cur.commit()
	result = cur.fetchall()
	conn.close()

	print(result)


if __name__ == "__main__":
	AccessLog()
	ErrorLog()