# Disaster Response Pipeline,ETL,ML

## Table for Contents
1. [installation](#installation)
2. [Motivation](#motivation)
3. [File Describtion](#file-describtion)
4. [Requirements](#requirements)
5. [Licensing](#licensing)

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

<img src="https://user-images.githubusercontent.com/122842788/232374746-5bfebfae-721c-4ecc-af6b-6a1b28f73504.png">
<img src="https://user-images.githubusercontent.com/122842788/232374890-064bf883-f951-49fc-9427-599117f9b1d9.png">
<img src="https://user-images.githubusercontent.com/122842788/232375018-4025c471-04ee-47a2-93f1-2cfcc6d5500c.png">
<img src="https://user-images.githubusercontent.com/122842788/232375080-ddbcc9dc-53f6-43ea-8d07-65a9ece7f765.png">

### How to run the web app

1. Run ETL pipeline that clean and save the data in database `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
2. To run ML pipeline that trains classifier and saves `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
3. Run web app: `python run.py` in app dicrectory
4. open this link (http://0.0.0.0:3000/)

### Licensing
This project was completed as a part of the Udacity data scientist nanodegree. 
