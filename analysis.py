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
    f.write("Counts of observations per species: \n{} \n\n".format(counts))
    f.write("\n\n\t Decriptive statistics by Iris flower species: \n\n")
    f.write("Setosa:\n{}\n\n".format(descr1))
    f.write("Virginica:\n{}\n\n".format(descr2))
    f.write("Versicolor:\n{}\n\n".format(descr3))

# Plots

# Simple Histogram
iris.hist()
plt.savefig("1simple_histogram.png")

#Histogram by Specie
sns.set_theme(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(5, 5))
fig.suptitle('Setosa Histograms')
sns.histplot(data=setosa, x="sepallength", kde=False, color="blue", ax=axs[0, 0])
sns.histplot(data=setosa, x="sepalwidth", kde=False, color="pink", ax=axs[0, 1])
sns.histplot(data=setosa, x="petallength", kde=False, color="green", ax=axs[1, 0])
sns.histplot(data=setosa, x="petalwidth", kde=False, color="brown", ax=axs[1, 1])
plt.tight_layout()
plt.savefig("2setosa_histogram.png")

sns.set_theme(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(5, 5))
fig.suptitle('Versicolor Histograms')
sns.histplot(data=versicolor, x="sepallength", kde=False, color="y", ax=axs[0, 0])
sns.histplot(data=versicolor, x="sepalwidth", kde=False, color="g", ax=axs[0, 1])
sns.histplot(data=versicolor, x="petallength", kde=False, color="gray", ax=axs[1, 0])
sns.histplot(data=versicolor, x="petalwidth", kde=False, color="magenta", ax=axs[1, 1])
plt.tight_layout()
plt.savefig("3versicolor_histogram.png")

sns.set_theme(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(5, 5))
fig.suptitle('Virginica Histograms')
sns.histplot(data=virginica, x="sepallength", kde=False, color="teal", ax=axs[0, 0])
sns.histplot(data=virginica, x="sepalwidth", kde=False, color="gray", ax=axs[0, 1])
sns.histplot(data=virginica, x="petallength", kde=False, color="yellow", ax=axs[1, 0])
sns.histplot(data=virginica, x="petalwidth", kde=False, color="m", ax=axs[1, 1])
plt.tight_layout()
plt.savefig("4virginica_histogram.png")
plt.show()

#Iris relationship pair plot by species with histogram
sns.set_theme(style="white")
p=sns.pairplot(iris, hue="species", height=2)
p.map_diag(sns.histplot)
p.map_offdiag(sns.scatterplot)
plt.savefig("5pairplot_histogram.png")
plt.show()

#Scatterplots by species
plt.title("Sepal lenght and width comparison by species")
sns.set_theme(style="white")
sns.scatterplot(x=iris["sepallength"], y=iris["sepalwidth"], hue=iris["species"],s=50)
plt.savefig("6scatterplot1.png")
plt.show()

plt.title("Petal lenght and width comparison by species")
sns.set_theme(style="white")
sns.scatterplot(x=iris["petallength"], y=iris["petalwidth"], hue=iris["species"],s=50)
plt.savefig("7scatterplot2.png")
plt.show()

#Multivariable plots for comparison
sns.set_theme(style="white")
sns.distplot(setosa['sepallength'], color='green', kde=True, label='Setosa')
sns.distplot(versicolor['sepallength'], color='blue', kde=True, label='Versicolor')
sns.distplot(virginica['sepallength'], color='red', kde=True, label='Virginica')
plt.legend()
plt.title('Sepal Length Comparson by Species')
plt.xlabel('Sepal Length in cm')  
plt.ylabel('Quantity')
plt.savefig("8multivariable1.png")
plt.show()

sns.set_theme(style="white")
sns.distplot(setosa['sepalwidth'], color='green', kde=True, label='Setosa')
sns.distplot(versicolor['sepalwidth'], color='blue', kde=True, label='Versicolor')
sns.distplot(virginica['sepalwidth'], color='red', kde=True, label='Virginica')
plt.legend()
plt.title('Sepal Width Comparson by Species')
plt.xlabel('Sepal Width in cm')  
plt.ylabel('Quantity')
plt.savefig("9multivariable2.png")
plt.show()

sns.set_theme(style="white")
sns.distplot(setosa['petallength'], color='green', kde=True, label='Setosa')
sns.distplot(versicolor['petallength'], color='blue', kde=True, label='Versicolor')
sns.distplot(virginica['petallength'], color='red', kde=True, label='Virginica')
plt.legend()
plt.title('Petal Length Comparson by Species')
plt.xlabel('Petal Length in cm')  
plt.ylabel('Quantity')
plt.savefig("10multivariable3.png")
plt.show()

sns.set_theme(style="white")
sns.distplot(setosa['petalwidth'], color='green', kde=True, label='Setosa')
sns.distplot(versicolor['petalwidth'], color='blue', kde=True, label='Versicolor')
sns.distplot(virginica['petalwidth'], color='red', kde=True, label='Virginica')
plt.legend()
plt.title('Petal width Comparson by Species')
plt.xlabel('Petal width in cm')  
plt.ylabel('Quantity')
plt.savefig("11multivariable4.png")
plt.show()

print("Hooray")