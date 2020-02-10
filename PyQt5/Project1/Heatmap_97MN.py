# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2
import pandas as pd


def makingheatmap(dataname):

    # read excel data by pandas
    data = pd.read_csv(dataname, engine='python', index_col=False)
    # only save information about height of individual microneedle into variable
    height_tiptobase = data.Nominal*1000

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

    # annotating heatmap by text
    #annotate_heatmap(im, valfmt="{x:.1f}")

    return numpy_array_1, height_tiptobase


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


# Sample 여러개일 때 돌리는 코드

## fname = []
# data 중 가장 첫번째 번호
## sample_num1 = 1
# data 중 가장 마지막 번호
## sample_num2 = 3
# for i in range(sample_num1, sample_num2 + 1):
# fname.append(f"Data/NT7_InjMol_Monument800/20190724_data{i}.cs## v")

# dataname =##  []
##
# 총 측정할 샘플 갯수
# Num_sample ## = 3

plt.show()
