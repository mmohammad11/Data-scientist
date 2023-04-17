# Disaster Response Pipeline,ETL,ML

## Table for Contents
1. [installation](https://github.com/mmohammad11/project1/edit/main/README.md#installation)
2. [Motivation](https://github.com/mmohammad11/project1/edit/main/README.md#motivation)
3. [File Describtion](https://github.com/mmohammad11/project1/edit/main/README.md#file-describtion)
4. [Requirements](https://github.com/mmohammad11/project1/edit/main/README.md#requirements)
5. [Licensing](https://github.com/mmohammad11/project1/edit/main/README.md#licensing)

### Installation
1. numpy
2. Pandas
3. Json
4. Nltk
5. Sklearn
6. Sqlalchemy
7. Sys
8. Re
9. Pickle

### Motivation

In this project, I put all my data engineering skills to build a model for an API and analyze disaster data from [Figure Eight](https://appen.com). I'll repair this data with an ETL pipeline and then use a Machine Learning Pipeline to build a supervised learning model.    

### File Describtion

App
* template
* go.html
* master.html
* run.py

Data
* disaster_categories.csv
* disaster_massages.csv
* process_data.py

Models
* classifier.pkl
* train_classifier.py

README.md

### Requirements

1. ETL pipeline Preparation
Follows ETL proccess that incloud:
* load messages and categories datasets
* merge the datasets
* clean the datasets
* drop duplicates
* save it in a sqlite database

2. ML pipeline preparation
writes a ML pipeline that:
* load the dataset from sqlite database
* write tokenize function
* build the pipeline model
* train a model using GridSearchCV
* save the final model as a pickle file

3. Wep app 
The wep app will extract data from database to provide data visulization, and use the model to classify new messages for 36 categories. The output are:

<img src=""

### Licensing
