# 3p
import numpy as np


kernel_params = {'gaussian': ['gamma']}


class Kernel:
    def __init__(self, kernel='gaussian', kernel_params=None):
        self.kernel_name = kernel
        self.kernel_params = kernel_params

    def _kernel(self):
        '''
        Returns kernel function
        where:
            - self.kernel_name: kernel type
        returns
            - kernel function
        '''
        if self.kernel_name == 'gaussian':
            def k(x, y):
                gamma = self.kernel_params['gamma']
                return np.exp(- np.sqrt(np.linalg.norm(x - y) ** 2 / (2 * gamma ** 2)))
            return k

    def _kernel_matrix(self, X_1, X_2):
        '''
        Computes kernel matrix
        where:
            - X_1: [n_1 x p] matrix
            - X_2: [n_2 x p] matrix
        returns:
            - K: [n_1 x n_2] kernel matrix .t. K[i, j] = k(X_1[i, :], X_2[j, :])
        '''
        n_1 = np.shape(X_1)[0]
        n_2 = np.shape(X_2)[0]
        K = np.zeros([n_1, n_2])
        k = self._kernel()
        for i in range(n_1):
            for j in range(n_2):
                K[i, j] = k(X_1[i, :], X_2[j, :])
        return K

    def compute_nedeed_matrices(self, data):
        d = {}
        for i in range(3):
            d["Ytr{}".format(i)] = data["Ytr{}".format(i)]
            d["Yval{}".format(i)] = data["Yval{}".format(i)]
        if self.kernel_name in ['gaussian']:
            for i in range(3):
                d["Ktr{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xtr{}_mat100".format(i)])
                d["Kte{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xte{}_mat100".format(i)])
                d["Kval{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xval{}_mat100".format(i)])
        else:
            # for i in range(3):
            #     d["Ktr{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xtr{}_mat100".format(i)])
            #     d["Kte{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xte{}_mat100".format(i)])
            #     d["Kval{}".format(i)] = self._kernel_matrix(data["Xtr{}_mat100".format(i)], data["Xval{}_mat100".format(i)])
            # TODO
            pass
        return d
