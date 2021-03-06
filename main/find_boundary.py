import numpy as np
import matplotlib.pyplot as plt
def find_bound (label, size):
    height = size[0]
    width = size[1]
    ret = np.zeros([height,width, 1], dtype=bool)
    div = label.reshape([height,width,1])
    df0 = np.diff(div,axis=0)
    df1 = np.diff(div,axis=1)
    mask0 = df0 != 0
    mask1 = df1 != 0
    ret[0:height - 1, :, :] = np.logical_or(ret[0:height - 1, :, :], mask0)
    ret[1:height, :, :] = np.logical_or(ret[1:height, :,:], mask0)
    ret[:,  0:width-1, :] = np.logical_or(ret[:,  0:width-1,:],mask1)
    ret[:, 1:width, :] = np.logical_or(ret[:, 1:width,:], mask1)

    ret2 = np.ones([height,width,1], dtype="uint8")
    ret2 = ret2*255 - ret * 255
    # plt.imshow(ret)
    # plt.show()
    return ret2