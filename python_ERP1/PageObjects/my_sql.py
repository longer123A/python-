import pymysql

class MySql:
    def get_sku(self,sku,limit):
        db = pymysql.connect("192.168.99.205", "bessky_pss", "20092009", "bessky_pss")
        cursor = db.cursor()
        sql="SELECT uuid FROM t_sku_trace WHERE sku='{0}' ORDER BY creation_date DESC LIMIT {1}" .format(sku,limit)
        cursor.execute(sql)
        result = cursor.fetchall()
        # return str(''.join(result))
        return result
if __name__ == '__main__':
    S=MySql().get_sku('SFW70621314L3',3)
    print(S)