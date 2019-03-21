import sys

sys.path.append('D:\prjs_all\my_app\prjs_edk')

import pyedk


sInDir='c:/pub/pyRds/bx.0/wave'
sOutDir='c:/pub/pyRds/bx.0/web'
sNet="SC"
sSta="CD2"
sDt0='2016-11-25_14:00:00'
sDt1='2016-11-25_14:20:00'
sOutFilePrefix='SC-CD2-123456'
#pyedk.bx.job_get_miniseed_tree.bxGet(sInDir,sOutDir,sNet,sSta,sDt0,sDt1,sOutFilePrefix)

sInFile='c:/pub/1.dat'
sOutFile='c:/pub/1o.txt'
sDt0='2016-01-01'
sDt1='2016-02-01'
fr=pyedk.qz.file_text6.fileText6_reader()
fr.read(sInFile)
print 'read finished...'
fr.export_part(sOutFile,sDt0,sDt1)
print 'export finished...'

