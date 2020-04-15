import numpy as np
import sys
import xml.etree.ElementTree

matr = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])
print(matr.size)

'''
print(matr.reshape((12)))
a_str = ','.join(str(x) for x in matr.reshape((12))) # '0,3,5'
a2 = np.array([int(x) for x in a_str.split(',')]) # np.array([0, 3, 5])
print('res',a2)

'''
matr = np.ones((3,3))

'''
row = np.array([[12,13,14]])
print('row shape', row.shape)
print(matr)
k = 2
matr = np.append(matr, row, axis=0)
m = matr.shape[0]
n = matr.shape[1]
print(matr)
matr[[k, m-1]]= matr[[m-1, k]]
print('add row \n', matr)

'''
print(matr)
k = 2
m = matr.shape[0]
n = matr.shape[1]
column = np.array([[12,13,14]])
#def add_column(self, k, column):
matr = np.append(matr, column.T, axis=1)
matr[:,[k,n]]= matr[:,[n,k]]
print(matr)


'''
#def delete_row(self,k):
matr = np.delete(matr, k, axis=0)
print(matr)

#def delete_column(self,k):
matr = np.delete(matr, k, axis=1)
print(matr)
'''


# xml.etree.ElementTree.dump(matr)

'''
FILENAME = "state.xml"
tree = xml.etree.ElementTree.parse(FILENAME)
'''