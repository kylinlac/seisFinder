import MySQLdb

def getData():
  conn=MySQLdb.connect(host='10.16.160.222',user='root',passwd='sycWEB1234',db='syc_web',port=3306)
  cur=conn.cursor()
  count=cur.execute('select * from tb_user')
  print "rows: %s" % count
  #res1=cur.fetchone()
  #print res1
  #res3=cur.fetchmany(3)
  #print res3
  res0=cur.fetchall()
  print res0
  cur.close()
  conn.close()

  print
  print res0[0][0],res0[0][2]


if __name__=="__main__":
  getData()
