# Insurance Cost Prediction

A Machine Learning project that predicts medical insurance charges based on personal and health-related information.
https://insurancepredictionmodel-8flh8cjpxp8go8hcuzomxr.streamlit.app/

## Project Overview

This project uses a Random Forest Regressor to predict insurance costs.

The model takes the following features as input:

- Age
- Sex
- BMI
- Number of Children
- Smoking Status
- Region

## Dataset

The project uses the `insurance.csv` dataset containing 1338 records.

### Features

| Feature | Description |
|---|---|
| age | Age of the person |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of children |
| smoker | Smoking status |
| region | Residential region |
| charges | Medical insurance cost |

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest
- Streamlit

## Machine Learning

Two regression models were tested:

### Linear Regression

- MAE: 4186.51
- RMSE: 5799.59
- R² Score: 0.7833

### Random Forest Regressor

- MAE: 2531.06
- RMSE: 4593.06
- R² Score: 0.8641

Random Forest performed better, so it was selected as the final model.

## Feature Importance

The most important features were:

1. Smoker - 60.9%
2. BMI - 21.6%
3. Age - 13.5%
4. Children - 2.0%
5. Region - 1.4%
6. Sex - 0.6%

Smoking status had the largest impact on the predicted insurance charges.

## Example Prediction

For a person with:

- Age: 30
- Sex: Male
- BMI: 25
- Children: 2
- Smoker: Yes
- Region: 2

The model predicted approximately:

**$18,886.68**

## Project Structure

```text
Insurance/
│
├── insurance.csv
├── insurance_model.pkl
├── main.py
├── requirements.txt
└── README.md
