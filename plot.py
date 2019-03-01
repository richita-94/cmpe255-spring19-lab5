from collections import Counter

from linear_algebra import distance

from statistics import mean

import math, random

from knn import knn_classify

import matplotlib.pyplot as plt

from data import cities



def plot_state_borders(plt, color='0.8'):

    pass

def plot_cities(cities):

    # key is language, value is pair (longitudes, latitudes)

    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

    # we want each language to have a different marker and color

    markers = { "Java" : "o", "Python" : "s", "R" : "^" }

    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

    for (longitude, latitude), language in cities:

        plots[language][0].append(longitude)

        plots[language][1].append(latitude)

    

    # create a scatter series for each language

    for language, (x, y) in plots.items():

        plt.scatter(x, y, color=colors[language], marker=markers[language],

                          label=language, zorder=10)

    plot_state_borders(plt)    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location

    plt.axis([-130,-60,20,55]) # set the axes

    plt.title("Favorite Programming Languages")

    plt.show()

def classify_and_plot_grid(cities, k=1):

    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }

    # we want each language to have a different marker and color

    markers = { "Java" : "o", "Python" : "s", "R" : "^" }

    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }
    for i in range(-130,-60):
        for j in range (20,55):
            lang = knn_classify(k,cities,[i,j])
            plots[lang][0].append(i)
            plots[lang][1].append(j)
        
    for lang, (i, j) in plots.items():

        plt.scatter(i, j, color=colors[lang], marker=markers[lang],

                          label=lang, zorder=0)



    plot_state_borders(plt, color='black')    # assume we have a function that does this

    plt.legend(loc=0)          # let matplotlib choose the location

    plt.axis([-130,-60,20,55]) # set the axes

    plt.title(str(k) + "-Nearest Neighbor Programming Languages")

    plt.show()


    """

    TODO

    Classify and plot for Python, Java, and R languages.

    """



    # Predict preferred language for each city using knn_classify() from knn.py.

    # longitude range (-130, -60)

    # latitude in range (20, 55)

    # Save the coordinate of prediction result in plots variable.

    # TODO



    # create a scatter series for each language

    # See above plot_cities() to plot your prediction.

    # TODO





if __name__ == "__main__":

    # TODO import cities from data.py

    # cities = []

    plot_cities(cities)

    classify_and_plot_grid(cities)

    classify_and_plot_grid(cities, 3)

    classify_and_plot_grid(cities, 5)

    