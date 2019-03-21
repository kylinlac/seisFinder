'''
dump/load file format is ml2
eqt is plain text


'''

import pickle


def ml_EqtToMl2(eqt):
  ml2=[]
  return ml2


def ml_Dump(inFile,outFile):
  f1=open(inFile,"r")
  data1=f1.readlines()
  f1.close()

  output = open(outFile, 'wb')
  pickle.dump(data1, output)
  # Pickle the list using the highest protocol available.
  #pickle2.dump(data1, output, -1)
  output.close()


def ml_Load(inFile):
  pkl_file = open(inFile, 'rb')
  data1 = pickle.load(pkl_file)
  #pprint.pprint(data1)
  #data2 = pickle.load(pkl_file)
  #pprint.pprint(data2)
  pkl_file.close()
  return data1

