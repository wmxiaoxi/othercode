from  common_fuc.my import *
from common_fuc.con_sql import  *
#
# #连接hive
# sql="SELECT * FROM t_box_office_1021 WHERE  name LIKE '%中国机长%'"
# newhivsql=InceptorConnect()
# newconn=newhivsql.hiveConnect()
# result=newhivsql.getData(newconn, sql)
# print(len(result))
# newhivsql.close(newconn)


# #连接mysql
# my1=ssql('192.168.17.214',3306,'wangmin','cndsdis','official_website')
# cur.execute("SELECT count(*) FROM t_box_office_1021 WHERE id=98605340 AND name LIKE '%中国机长%'")
# print (cur.fetchall())
# cur.close()
# con.close()



###连接postgresql
sql="select * from public.record_summary where type='电影'"
newpg=InceptorConnect()
newpgcoon=newpg.postgconnect()
result=newpg.get_all_data(newpgcoon,sql)
print(len(result),result)


