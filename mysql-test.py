import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='HanDong85',db='nickname',port=3306)
# 创建游标
cursor = conn.cursor()

# cursor.execute("select * from Nickname")
# row_1 = cursor.fetchone()
# print(row_1)

#SQL 插入语句
sql = """INSERT INTO Nickname(name)\
         VALUES ('13Dong')"""

insertRow = cursor.executemany('INSERT INTO user (name, password, age) VALUES (%s, %s, %s)', [('happyheng', '123456', '22'), ('happyheng2', '123456', '22')])
print('插入的行数为' + str(insertRow))
cursor.execute(sql)

# SQL 查询语句
# sql = "SELECT * FROM Nickname \
#        WHERE name = '%s'" % ('12Dong')
# cursor.execute(sql)
# results = cursor.fetchall()
# if results is None:
#     print('Yes')
# else:
#     print('No')
# SQL 删除语句
# sql = "DELETE FROM Nickname WHERE name = '%s'" % ('13Dong')
# cursor.execute(sql)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()