import pymysql  # 导入pymysql模块


class ssql(object):
    # 初始化链接服务器
    def __init__(self, host, port, user, password,db):

        print('正在连接MySQL服务器...')
        try:
            self.conn = pymysql.connect(host=host,port=port,user=user,password=password,db=db)
            print('已成功连接！')
        except Exception as e:
            print('连接服务器失败！请检查参数！', e)
        else:
            self.cursor = self.conn.cursor()
            print('游标已生成！请后续操作！')

    # 自动断开连接
    def __del__(self):
        try:
            self.conn.close()
            print('已断开与mysql服务器连接！')
        except AttributeError as e:
            print('断开无效，数据库未成功连接：', e)

    # 建表
    def create_table_func(self, create_table=None):
        if create_table != None:
            try:
                self.cursor.execute(create_table)
                print('数据表创建成功！')
            except AttributeError as e:
                print('数据表创建失败！\n游标未生成！请检查数据库连接！', e)
        else:
            print('请输入sql建表语句！')

    # 插入数据
    def insert_date(self, insert=None):
        if insert != None:
            try:
                self.cursor.execute(insert)
                self.conn.commit()
                print('插入数据成功！')
            except Exception as e:
                print('插入数据失败，错误原因是：{}\n准备回滚...'.format(e))
                # print(traceback.format_exc())
                try:
                    self.conn.rollback()
                    print('已回滚！')
                except AttributeError as e:
                    print('回滚失败！\n游标未生成！请检查数据库连接！', e)
        else:
            print('请输入sql语句！')

    # 更新数据
    def update_data(self, update=None):
        if update != None:
            try:
                self.cursor.execute(update)
                self.conn.commit()
                print('数据更新成功！')
            except Exception as e:
                print('数据更新失败！错误原因是：{}\n准备回滚...'.format(e))
                # print(traceback.format_exc())
                try:
                    self.conn.rollback()
                    print('已回滚！')
                except AttributeError as e:
                    print('回滚失败！\n游标未生成！请检查数据库连接！', e)
        else:
            print('请输入sql语句！')

    # 删除数据
    def delete_data(self, delete=None):
        if delete != None:
            self.cursor.execute('SELECT *' + delete[7:])
            if self.cursor.fetchall() != ():
                try:
                    self.cursor.execute(delete)
                    self.conn.commit()
                    print('删除成功！')
                except Exception as e:
                    print('删除失败！错误原因是：', e)
                    self.conn.rollback()
            else:
                print('删除失败！未查询到该数据!')
        else:
            print('请输入sql语句！')

    # 查询数据
    def select_data(self, select=None):
        if select != None:
            try:
                self.cursor.execute(select)
                all_data = self.cursor.fetchall()
                if all_data != ():
                    for i in all_data:
                        print('查询结果为：id:{},name:{},age:{},sex:{}'.format(i[0], i[1], i[2], i[3]))
                else:
                    print('查询失败，服务器无该条数据！')
            except Exception as e:
                print('sql语句错误！：', e)
        else:
            print('请输入sql语句！')


#if __name__ == '__main__':


    #create_table = 'create table stu(id int not null primary key auto_increment,name varchar(255) not null,age int, sex varchar(255))default charset=utf8'
    #select = 'SELECT * FROM activity'
    #update = 'update stu set name="小王" where id=6'
    #delete = 'delete from stu where id=2'
    #insert = 'insert into stu(name,age,sex) values("%s","%d","%s")' % ('小鱼', 9, '男')

    # # 执行
    #my = PyMySQL('192.168.17.214',3306, 'wangmin', 'cndsdis', 'official_website')

    # # my.create_table_func(create_table)
    # # my.insert_date(insert)
    # # my.update_data(update)
    # # my.delete_data(delete)
    # my.select_data(select)
