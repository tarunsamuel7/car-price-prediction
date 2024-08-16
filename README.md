# CAR PRICE PREDICTION

Project Overview: 
This project focuses on building a machine learning model that can accurately predict the selling price of a car based on various features such as mileage, year, make, model, and location. The final output is a cloud-deployed application that provides users with valuable insights and price predictions.

Dataset: 
The dataset contains 852,122 rows and 8 columns. Key features include:

Price (Target Variable): The car's selling price.
Year: The manufacturing year of the car.
Mileage: Total distance traveled by the car (in kilometers).
City: The city where the car was sold.
State: The state where the car was sold.
VIN: Vehicle Identification Number (unique to each car).
Make: Manufacturer of the car (e.g., Toyota, Ford, Honda).
Model: Specific model of the car.

Data Exploration and Preparation: 
Initial Exploration: The dataset was inspected for missing values, data types, and high cardinality features.
Data Cleaning: Duplicate rows based on VIN and Year were removed, reducing the dataset to 800,000 rows.
Visualization: Various plots such as histograms, scatter plots, and heatmaps were created to understand data distributions and relationships.

Feature Engineering: 
Car Age: Calculated as 2024 - Year.
Mileage_Age_Interaction: Interaction term created by multiplying Mileage and Car Age.
Log_Price: Applied log transformation to the Price variable to reduce skewness.

Model Selection and Tuning: 
Model: A Decision Tree Regressor was selected for its ability to model non-linear relationships.
Hyperparameter Tuning: GridSearchCV was used to find the best combination of parameters:
max_depth: 20
min_samples_split: 5
min_samples_leaf: 2
max_features: 'sqrt'
Model Evaluation
The model was evaluated on the test set using the following metrics:

RMSE: 5,328 units
MAE: 3,500 units
R² Score: 0.72
These metrics indicate that the model explains 72% of the variance in the target variable.

Visualization and Insights:

Car Price Distribution: The prices are right-skewed, with most cars priced under 30,000 units.
Correlation Analysis: Price has a moderate positive correlation with Year and a moderate negative correlation with Mileage.
Market Segmentation: Luxury brands dominate the high-price segment, while economy brands occupy the lower end.
Deployment
The final model is deployed on a cloud platform, accessible via a web-based interface that allows users to input car details and receive price predictions.

Conclusions and Recommendations: 
Feature Importance: Mileage and Year are the most critical features influencing car prices.
Market Trends: The market shows a clear preference for newer, lower-mileage cars.
User Recommendations:
Buyers: Focus on newer, low-mileage vehicles.
Sellers: Highlight the car's age and mileage in listings to attract buyers.

streamlit Link: https://car-price-prediction-nrrj2dzcwnzhj8jmygenqy.streamlit.app/ 
