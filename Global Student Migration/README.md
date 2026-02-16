## Project Overview and Problem Statement
- Analyze global international student migration patterns using predictive analytics.
- Forecast annual student migration volumes between origin and destination countries.
- Identify key drivers influencing migration decisions, including financial aid, academic readiness, and career outcomes.
- Evaluate the impact of global disruptions (e.g., COVID‑19) on forecasting accuracy and model stability.

## Data Sources and Datasets Used
- Global Student Migration dataset with approximately 5,000 records and 20 variables.
- Student‑level data aggregated by origin country, destination country, and year.
- Key features include scholarship rate, placement rate, GPA, test scores, and enrollment year.

## Analytical and Predictive Methods Applied
- Exploratory Data Analysis (EDA) to understand trends, distributions, and relationships.
- Feature engineering with aggregation, label encoding, and MinMax scaling.
- Predictive modeling using:
  - Ridge Regression (baseline linear model)
  - Random Forest Regressor
  - XGBoost Regressor
- Chronological train–test splits to simulate real‑world forecasting.
- Model evaluation using MAE, RMSE, and MAPE metrics.

## Key Findings or Outcomes
- Random Forest consistently delivered the best overall forecasting performance.
- XGBoost provided comparable accuracy and valuable feature‑importance insights.
- Scholarship rate and placement rate were the strongest predictors of student migration.
- Academic indicators (GPA and test scores) were more influential than country‑level factors.
- Models trained with pandemic‑era data showed improved robustness and lower error rates.

## Tools and Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit‑learn, Matplotlib, Seaborn, XGBoost
- **Environment:** Jupyter Notebook
- **Techniques:** Regression, ensemble learning, feature scaling, cross‑validation

## Future Enhancements or Next Steps
- Incorporate policy and macroeconomic variables (visa rules, GDP, inflation).
- Explore time‑series and deep learning models for improved trend capture.
- Improve forecasting for low‑volume countries using hierarchical or Bayesian approaches.
- Develop scenario‑based simulations to support institutional and policy planning.
