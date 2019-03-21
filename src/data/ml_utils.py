
import pickle

def ml_EqtToMl2(eqt):
  ml2=[]
  return ml2


def ml_Dump(inFile,outFile):
  f1=open(inFile,"r")
  data1=f1.readlines()
  f1.close()

  output = open(outFile, 'wb')
  pickle2.dump(data1, output)
  # Pickle the list using the highest protocol available.
  #pickle2.dump(data1, output, -1)
  output.close()



