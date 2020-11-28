import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


def np_basic():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    print(np.__version__)
    print(type(arr))
    print(np.array((1, 2, 3, 4, 5)))


def np_dim():
    arr = np.array(42)
    print(arr)
    print(arr.ndim)
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    print(arr.ndim)
    print(arr[0])
    print(arr[1])
    print(arr[2] + arr[3])
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr)
    print(arr.ndim)
    print(arr[0, 1])
    print(arr[1, 2])
    print(arr[1, -1])
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    print(arr)
    print(arr.ndim)
    print(arr[0, 1, 2])
    print(arr.shape)
    arr = np.array([1, 2, 3, 4], ndmin=5)
    print(arr)
    print(arr.ndim)


def np_slice():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    print(arr[1:5])
    print(arr[-3:-1])
    print(arr[1:5:2])
    print(arr[::2])
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(arr[1, 1:4])
    print(arr[0:2, 2])
    print(arr[0:2, 1:4])


def np_type():
    arr = np.array([1, 2, 3, 4])
    print(arr.dtype)
    arr = np.array(["apple",  "banana", "cherry"])
    print(arr.dtype)
    arr = np.array([1, 2, 3, 4], dtype="S")
    print(arr)
    print(arr.dtype)
    arr = np.array([1, 2, 3, 4], dtype="i4")
    print(arr)
    print(arr.dtype)
    arr = np.array([1.1, 2.1, 3.1])
    newarr = arr.astype(int)
    print(newarr)
    print(newarr.dtype)
    arr = np.array([1, 0, 3])
    newarr = arr.astype(bool)
    print(newarr)
    print(newarr.dtype)


def np_copy():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42
    print(arr)
    print(x)
    x = arr.view()
    arr[0] = 42
    print(arr)
    print(x)
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    y = arr.view()
    print(x.base)
    print(y.base)


def np_shape():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr.shape)
    arr = np.array([1, 2, 3, 4], ndmin=5)
    print(arr.shape)


def np_reshape():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(4, 3)
    print(newarr)
    newarr = arr.reshape(2, 3, 2)
    print(newarr)
    print(arr.reshape(4, 3).base)
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    newarr = arr.reshape(2, 2, -1)
    print(newarr)
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    newarr = arr.reshape(-1)
    print(newarr)
    newarr = arr.flatten()
    print(newarr)


def np_iter():
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    for x in np.nditer(arr):
        print(x)
    arr = np.array([1, 2, 3])
    [print(x) for x in np.nditer(arr, flags=["buffered"], op_dtypes=['S'])]
    arr = np.array([1, 2, 3])
    [print(i, x) for i, x in np.ndenumerate(arr)]
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    [print(i, x) for i, x in np.ndenumerate(arr)]


def np_join():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arr = np.concatenate((arr1, arr2))
    print(arr)
    arr = np.stack((arr1, arr2), axis=0)
    print(arr)
    arr = np.hstack((arr1, arr2))
    print(arr)
    arr = np.vstack((arr1, arr2))
    print(arr)
    arr = np.dstack((arr1, arr2))
    print(arr)
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((arr1, arr2), axis=1)
    print(arr)
    arr = np.concatenate((arr1, arr2), axis=0)
    print(arr)
    arr = np.stack((arr1, arr2), axis=1)
    print(arr)
    arr = np.stack((arr1, arr2), axis=0)
    print(arr)


def np_split():
    arr = np.array([1, 2, 3, 4, 5, 6])
    newarr = np.array_split(arr, 3)
    print(newarr)
    print(newarr[0])
    print(newarr[1])
    print(newarr[2])
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    newarr = np.array_split(arr, 3)
    print(newarr)
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    newarr = np.vsplit(arr, 3)
    print(newarr)


def np_search():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)
    print(x)
    x = np.where(arr % 2 == 0)
    print(x)
    arr = np.array([6, 7, 8, 9])
    x = np.searchsorted(arr, 7)
    print(x)
    x = np.searchsorted(arr, 7, side="right")
    print(x)
    arr = np.array([1, 3, 5, 7])
    x = np.searchsorted(arr, [2, 4, 6])
    print(x)


