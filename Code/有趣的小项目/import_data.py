import pymysql
import pandas as pd


def import_data(filename):
    db = pymysql.connect(host='47.104.128.150', user='root', password='123456', port=3306)
    cursor = db.cursor()
    cursor.execute('use stock')
    df = pd.read_excel(filename)
    nrows = df.shape[0]
    for i in range(1,nrows):
        Id = df.iloc[i,0]
        Name = df.iloc[i,1]
        Rate = df.iloc[i,2]
        BGQ = '20151231'
        sql = 'insert into TB_RATE_PROFIT(SECID,SECNAME,REPORT,RATE) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (Id, Name, BGQ, Rate))
            db.commit()
        except:
            db.rollback()
    db.close()


if __name__ == '__main__':
    filename = '全部A股.xlsx'
    import_data(filename)
    #data = pd.read_excel(filename)
    #print(data.shape)
    #print(data.shape[0])




