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

# 4. Predict for 2020 and PRINT the result
X = pd.DataFrame({'year':[2020]})
print(regr.predict(X))
print("\n--- Prediction ---")
print(f"Predicted per capita income for X: {regr.predict(X)[0]}")

# 5. Plot the Regression Line
print("\nShowing regression line plot...")
plt.xlabel('year', fontsize=20)
plt.ylabel('percapitaincomeUS', fontsize=20)
plt.scatter(df.year,df.percapitaincomeUS, color='red')
plt.plot(df.year,regr.predict(df[['year']]),color='blue')
plt.show()