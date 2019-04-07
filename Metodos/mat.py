import numpy as np
from numpy import pi
import math

mat2 = np.matrix([[1,2, 3],[4,5,6]])
mat1 = np.matrix ([[2,0],[1,3]])
mat3 = np.matrix ([[2,-2],[3,1]])


def transpose():
    mat = np.transpose(mat1)
    print(mat)
    return mat

def print_mat(mat):
    print(mat)

#print_mat(mat1)
#transpose()

def mat_add(mat1, mat2):
    mat = np.add(mat1, mat2)
    print(mat)
    return mat

def mat_res(mat1, mat2):
    mat = np.subtract(mat1,mat2)
    print(mat)
    return mat

def mat_mul(mat1, mat2):
    mat = np.dot(mat1, mat2)
    print(mat)
    return mat


mat_mul(mat1, mat2)