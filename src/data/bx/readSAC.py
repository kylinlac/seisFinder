import sys

sys.path.append('D:\prjs_all\my_app\prjs_edk')

import pyedk

sSacFile='c:/pub/1.sac'
sOutFile='c:/pub/1a.txt'
sr=pyedk.bx.file_sac.sac_reader()
sr.read(sSacFile)
sr.export_text(sOutFile)
print "end..."