# 💼 Salary Prediction Model

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white&style=flat-square) 
![Flask](https://img.shields.io/badge/Flask-2.x-orange.svg?logo=flask&logoColor=white&style=flat-square)
![Heroku](https://img.shields.io/badge/Deployment-Heroku-purple?style=flat-square&logo=heroku) 

## 🎯 Project Overview  
This **Salary Prediction Model** predicts employee salaries based on their **years of experience** using **OLS Regression**. Users can input their experience in a web interface built with **Flask** and receive the predicted salary.  
Deployed on **Heroku** for easy access.

🔗 **Live Demo**: [Check out the deployment on Heroku](https://your-heroku-app.herokuapp.com)

---

## 🛠️ Features  
- 🌐 **Interactive Web Interface**  
- 📈 **OLS Regression Model** for predictions  
- 🎯 **Real-time Salary Predictions**  
- 🚀 **Heroku Deployment** for seamless access  

---

## 📁 Dataset  
The dataset used:  
- **`yoe`**: Years of Experience  
- **`salary`**: Corresponding Salary  

---

## 🧩 How It Works  
1. User inputs the **years of experience** into the form.
2. The input is processed by the **OLS regression model**.
3. The **predicted salary** is displayed on the web page.

---

## 💻 Code Overview

### **Python Code (Model Logic)**
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from statsmodels.formula.api import ols

def salary_prediction(experience):
    df = pd.read_csv('Salary_dataset.csv')
    ols_formula = "salary ~ yoe"
    model = ols(formula=ols_formula, data=df).fit()
    pred = model.predict(pd.DataFrame({'yoe': [experience]})).to_numpy()[0]
    return pred