def np_sort():
    arr = np.array([3, 2, 0, 1])
    print(np.sort(arr))
    arr = np.array(["banana", "cherry", "app"])
    print(np.sort(arr))
    arr = np.array([True, False, True])
    print(np.sort(arr))
    arr = np.array([[3, 2, 4], [5, 0, 1]])
    print(np.sort(arr))


def np_filter():
    arr = np.array([41, 42, 43, 44])
    x = [True, False, True, False]
    newarr = arr[x]
    print(newarr)
    newarr = arr[arr > 42]
    print(newarr)
    newarr = arr[arr % 2 == 0]
    print(newarr)


def np_random():
    x = random.randint(100)
    print(x)
    x = random.rand()
    print(x)
    x = random.randint(100, size=5)
    print(x)
    x = random.randint(100, size=(3, 5))
    print(x)
    x = random.rand(5)
    print(x)
    x = random.rand(3, 5)
    print(x)
    x = random.choice([3, 5, 7, 9])
    print(x)
    x = random.choice([3, 5, 7, 9], size=(3, 5))
    print(x)


def np_data_distribution():
    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
    print(x)
    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
    print(x)


def np_permutation():
    arr = np.array([1, 2, 3, 4, 5])
    random.shuffle(arr)
    print(arr)
    arr = np.array([1, 2, 3, 4, 5])
    print(random.permutation(arr))


def np_normal_distribution():
    x = random.normal(size=(2, 3))
    print(x)
    x = random.normal(loc=1, scale=2, size=(2, 3))
    print(x)
    sns.distplot(random.normal(size=1000), hist=False)
    plt.show()


def np_binomial_distribution():
    # x = random.binomial(n=10, p=0.5, size=1000)
    # print(x)
    # sns.distplot(x, hist=True, kde=False)
    sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
    sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
    plt.show()


def np_poisson_distribution():
    x = random.poisson(lam=2, size=10)
    print(x)
    # sns.distplot(random.poisson(lam=2, size=1000), kde=False)
    # sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
    # sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
    sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
    sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
    plt.show()


def np_uniform_distribution():
    x = random.uniform(size=(2, 3))
    print(x)
    sns.distplot(random.uniform(size=1000), hist=False)
    plt.show()


def np_logistic_distribution():
    x = random.logistic(loc=1, scale=2, size=(2, 3))
    print(x)
    # sns.distplot(random.logistic(size=1000), hist=False)
    sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
    sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
    plt.show()


def np_multinomial_distribution():
    x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    print(x)


def np_exponential_distribution():
    x = random.exponential(scale=2, size=(2, 3))
    print(x)
    sns.distplot(random.exponential(size=1000), hist=False)
    plt.show()


def np_chi_square_distribution():
    x = random.chisquare(df=2, size=(2, 3))
    print(x)
    sns.distplot(random.chisquare(df=1, size=1000), hist=False)
    plt.show()


def np_rayleigh_distribution():
    x = random.rayleigh(scale=2, size=(2, 3))
    print(x)
    sns.distplot(random.rayleigh(size=1000), hist=False)
    plt.show()


def np_pareto_distribution():
    x = random.pareto(a=2, size=(2, 3))
    print(x)
    sns.distplot(random.pareto(a=2, size=1000), kde=False)
    plt.show()


def np_zipf_distribution():
    x = random.zipf(a=2, size=(2, 3))
    print(x)
    x = random.zipf(a=2, size=1000)
    sns.distplot(x[x<10], kde=False)
    plt.show()


if __name__ == "__main__":
    # np_basic()
    # np_dim()
    # np_slice()
    # np_type()
    # np_copy()
    # np_shape()
    # np_reshape()
    # np_iter()
    # np_join()
    # np_split()
    # np_search()
    # np_sort()
    # np_filter()
    # np_random()
    # np_data_distribution()
    # np_permutation()
    # np_normal_distribution()
    # np_binomial_distribution()
    # np_poisson_distribution()
    # np_uniform_distribution()
    # np_logistic_distribution()
    # np_multinomial_distribution()
    # np_exponential_distribution()
    # np_chi_square_distribution()
    # np_rayleigh_distribution()
    # np_pareto_distribution()
    np_zipf_distribution()













