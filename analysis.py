# This is analysis of Iris data set using python as pands2021 module assesment
# Author: Mantvydas Jokubaitis

# Importing packages to be used
import pandas as pd
import numpy as np

irissrc = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Reading data from url, adding column names and saving to csv
iris = pd.read_csv(irissrc, sep=',', names=["sepallength", "sepalwidth", "petallength", "petalwidth", "species"])
iris.to_csv('iris.csv')

# Creating 15 instances data sample and confirming value counts by species, checking for NAs
na = iris.isnull().sum()
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
print(descr1)