import sys

sys.path.append('D:\prjs_all\my_app\prjs_edk')

import pyedk


sOutFile='c:/pub/ws01.txt'
sDt0='2016-01-01'
sDt1='2016-02-01'

print "data begin"
ws=pyedk.qz.net_ws.ws_reader()
#not ??
#ws.wsData_days("dyu01","53001_2_4112",10)
ws.wsData("dyu01","53001_2_4112","2015-01-01","2015-01-31")
print "data end"