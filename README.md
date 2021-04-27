<p># pands-project2021</p>
<h2 style="text-align: center;">GMIT Programming and Scripting 2021 Project</h2>
<h2 style="text-align: center;">This depository contains Iris dataset analysis using Python.</h2>
<h4>Student: Mantvydas Jokubaitis</h4>
<p>Summary: Iris flower data set is a multivariable data set collected by Sir Ronald Aylmer Fisher and published in journal article &apos;The Use of Multiple Measurements in Taxonomic Problems.&apos; in Annals of Eugenics, 7 in 1936. Data set contain biological data of Iris flower and is divided by species into Iris setosa, Iris virginica and Iris versicolor.</p>
<p>Dataset contains 150 observations altogether, 50 observations for each species. Features include length and width of sepal and petal, also Iris species name.</p>


<img src="https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/tim-russmann-hws29QtFM3U-unsplash.jpg" width="250"/> <img src="https://www.fs.fed.us/wildflowers/beauty/iris/images/flower/blueflagiris_flower_lg.jpg" width="250"/> <img src="https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/dmitry-stepanov-o7zBtfqfxxo-unsplash.jpg" width="250"/>


Photo by <a href="https://unsplash.com/@timaesthetic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Tim Rüßmann</a> on <a href="https://unsplash.com/s/photos/iris-flower?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@stepanovgg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dmitry Stepanov</a> on <a href="https://unsplash.com/s/photos/iris-flower?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

<p>Analysis of this dataset will be performed using Python, that is a powerful high level programming language. Various Python packages will be used to explore and summarize the findings.&nbsp;</p>
<p>Dataset is available to be downloaded from UCI Machine Learning Repository. It contains two files, one for data and one for dataset description.</p>
<p>For this project Python 3.8.5 is being used with Anaconda package for data analysis.</p>
<p>To start the analysis we load required packages: Pandas, Numpy, Matplotlib.pyplot and Seaborn.</p>

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
<p>We are using Pandas to download Iris flower dataset from UCI Machine Learning depository. &nbsp;After overview of data column names are added and it is saved in CSV format in the working directory.</p>
<p>To get familiar with dataset we check data shape, count missing values and look at top ten lines:</p>

```python
shape = np.shape(iris)
na = iris.isnull().sum()
head = iris.head(10) 
sample = iris.sample(15)
counts = iris["species"].value_counts()
```
<p>Results of the code displaying shape of data, missing values count and top of dataset:</p>

![Data shape, missing values count and top of dataset](https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/1.PNG) 

<p>Also, sample of 15 instances:</p>

![A sample of 15 instances](https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/2.PNG)

<p>To get descriptive statistics by flower species we divide dataset into 3 sections:</p>

```python
descr1 = pd.DataFrame(setosa).describe()
descr2 = pd.DataFrame(virginica).describe()
descr3 = pd.DataFrame(versicolor).describe()
```
![Descriptive statistics by flower species](https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/3.PNG)


<p>All the data generated so far is being saved into a summary.txt file in an append mode:</p>

```python
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
```

# Plotting
<p>For plotting we are using matplotlib.pyplot and seaborn with seaborn having a nicer look all together without extensive tweaking of code.</p>

![Simple histogram](https://github.com/Mantvydas-data/pands-project2021/blob/main/1simple_histogram.png)


![Setosa histogram](https://github.com/Mantvydas-data/pands-project2021/blob/main/2setosa_histogram.png)
![Versicolor histogram](https://github.com/Mantvydas-data/pands-project2021/blob/main/3versicolor_histogram.png)
![Virginica histogram](https://github.com/Mantvydas-data/pands-project2021/blob/main/4virginica_histogram.png)

![Pairplot with histograms](https://github.com/Mantvydas-data/pands-project2021/blob/main/5pairplot_histogram.png)

![Scatterplot1](https://github.com/Mantvydas-data/pands-project2021/blob/main/6scatterplot1.png)
![Scatterplot2](https://github.com/Mantvydas-data/pands-project2021/blob/main/7scatterplot2.png)


![Multivariable1](https://github.com/Mantvydas-data/pands-project2021/blob/main/8multivariable1.png) ![Multivariable2](https://github.com/Mantvydas-data/pands-project2021/blob/main/9multivariable2.png)
![Multivariable3](https://github.com/Mantvydas-data/pands-project2021/blob/main/10multivariable3.png) ![Multivariable4](https://github.com/Mantvydas-data/pands-project2021/blob/main/11multivariable4.png)

<h3>References of sources used:</h3>
<p>https://en.wikipedia.org/wiki/Iris_flower_data_set</p>
<p>https://www.w3schools.com/html/html_paragraphs.asp</p>
<p>https://archive.ics.uci.edu/ml/datasets/Iris</p>
<p>https://gist.github.com/curran/a08a1080b88344b0c8a7</p>
<p>https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/</p>
<p>https://www.guru99.com/reading-and-writing-files-in-python.html</p>
<p>https://www.w3schools.com/python/python_ref_functions.asp</p>
<p>https://ourcodingclub.github.io/tutorials/pandas-python-intro/</p>
<p>https://www.w3schools.com/python/python_strings_escape.asp</p>
<p>https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/</p>
<p>https://machinelearningmastery.com/machine-learning-in-python-step-by-step/</p>
<p>https://seaborn.pydata.org/examples/index.html</p>
<p>https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8</p>
<p>https://www.markdownguide.org/basic-syntax/</p>
