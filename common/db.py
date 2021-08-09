from pymysql import connect
from sshtunnel import SSHTunnelForwarder


class Mysql:



    db = connect(
        host="xxx",
        port=3306,
        #port=server.local_bind_port,
        user="xx",
        passwd="xx",
        db="xx")
    #print("端口：" + str(server.local_bind_port))

    cursor = db.cursor()

    def gather_sql(self, sql_sentence):
        """ 包括更新、删除、添加sql """
        try:
            self.db.ping(reconnect=True)  # 检查连接是否断开，如果断开就进行重连
            self.cursor.execute(sql_sentence)
            self.db.commit()               # 提交至数据库执行
        except Exception as e:
            print("操作出现错误：{}".format(e))
            self.db.rollback()             # 发生错误时回滚

    def insert_sql(self, sql_sentence):
        """ 插入sql """
        self.gather_sql(sql_sentence)

    def update_sql(self, sql_sentence):
        """ 更新sql """
        self.gather_sql(sql_sentence)

    def delete_sql(self, sql_sentence):
        """ 删除sql """
        self.gather_sql(sql_sentence)

    def select_sql(self, sql_sentence):
        """ 查询sql """
        self.db.ping(reconnect=True)
        self.cursor.execute(sql_sentence)
        results = self.cursor.fetchall()
        for row in results:
            result = row[0]
            return result
        self.db.close()
        self.server.close()

    def select_sql_all(self, sql_sentence):
        """ 查询sql全部数据 """
        self.db.ping(reconnect=True)
        self.cursor.execute(sql_sentence)
        results = self.cursor.fetchall()
        return results

    def server_close(self):
        self.db.close()
        self.server.close()



