# CREDIT-CARD-FRAUD-DETECTION
Built a model that is able to detect fraudulent credit card transactions with high accuracy, recall and F1 score using Scikit-learn in Python.

# Problem statement
The problem statement for this project is to predict fraudulent credit card transactions with the help of machine learning models.

# Business Problem Overview 
Credit card companies play a crucial role in safeguarding consumers from unauthorized charges on their accounts. Detecting fraudulent transactions is paramount in ensuring that customers are not wrongly billed for purchases they did not make.In the banking industry, credit card fraud detection using machine learning is not just a trend but a necessity for them to put proactive monitoring and fraud prevention mechanisms in place. The importance of this task cannot be overstated, and the integration of Data Science and Machine Learning is pivotal in rising to this challenge.It enables these financial institutions to establish proactive monitoring and robust fraud prevention measures. Machine learning plays a pivotal role in curtailing the need for labor-intensive manual reviews, mitigating the expenses associated with chargebacks and fees, and preventing the rejection of legitimate transactions."

# Data Dictionary
The dataset can be download using this [link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the fraud transactions account for 0.172% of all transactions.
The data set has also been modified with Principal Component Analysis (PCA) to maintain confidentiality. Apart from ‘time’ and ‘amount’, all the other features (V1, V2, V3, up to V28) are the principal components obtained using PCA. The feature 'time' contains the seconds elapsed between the first transaction in the data set and the subsequent transactions. The feature 'amount' is the transaction amount. The feature 'class' represents class labelling, and it takes the value 1 in cases of fraud and 0 in others.

# Project Pipeline
Following are the steps taken to achieve the objective of the project:

**Loading the Data/ ETL:** A python script has been written to mock the actual ETL. The data is *Extracted* from a source(abouve mentioned link in this case and then minor operations has been perfoemed on the data to show the concepts of *Transformtion* and fillaly data is *Loaded* to another location. The IDE used is PyCharm to create the python scrpt and file is uploaded in this repository. 

**UNderstanding the Data:** The .py file is then called in jupyter notebook to understand the data features.This would help us choose the features that we will need for your final model.

**Exploratory data analytics (EDA)**: we need to perform univariate and bivariate analyses of the data, followed by feature transformations, if necessary. This

**Train/Test Split:** Performing train/test split in order to check the performance of our models with unseen data. Here, for validation and using heatmap for validation

**Model-Building:** This is the final step at which we can try different models and fine-tune their hyperparameters until we get the desired level of performance on the given dataset. We should try and see if we get a better model by the various sampling techniques.

**Model Evaluation:** evaluate the models using appropriate evaluation metrics. Note that since the data is imbalanced it is is more important to identify which are fraudulent transactions accurately than the non-fraudulent. We need to choose an appropriate evaluation metric which reflects this business goal.
