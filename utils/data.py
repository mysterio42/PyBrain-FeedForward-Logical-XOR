from pybrain.datasets import supervised


def xor_data():
    data = supervised.SupervisedDataSet(2, 1)

    data.addSample((0, 0), (1))
    data.addSample((1, 0), (0))
    data.addSample((0, 1), (0))
    data.addSample((1, 1), (1))

    return data
