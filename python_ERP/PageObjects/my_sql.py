import pymysql

class MySql:

    #数据库二维码序号查询
    def get_sku(self,sku,limit):
        db = pymysql.connect("192.168.99.205", "bessky_pss", "20092009", "bessky_pss")
        cursor = db.cursor()
        sql="SELECT uuid FROM t_sku_trace WHERE sku='{0}' ORDER BY creation_date DESC LIMIT {1}" .format(sku,limit)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def get_scan(self,mold):

        db = pymysql.connect("192.168.99.205", "bessky_pss", "20092009", "bessky_pss")
        cursor = db.cursor()
        sql = "SELECT transportation_classify FROM t_transportation_limit WHERE FIND_IN_SET((select CONCAT(transportation_mode_id)from t_transportation_mode where transportation_mode_chinese = '{0}'), transportation_ids) limit 1".format(mold)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
if __name__ == '__main__':
    S=MySql().get_scan("1")
    print(S[0][0])