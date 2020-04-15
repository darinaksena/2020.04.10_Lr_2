import numpy as np
import string
import sys
import xml.etree.ElementTree as xml
import xml.etree.cElementTree as ET

class Matrix:
 
    m = 0
    n = 0
    matr = np.zeros((m,n), dtype= int)
 
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matr = np.ones((m,n), dtype= int)

    def set_matr(self, matr):
        self.matr = matr
        self.m = self.matr.shape[0]
        self.n = self.matr.shape[1]
        print('m', self.m)
        print('n', self.n)

    def show(self):
        print(self.matr)

    def add_row(self, k, row):
        self.matr = np.append(self.matr, row, axis=0)
        m = self.m
        self.matr[[k, m]]= self.matr[[m, k]]
        self.m = self.matr.shape[0]
        self.n = self.matr.shape[1]

    def add_column(self, k, column):
        n = self.n
        column = column.T
        self.matr = np.append(self.matr, column, axis=1)
        self.matr[:,[k,n]]= self.matr[:,[n,k]]
        self.m = self.matr.shape[0]
        self.n = self.matr.shape[1]
        
    def delete_row(self,k):
        self.matr = np.delete(self.matr, k, axis=0)
        self.m = self.matr.shape[0]
        self.n = self.matr.shape[1]

    def delete_column(self,k):
        self.matr = np.delete(self.matr, k, axis=1)
        self.m = self.matr.shape[0]
        self.n = self.matr.shape[1]
    
    def createXML(self, filename):
        
        #Создаем XML файл.
        root = xml.Element("zAppointments")
        appt = xml.Element("appointment")
        root.append(appt)
        
        # создаем дочерний суб-элемент. 
        m_xml = xml.SubElement(appt, "m")
        m_xml.text = str(self.m)
        
        n_xml = xml.SubElement(appt, "n")
        n_xml.text = str(self.n)

        
        ts = self.matr.reshape((self.matr.size))
        ts2 = ','.join(str(x) for x in ts)
        arr_xml = xml.SubElement(appt, "matr")
        arr_xml.text = ts2
        
        tree = xml.ElementTree(root)
        with open(filename, "wb") as fh:
            tree.write(fh)

def parseXML(xml_file):

    #Парсинг XML используя ElementTree
    tree = ET.ElementTree(file=xml_file)
    #print(tree.getroot())
    root = tree.getroot()
    #print("tag=%s, attrib=%s" % (root.tag, root.attrib))
    '''
    for child in root:
        #print(child.tag, child.attrib)
        if child.tag == "appointment":
            for step_child in child:
                #print(step_child.tag)
'''
    # Парсинг всей XML структуры.
    iter_ = tree.getiterator()

    # получаем данные используя дочерние элементы
    appointments = root.getchildren()
    
    for appointment in appointments:
        appt_children = appointment.getchildren()
        m = int(appt_children[0].text)
        n = int(appt_children[1].text)
        tmp = appt_children[2].text
        try:
            tmp = np.array([int(x) for x in tmp.split(',')])
        except:
            tmp = np.zeros((m,n), dtype = int)
        m_matr = tmp.reshape((m,n))
        matrix = Matrix(m,n)
        matrix.set_matr(m_matr)

        '''
        for appt_child in appt_children:
            print(appt_child.text)
            
            m_m = int(appt_children[0].text)
            m_n = int(appt_children[1])
            res = np.fromstring(appt_children[2] ,dtype=int)
            m_matr = res.reshape((m,n))
            matrix = Matrix(m,n)
            matrix.set_matr(m_matr)
            '''
    return matrix

def what_to_do():
    print('To add a row input [1]')
    print('To add a colump input [2]')
    print('To delete a row input [3]')
    print('To delete a column input [4]')
    print('To exit the program input [q]')
    print('Tip: use negative index value for backward indexing')
    return (input('Your choice: '))

def input_rc(n):
    arr = np.zeros((1,n), dtype = int)
    print('Input new row(column):')
    for i in range(n):
        arr[0][i] = input('Elem ')
    return arr




FILENAME = "state.xml"
'''
m = int(input('Input m '))
n = int(input('Input n '))
'''
#matrix = Matrix(2,2)
#matrix.createXML(FILENAME)


matrix = parseXML('state.xml')
print('Your matrix is:')
matrix.show()

op = ''
while (op != 'q'):
    op = what_to_do()
    matrix = parseXML('state.xml')
    if op == '1':
        try:
            k = int(input('Number of a row '))
            if k > matrix.n+1: raise IndexError
            elem = input_rc(matrix.n)
            matrix.add_row(k, elem)
        except IndexError:
            print('Please, try correct row index')
    elif op == '2':
        try:
            k = int(input('Number of a colunm '))
            if k > matrix.m+1: raise IndexError
            elem = input_rc(matrix.m)
            matrix.add_column(k, elem)
        except IndexError:
            print('Please, try correct column index ')
    elif op == '3':
        try:
            k = int(input('Number of a row to delete '))
            matrix.delete_row(k)
        except IndexError:
            print('Try correct row index ')
    elif op == '4':
        try:
            k = int(input('Number of a column to delete '))
            matrix.delete_column(k)
        except IndexError:
            print('Try correct column index ')
    elif op == 'q':
        exit(0)
    else:
        print('Type a correct message ')
    matrix.show()
    matrix.createXML(FILENAME)