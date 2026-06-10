# hands on project: EDA on a sample dataset
# use this link: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Task 1: perform data cleaning, aggregation and filtering

# load the dataset
url='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# inspection
# print(df.info())
# print(df.describe())

# Handling missing data
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop(columns=["Cabin"], inplace=True)

# remove duplicate
df = df.drop_duplicates()

# print(df)

# first class data - 5 row
first_class = df[df["Pclass"] == 1].head().iloc[:,:3]
# print("First Class: \n", first_class)

# second class data - 5 row
second_class = df[df["Pclass"] == 2].head().iloc[:,:3]
# print("Second Class: \n", second_class)
# Generate Visualizations to Illustrate key insights - name, ticket
# line-plot
# plt.plot(second_class["PassengerId"], second_class["Survived"], color='blue', label='first and second class trend')
# plt.title("First And Second Class Line Plot")
# plt.legend()
# plt.show()

# bar graph
# plt.bar(first_class["PassengerId"], first_class["Survived"], label="Name-Age-trend", color="blue", edgecolor="red")
# plt.title("Name-Age-Graph")
# plt.show()

# histo graph
# plt.hist(first_class["Survived"], label="Histograph", bins=10, color='Green')
# plt.title("First Class Titanic Survived Distribution")
# plt.xlabel("Survived Dis")
# plt.ylabel("Frequency Dis")
# plt.show()

# scatter plot
plt.scatter(df["Age"], df["Fare"], edgecolor="white", color='blue', alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
