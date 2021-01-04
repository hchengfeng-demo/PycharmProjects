# ！ /usr/bin/python
# _*_ coding:UTF-8 _*_

import pymysql

# 打开数据库连接
db = pymysql.connect('192.168.1.104', 'root', '123456', 'work_list')

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用预处理sql语句
sql = """insert into worker(id,workerName,identify) 
                            values
                            ('00001','huangchengfeng','429004199207241411');"""

# 使用execute()方法执行sql查询
try:
    cursor.execute(sql)
    # 提交到数据库    
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
