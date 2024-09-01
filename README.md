# Predicting Arrests in Terry Traffic Stops
![alt text](Images/ohio%20police%20stop.jpg)

## Project Overview
This project aims to develop predictive models to determine the likelihood of an arrest during Terry Traffic Stops, a procedure used by law enforcement in the United States. By analyzing various factors, such as stop resolution, perceived race, perceived gender, and age group, the project provides valuable insights to help law enforcement agencies optimize their strategies and improve community policing efforts.

## Business Understanding
The primary goal of this project is to predict the likelihood of an arrest during a traffic stop, which is valuable for stakeholders such as law enforcement agencies, policymakers, and community organizations. Understanding the factors that lead to arrests can help:
* *Law Enforcement:* Allocate resources more effectively and make data-driven decisions to enhance public safety.
* *Community Organizations:* Advocate for equitable treatment and highlight areas where improvements are needed.
* *Policymakers:* Formulate policies that ensure fair and unbiased policing.

## Data Understanding
* *Data Source:* The dataset used in this project is sourced from public records on [Terry Traffic Stops](https://data.seattle.gov/Public-Safety/Terry-Stops/28ny-9ts8/about_data), which include various features such as Subject Age Group, Subject Perceived Race, Stop Resolution, and others.
* *Data Properties:* The data contains categorical and numerical attributes that represent various characteristics of each traffic stop. The key variable of interest is the Arrest Flag, which indicates whether an arrest was made.

## Data Preparation
* *Data Cleaning:* Missing values were handled by dropping columns with missing data and did not have much influence on the arrest.
* *Feature Engineering:* I selected relevant features based on domain knowledge and their potential influence on the likelihood of an arrest.
* *Encoding:* I encoded categorical features using one-hot encoding to convert them into a numerical format suitable for model training.
* *Feature Scaling:* I standardized Numerical features to ensure consistent model performance, particularly for models sensitive to feature scaling.

## Exploratory Data Analysis (EDA)
*Visualizations:* I created the following visualizations to understand the data distribution and relationships between features:
* *Count Plots:* For categorical features like Stop Resolution, Subject Perceived Race, Subject Perceived Gender, and Subject Age Group.
* *Feature Importance:* For Decision Tree model to identify the most influential features.

## Modelling
*Models Used:* 
* Logistic Regression: Chosen for its simplicity and interpretability.
* Decision Tree: Selected for its ability to capture non-linear relationships in the data.
*Hyperparameter Tuning:*
* Employed Grid Search for hyperparameter tuning on the Decision Tree model to optimize its performance.
*Cross-Validation:*
* Conducted 5-fold cross-validation to evaluate the robustness of both models across different data subsets, ensuring generalizable results.
## Evaluation

*Performance Metrics: Both models were evaluated using:*

* *Accuracy:* Overall correctness of predictions.
* *Precision and Recall:* To assess the balance between false positives and false negatives.
* *F1-Score:* To provide a single metric combining both precision and recall.
* *ROC-AUC:* Area Under the Curve to evaluate the model's discriminative ability.

*Final Model Selection: The Decision Tree model was selected as the final model due to its superior performance in recall and its ability to provide interpretable rules, despite Logistic Regression providing a more balanced precision.*

## Results and Interpretation

*Key Findings:*
* The Decision Tree model identified 'Stop Resolution' and 'Subject Perceived Race' as critical predictors of an arrest during a traffic stop.
* Logistic Regression showed that linear relationships between variables could still provide substantial insights, though with some limitations in capturing non-linear dynamics.

*Model Limitations:* Both models showed limitations with imbalanced classes, which affected recall and precision metrics. Future improvements could include using balancing techniques or acquiring more balanced datasets.

## Visualization of Results
*Linear Regression Confusion Matrix*
![alt text](Images/LR%20COR.png)

*True Negative (TN): 10,696*
* This is the number of instances where the actual class was "No Arrest" (No) and the model correctly predicted "No Arrest" (No).

*False Positive (FP): 225*
* This is the number of instances where the actual class was "No Arrest" (No) but the model incorrectly predicted "Arrest" (Yes).

*False Negative (FN): 1,087*
* This is the number of instances where the actual class was "Arrest" (Yes) but the model incorrectly predicted "No Arrest" (No).

*True Positive (TP): 202*
* This is the number of instances where the actual class was "Arrest" (Yes) and the model correctly predicted "Arrest" (Yes).

The model has a high accuracy and specificity, indicating it is good at identifying the "No Arrest" class correctly. However, the model has low precision and recall for the "Arrest" class. This suggests that the model is not very effective at predicting the "Arrest" class. It misses many actual "Arrest" cases (low recall) and has a relatively high rate of false positives when it does predict "Arrest" (low precision).


*Decision Tree Confusion Matrix*
![alt text](Images/dt%20con.png)

True Negative (TN): 10,000
The number of instances where the actual class was "No Arrest" (No) and the model correctly predicted "No Arrest" (No).

False Positive (FP): 429
The number of instances where the actual class was "No Arrest" (No), but the model incorrectly predicted "Arrest" (Yes).

False Negative (FN): 775
The number of instances where the actual class was "Arrest" (Yes), but the model incorrectly predicted "No Arrest" (No).

True Positive (TP): 514
The number of instances where the actual class was "Arrest" (Yes) and the model correctly predicted "Arrest" (Yes).

The Decision Tree model shows improved recall and precision over logistic regression for the "Arrest" class but still struggles with a moderate rate of false negatives and false positives. It has high specificity and accuracy, making it better suited for scenarios where correctly identifying the "No Arrest" class is more important.