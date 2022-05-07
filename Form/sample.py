import pymysql
print("---Database Connection Model------")
x=pymysql.connect(host='localhost',user='root',password='prejin2310',database='sample')
cr=x.cursor()
#cr.execute('create table demo(name varchar(25),age int)')
a='insert into demo values("arun",36)'
cr.execute(a)
x.commit()
x.close()
