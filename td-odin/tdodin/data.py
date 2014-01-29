import pymysql


conn = pymysql.connect(
    host='localhost',
    unix_socket='/var/run/mysqld/mysqld.sock',
    user='gloreus_tdodin68',
    passwd='c300g',
    db='gloreus_tdodin68',
    port='3306',
    charset='cp1251'
    )

catalog = None

def get_tree():
    def get_sub_tree(parent_id):
        cur = conn.cursor()
        if parent_id:
            parent = "= '" + parent_id + "'"
        else:
            parent = 'is null'

        sql = """
        select
    	  t.code
        , t.name
    	, (select count(*) from TreeItem t1 where t1.parent = t.code and t1.is_node = 1) as cnt
        from TreeItem t
        where t.parent {0} and t.is_node = 1
        order by code
        """.format(parent)
        
        cur.execute(sql)
        d = [
            {'code': r[0],
             'name': r[1],
             'cnt': r[2],
             'childrens': (get_sub_tree(r[0]) if r[2] > 0 else []) 
             } for r in cur]
        cur.close()
        return d

    global catalog    
    if not catalog:
        catalog = get_sub_tree(None)
    return catalog

def update_catalog():
    f = open('templates/catalog.html', 'w')
    f.write('test')
    c = 
    f.close()
