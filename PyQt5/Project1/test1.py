import pandas as pd
import numpy as np

data = pd.read_csv('QuadMedicine/Mitutoyo/data/NT7_InjMol_Monument800/20190724_data2.csv',
                   engine='python', index_col=False)
# only save information about height of individual microneedle into variable
height_tiptobase = data.Nominal*1000

print(height_tiptobase.describe()[-1])

# make height information into numpy array
arrayheight_tiptobase = np.array(height_tiptobase)

numpy_array_1 = np.zeros([11, 11])
numpy_array_1[10, :3] = None
numpy_array_1[10, 3:8] = arrayheight_tiptobase[:5]  # 1
numpy_array_1[10, 8:] = None

numpy_array_1[9, :2] = None
numpy_array_1[9, 2:9] = arrayheight_tiptobase[5:12]  # 2
numpy_array_1[9, 9:] = None

numpy_array_1[8, 0] = None
numpy_array_1[8, 1:10] = arrayheight_tiptobase[12:21]  # 3
numpy_array_1[8, 10] = None

numpy_array_1[7, 0:11] = arrayheight_tiptobase[21:32]  # 4
numpy_array_1[6, 0:11] = arrayheight_tiptobase[32:43]  # 5
numpy_array_1[5, 0:11] = arrayheight_tiptobase[43:54]  # 6
numpy_array_1[4, 0:11] = arrayheight_tiptobase[54:65]  # 7
numpy_array_1[3, 0:11] = arrayheight_tiptobase[65:76]  # 8

numpy_array_1[2, 0] = None
numpy_array_1[2, 1:10] = arrayheight_tiptobase[76:85]  # 9
numpy_array_1[2, 10] = None

numpy_array_1[1, :2] = None
numpy_array_1[1, 2:9] = arrayheight_tiptobase[85:92]  # 10
numpy_array_1[1, 9:] = None
#
numpy_array_1[0, :3] = None
numpy_array_1[0, 3:8] = arrayheight_tiptobase[92:]  # 11
numpy_array_1[0, 8:] = None
