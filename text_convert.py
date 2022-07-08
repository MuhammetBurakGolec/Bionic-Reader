from openpyxl import NUMPY

try:
    import numpy as np

except ImportError:
    print("Import Error --text_conver--")

def __init__matrix(text):
    text_matrix = []
    for i in range(len(text)):
        text_matrix.append(0)

#text_arr = np.array([],ndim=1) # 2 dimension



