import json, mysql.connector

conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1')
cur = conn.cursor()
cur.execute("use yelp;")
cur.execute("begin;")

with open('../raw.nosync/categories.txt', 'r') as f:
    for line in f:
        u = line[:-1].split(', ')
        s = 'insert into Categories (category_id, category_name) values (' + u[0] + ', "' + u[1] + '");'
        # s = 'UPDATE Categories SET category_name = "' + u[1] + '" WHERE category_id = ' + u[0] + ';'
        # print(s)
        cur.execute(s)
cur.execute("commit;")