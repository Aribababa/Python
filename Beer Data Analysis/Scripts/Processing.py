import numpy as np


""""
    Algunas funciones paar el procesamiento y visualizacion de los datos.
"""


def data_average(data_dictionary, key, prev_avg=0):
    """"
    Obtiene la media de los datos. Se puede encadenar los datos para
    realizar un promedio en forma de cascada.
    """
    avg = 0
    for data in data_dictionary:
        avg += data[u''+key]

    if prev_avg:
        avg = avg / len(data_dictionary)
    else:
        avg = avg / len(data_dictionary)
        avg = (avg + prev_avg)/2
    return avg


def data_std_dev(data_dictionary, key, prev_std=0):
    """"
       Obtiene la desviacion estandar de los datos.
    """
    standard_deviation = []
    for data in data_dictionary:
        standard_deviation.append(data[key])

    try:
        standard_deviation = np.std(standard_deviation)
    except TypeError:
        return 0
    if not prev_std:
        standard_deviation = (standard_deviation + prev_std)/2
    return standard_deviation


def data_histogram(data_dictionary, key, histogram={}):

    for data in data_dictionary:
        data = data[key]
        histogram[data] = histogram.get(data, 0) + 1
    return histogram


