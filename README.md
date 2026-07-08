# Canada Per Capita Income Predictor 📈

A simple Machine Learning project that uses **Linear Regression** to predict Canada's future per capita income based on historical data ranging from 1970 onwards. This project utilizes Python, `scikit-learn` for modeling, `pandas` for data manipulation, and `matplotlib` for data visualization.

## 🚀 Features
* **Data Visualization:** Plots historical data points to observe the income growth trend.
* **Predictive Modeling:** Fits a linear regression model to map out the best-fit trend line.
* **Future Forecasts:** Predicts per capita income for any target year (e.g., 2020).
* **Clean Code Structure:** Avoids common `scikit-learn` alignment warnings by preserving feature names during prediction.

---

## 📊 Dataset
The project relies on a dataset named `canada_income_dataset.csv`. It contains two primary columns:
* `year`: The calendar year of the recorded data.
* `percapitaincomeUS`: The corresponding per capita income in USD.

### Sample Data
| year | percapitaincomeUS |
| :--- | :---------------- |
| 1970 | 3399.299037       |
| 1971 | 3768.297935       |
| 1972 | 4251.175484       |

---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have Python installed on your system. You will also need the following libraries:
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`

### Step 1: Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
