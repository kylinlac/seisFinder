#使用pickle模块将数据对象保存到文件

import pickle as pickle2
#import cPickle as pickle2

f1=open("ms6.txt","r")
data1=f1.readlines()
f1.close()
'''
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
'''
output = open('ms6.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle2.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle2.dump(data1, output, -1)

output.close()