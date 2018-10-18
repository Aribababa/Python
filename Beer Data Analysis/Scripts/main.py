from FileCreator import ExcelReport
from Database import MongoDatabase
import Visualization
import Processing
import pandas as pd

CRAFTED_BEER_SETS = 72  # Numero de colecciones que se van a evaluar


def main():
    beer_dataframe = []  # Dataframe de la mustra

    crafted_beer_db = MongoDatabase('mongodb://localhost:27017/', 'Crafted-Brewery-Database')
    style_histogram = {}

    for i in range(0, CRAFTED_BEER_SETS):
        retrieved_data = crafted_beer_db.fetch_collection('Crafted-Brewery-Beers-' + str(i))
        beer_dataframe.extend(retrieved_data)

        # Ranking de los estilos de cerveza mas comunes
        style_histogram = Processing.data_histogram(retrieved_data, 'Style', histogram=style_histogram)

    style_histogram.pop("N/A")

    # Con todos los datos listos, pasamos a un Dataframe para facilitar la visualizacion
    import seaborn as sns
    import matplotlib.pyplot as plt

    beer_dataframe = pd.DataFrame(beer_dataframe)
    pairplot = beer_dataframe.loc[:, ['ABV', 'IBU']]

    sns.pairplot(pairplot)
    plt.savefig('..\Results\Crafted-beer-correlation-pairplot.png')
    return


if __name__ == '__main__':
    main()
