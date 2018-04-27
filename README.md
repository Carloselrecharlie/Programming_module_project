# Programming_module_project
Final project about the popular Iris flower data set for the Programming and Scripting module included in the H.D. in Computer Science: Data Analytics by GMIT.

This data set also known as *Fisher's Iris data set* is a multivariate data set introduced by the British statistician and biologist **Ronald Fisher** in his 1936 paper *The use of multiple measurements in taxonomic problems* as an example of linear discriminant analysis. It is sometimes called *Anderson's Iris data set* because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two out of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

<img align="left" width="150" height="170" src="http://s5047.pcdn.co/wp-content/uploads/2015/04/iris_petal_sepal.png">

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

A link with more detailed info about this prominent data set can be found at the end of this readme in References.

## Content
```
This repository contains my first proper data analytics experience. Before anything else I researched for other articles that describe the mentioned data set and this meant my starting point. Some of this information was not harnessed for the level difference but still it gave me ideas and also some knowledge. Shortly, I will include comments from a few of these articles.

There also are three python files:

* data&param.py shows the measures contained in the csv file, which can be found in the *data* folder of this repository. I aimed to dislay it in a clear way and then, there is the code that outputs some statistical parameters that represent the whole file on one hand, and each of the three flower classes separately on the other hand.

* plots.py code which produced my plots.

* mean.py short script where I calculated the mean 
```

## Articles

**1. Basic Analysis of the Iris Data set Using Python**  
In this research, they load and then explore the data with *pandas* using both descriptive statistics and data visualization. After a quick checkout of the data they take boxplots and histograms. Then, through scatterplots they find a diagonal relationship of some pair of attributes, which suggests a high correltaion and a predictable relationship. Then they create a validation set for this dataset by splitting the data into two:
    * 80% to train their models 
    * 20% held back as a dataset

Then they use 10-fold cross validation to estimate accuracy. To evaluate models the ratio of the number of correctly predicted instances in is divided by the total number of instances in the dataset multiplied by 100 to give a percentage (f.i. 97% of accuracy).

After that they test some linear and non-linear algorithms to know which one is the best to take care of the data set. KNN shows better figures. 

The accuracy is 90%. The confusion matrix provides an indication of the three errors made. Finally, the classification report provides a breakdown of each class by precision showing excellent results (granted the validation dataset was small).

**2. Statistical Analysis of the Iris Flower Dataset** 
This study uses two approches, scatterplot graphs and programming to find patterns and draw some conclusions. For the graphs it compares every numerical variable with every classification of flower, giving a different color to each of the three flower classes. This way it is easy to sort the flower varieties from shorter to longer measurements and then, build a predictor for a particular classification
of Iris flowers:
  * If the Iris flower has a long sepal (6-8cm), long petals (5-7cm) and wide petals (1.5-2.5cm) then the Iris is most likely an Iris-Virginica. 
  * If the Iris flower has a short sepal (4.5-5.5cm), short petals(1-2cm) and very narrow petals (.1-.5cm) then the Iris is most likely an Iris-Setosa. 
  * Any Iris flower that falls in between these two classifications is most likely an Iris-Versicolor.
They also make a Java script to get statistical parameters like mean, mode, median, range, variance, standard deviation, minimum value and maximum values.

**3. Python Data Visualizations**

Using 3 libraries in the study (pandas, matplotlib and seaborn) they do things like joinning and summarizing two graphs into a single violin plot, which combines the benefits of a box plot with a layer of spots that shows every measurement. Denser regions of the data are fatter, and sparser thiner in a violin plot

![violinplot](\images\violinPlot.png)[width="150" height="170"]

With another useful seaborn plot, the pairplot, they show the bivariate relation between each pair of features and also that the Iris-setosa species is separataed from the other two across all feature combinations

<img align="center" width="400" height="300" src="https://deeplearning.cms.waikato.ac.nz/img/iris.png">

## References

Source | Link
-------|-----
Wiki intro | https://en.wikipedia.org/wiki/Iris_flower_data_set
Article 1 | https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
Article 2 |  http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf 
Article 3 | https://www.kaggle.com/uciml/iris









=======

Final project about the popular Iris flower data set for the Programming and Scripting module

Based on the combination of the four features shown in the set, Fisher developed a linear discriminant model to distinguish the species from each other.

Statistical Analysis http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf
The goal a this discriminant analysis like this is to produce a simple function that, given the four measurements, will
classify a flower correctly. This is the beginning of creating “predictors” in order to try to make a more educated guess 
on a record in a dataset.

matplotlib.pyplot and plots http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

video scikit-learn https://www.youtube.com/watch?v=hd1W4CyPX58

Basic Analysis of the Iris Data set Using Python https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342 

Python - IRIS Data visualization and explanation https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation 

Iris Data Set, Machine learning,  Install SciPy Libraries https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
