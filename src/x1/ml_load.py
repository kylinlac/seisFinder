#使用pickle模块从文件中重构python对象

import pprint, pickle


def load_ms6():
  pkl_file = open('ms6.pkl', 'rb')
  data1 = pickle.load(pkl_file)
  pprint.pprint(data1)

  data2 = pickle.load(pkl_file)
  pprint.pprint(data2)

  pkl_file.close()

  return data1