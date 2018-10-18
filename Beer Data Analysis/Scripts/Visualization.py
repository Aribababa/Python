import matplotlib.pyplot as plt
import seaborn as sns


# Distribucion de los datos antes de ser procesados
def data_missingness_matrix():
    import pandas as pd
    import missingno as msno

    df = pd.read_csv('../Data/recipeData.csv')
    msno.matrix(df)
    plt.title("Missingness matrix of the data")
    plt.savefig('..\Results\Crafted-beer-missingness-matrix.png')

    return


def data_heatmap():
    import pandas as pd
    import missingno as msno

    df = pd.read_csv('../Data/recipeData.csv')
    msno.heatmap(df)
    plt.savefig('..\Results\Crafted-beer-Heatmap.png')
    return


# Visualizacion de los datos
def beer_count_per_style(histogram_dict, path, limit=20):
    """
        Crea una grafica con el conteo de cervezas por estilo. El resultado se guarda
        en una imagen en la ruta dada.
    """
    import operator

    histogram_dict = sorted(histogram_dict.items(), key=operator.itemgetter(1, 0), reverse=True)
    list_keys, list_values = map(list, zip(*histogram_dict))
    list_keys = list_keys[:limit]
    list_values = list_values[:limit]

    x_pos = [i for i, _ in enumerate(list_keys)]
    plt.style.use('seaborn')
    plt.barh(x_pos, list_values)
    plt.ylabel("Beer")
    plt.xlabel("Beers per style")
    plt.title("Most common styles")

    plt.yticks(x_pos, list_keys)
    plt.gca().invert_yaxis()
    plt.savefig(path)

    return


def percentaje_per_style(histogram_dict, path, limit=10):
    import operator

    histogram_dict = sorted(histogram_dict.items(), key=operator.itemgetter(1, 0), reverse=True)
    list_keys, list_values = map(list, zip(*histogram_dict))

    # lo que esta fuera de los limites se considera como otros, por lo que adaptamos la lista.
    other_values = sum(list_values[limit:])

    # separamos en dos listas
    list_keys = list_keys[:limit]
    list_values = list_values[:limit]

    list_keys.append('Others')
    list_values.append(other_values)

    # Adaptamos los datos para poder graficarlos en la grafica de pastel
    total = float(sum(list_values))
    sizes = [100*(x/total) for x in list_values]

    # Comenzamos a graficar el resultado
    plt.style.use('seaborn')
    _, ax1 = plt.subplots()
    ax1.pie(sizes, labels=list_keys, autopct='%1.1f%%', shadow=True, startangle=0)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.title("Ratio of the styles in the beer data set")
    plt.tight_layout()
    plt.savefig(path)

    return


def data_correlation(dataframe, keys, path):
    """
    Obtiene las graficas de correlacion de los datos sobre los parametros a evaluar.

    :param dataframe: Set de datos con el que evaluara la funcion
    :param keys: lista de los elemntos que se corelacionaran
    :param path: Ruta donde se guardara la imagen
    :return:
    """

    correlation_plot = dataframe.loc[:, keys]
    sns.pairplot(correlation_plot)
    plt.savefig(path)
    return

