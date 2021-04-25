# This is analysis of Iris data set using python as pands2021 module assesment
# Author: Mantvydas Jokubaitis

# Importing packages to be used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

irissrc = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Reading data from url, adding column names and saving to csv
iris = pd.read_csv(irissrc, sep=',', names=["sepallength", "sepalwidth", "petallength", "petalwidth", "species"])
iris.to_csv('iris.csv')

# Checking data shape, missing data, sample size of 15, value counts by species
shape = np.shape(iris)
na = iris.isnull().sum()
head = iris.head(10) 
sample = iris.sample(15)
counts = iris["species"].value_counts()

# Slicing data by species for group statistics
setosa = iris.loc[iris["species"] == "Iris-setosa"]
virginica = iris.loc[iris["species"] == "Iris-virginica"]
versicolor = iris.loc[iris["species"] == "Iris-versicolor"]

# Descriptive statistics including min, max, mean and standard deviation
descr1 = pd.DataFrame(setosa).describe()
descr2 = pd.DataFrame(virginica).describe()
descr3 = pd.DataFrame(versicolor).describe()

# Output to summary text file:
with open("summary.txt", "a+") as f:
    f.write("\n\t This file provides summary of Iris dataset analysis \n\n")
    f.write("Dataset shape is (lines, columns): \n{}\n\n".format(shape))
    f.write("Check for any missing values: \n{}\n\n".format(na))
    f.write("Top of dataset: \n{}\n\n".format(head))
    f.write("Data sample of 15 instances: \n{} \n\n".format(sample))
    f.write("\n\n\t Decriptive statistics by Iris flower species: \n\n")
    f.write("Setosa:\n{}\n\n".format(descr1))
    f.write("Virginica:\n{}\n\n".format(descr2))
    f.write("Versicolor:\n{}\n\n".format(descr3))

# Plots 
#sns

# Saving plots

#plt.show()
#plt.savefig("plot_name.png")
print("ALL works ook")