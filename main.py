# standard imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io
import datetime

data_path = "PQDSC\\dataset\\PowerQualityDistributionDataset1.csv"
# mat_data_path = "PQDSC\\dataset\\5Kfs_1Cycle_50f_1000Sam_1A.mat" # keys: '__header__'、'__version__'、'Out'、1000x100x17
# keys: '__header__'、'__version__'、'__globals__'、'SignalsDataBase'、7680x640x
mat_data_path = "PQDSC\\dataset\\16PQDs_480_NoNoise.mat"


def csv_data_Read():
    data_frame = pd.read_csv(data_path, encoding='utf-8')
    data_frame.drop(data_frame.columns[[0]], axis=1, inplace=True)
    print('data head:', data_frame.head())
    print('data shape:', data_frame.shape)
    print('data type:', type(data_frame))
    data_array = data_frame.to_numpy()
    print('data type:', type(data_array))   # <class 'numpy.ndarray'>
    return data_array


X = [None]
Y = [None]


def mat_data_Read():
    data_original = scipy.io.loadmat(mat_data_path)
    print('type:', type(data_original))  # dict type
    print('data:', data_original.keys())
    print('__header__:', data_original['__header__'])
    print('__version__:', data_original['__version__'])
    # data_real = data_original['Out']
    print('__globals__:', data_original['__globals__'])
    data_real = data_original['SignalsDataBase']
    print('data_real type:', type(data_real))  # <class 'numpy.ndarray'>
    print('data_real shape:', data_real.shape)
    return data_real


def data_visualization(data, num):
    t = np.arange(640)
    plt.show()


def funs():
    pass


def main():
    # original_data = data_Read()
    mat_data = mat_data_Read()


if __name__ == "__main__":
    main()
