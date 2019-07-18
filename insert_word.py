import pymysql
import re

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标(操作数据库，执行sql语句)
cur = db.cursor()

f = open('dict.txt')
# data = f.readline().split(' ')
# f_name = data[0]
# f_comment = ' '.join(data[1:]).strip()
sql = 'insert into words (name,comment) values (%s,%s)'
for line in f:
    tup = re.findall(r'(\S+)\s+(.*)', line)[0]

    try:
        cur.execute(sql, tup)  # 执行语句

        db.commit()  # 将写操作提交，多次写操作一同提交
    except Exception as e:
        db.rollback()  # 退回到commit执行之前的数据库状态
        print(e)

f.close()
# 关闭数据库
cur.close()
db.close()
