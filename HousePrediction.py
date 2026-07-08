import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("canada_income_dataset.csv")
print(df.head())

print("Printing")
plt.xlabel('year')
plt.ylabel('income US$')
plt.scatter(df.year,df.percapitaincomeUS)
plt.show()

#modeling
regr = linear_model.LinearRegression()
regr.fit(df[['year']],df.percapitaincomeUS)
print(regr.feature_names_in_)

X = pd.DataFrame({'year':[2020]})
print(regr.predict(X))

plt.xlabel('year', fontsize=20)
plt.ylabel('percapitaincomeUS', fontsize=20)
plt.scatter(df.year,df.percapitaincomeUS, color='red')
plt.plot(df.year,regr.predict(df[['year']]),color='blue')
plt.show()