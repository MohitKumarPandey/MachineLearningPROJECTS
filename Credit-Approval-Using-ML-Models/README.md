# Credit-Approval-Using-ML-Models

## **Table of contents**

- [Project overview](#project-overview)
- [Data](#data)
- [Technologies](#technologies)
- [Features](#features)
- [Limitations](#limitations)
- [Process](#process)
- [Results](#results)
- [What I learned](#what-i-learned)
- [How can it be improved](#how-can-it-be-improved)
- [Running the project](#running-the-project)

## **Project overview**

This project evaluates the performance of different machine learning models on a banking dataset related to personal loan approval.

The analysis focuses on comparing the performance of **Logistic Regression**, **Decision Trees**, **Gradient Boosting**, and **Support Vector Machines (SVM)**, starting with Logistic Regression as the baseline model due to its interpretability and then extending the analysis with machine learning models capable of capturing complex nonlinear relationships.

The methodological approach includes data cleaning, selection of relevant variables through correlation analysis, cross-validation, evaluation using metrics such as **accuracy**, **recall**, **F1-score**, and **AUC**, as well as an analysis of statistical assumptions in the case of logistic regression.

## **Data**

The dataset used, "`bank_loan`", contains demographic and financial information for 5,000 individuals across the following variables:

| Variable | Definition |
| :---: | :---: |
| `ID` | Client ID |
| `Age` | Age of the client |
| `Experience` | Years of experience |
| `Income` | Annual income (thousands of USD) |
| `ZIP.Code` | ZIP code | 
| `Family` | Number of family members |
| `CCAvg` | Average monthly credit card spending |
| `Education` | Educational level (1 = Undergrad, 2 = Graduate, 3 = Professional) |
| `Mortgage` | Existing mortgage amount |
| `Personal.Loan` | Indicates whether the loan was granted (1 = Yes, 0 = No) |
| `Securities.Account` | Indicates whether the client has a securities account (1 = Yes, 0 = No) |
| `CD.Account` | Indicates whether the client has a CD account (1 = Yes, 0 = No) |
| `Online` | Indicates whether the client has an online account (1 = Yes, 0 = No) |
| `CreditCard` | Indicates whether the client has a credit card (1 = Yes, 0 = No) |

## **Technologies**

- **Python**
- **Jupyter Notebook**

## **Features**

Here is what this project does:

- **Exploratory data analysis:** Analyzes customer demographic and financial variables related to personal loan approval.
- **Feature selection:** Identifies relevant predictive variables based on correlation analysis and financial interpretability.
- **Model training:** Trains and evaluates multiple machine learning models, using Logistic Regression as a baseline.
- **Class imbalance handling:** Applies SMOTE to address class imbalance in the target variable.
- **Model evaluation:** Assesses model performance using metrics such as **Accuracy**, **Precision**, **Recall**, **F1-score**, **AUC**, and **ROC curves**.
- **Model comparison:** Compares **Logistic Regression**, **Decision Tree**, **Gradient Boosting**, and **Support Vector Machine** models using **ROC curves**, **AUC values**, and the **Kolmogorov–Smirnov index** to determine the best-performing approach.

## **Limitations**

The main limitations of this project are:

- The dataset only includes **basic demographic** and **financial variables**.
- Although SMOTE is applied to address class imbalance, **synthetic observations** may not fully reflect real borrower behavior.
- Model performance could differ when applied to naturally **imbalanced data**.

## **Process**

First, the dataset "`bank_loan.csv`" was loaded, its dimensions (5,000 rows and 14 columns) were verified, data types were reviewed, and the presence of missing values was checked. Then, an exploratory analysis was performed, using `Personal.Loan` as the target variable, which has a class imbalance with 90.4% non-approved loans and 9.6% approved loans.

Next, the correlation matrix was computed, and the distribution of variables was explored using histograms and count plots. Based on their correlation with the target variable and financial interpretability, the following predictors were selected:

- **Income**
- **CCAvg**
- **CD.Account**
- **Mortgage**
- **Education**

Additionally, a bivariate analysis was performed to assess the relationship between each selected predictor and `Personal.Loan`.

A logistic regression model was then fitted and performance metrics such as the confusion matrix, accuracy, precision, recall, and F1-score were computed, along with the ROC curve.

![Confusion_matrix_logistic_regression](https://github.com/Daniel-Ro-Santiago/Credit-Approval-Using-ML-Models/blob/main/README-Img/README_CAUMLM_1.png)

![ROC_curve_logistic_regression](https://github.com/Daniel-Ro-Santiago/Credit-Approval-Using-ML-Models/blob/main/README-Img/README_CAUMLM_2.png)

To address class imbalance, SMOTE was applied to the training set, the logistic regression model was retrained, and the same performance metrics were recalculated. The assumptions of logistic regression were then evaluated, including multicollinearity, logit linearity (Box-Tidwell test), independence of errors (Durbin-Watson), and the absence of influential outliers (Cook’s distance and leverage). Finally, the analysis was extended by evaluating the overall goodness of fit.

For the comparison between Logistic Regression, Decision Tree, Gradient Boosting, and Support Vector Machine models, the 10 variables with the highest correlation with `Personal.Loan` were used. Model performance was summarized in a comparative table, ROC curves were generated, AUC values were plotted, and the Kolmogorov–Smirnov index was calculated for each model.

![ROC_curves_complete_models](https://github.com/Daniel-Ro-Santiago/Credit-Approval-Using-ML-Models/blob/main/README-Img/README_CAUMLM_3.png)

![AUC_complete_models](https://github.com/Daniel-Ro-Santiago/Credit-Approval-Using-ML-Models/blob/main/README-Img/README_CAUMLM_4.png)

## **Results**

**Gradient Boosting** achieved the best overall performance compared to the other models.

> **Final recommendation**
>
> As a final recommendation for this dataset, Gradient Boosting is proposed as the primary model due to its high predictive performance, while SVM, Decision Tree, and Logistic Regression are considered suitable alternatives depending on interpretability requirements or computational constraints.

## **What I learned**

The most important thing I learned from this project is that the selection of a machine learning model should be guided by its performance metrics on a specific dataset, rather than by model popularity alone. It is also essential to align model choice with the objectives and characteristics of the data, as different models can provide valuable insights from different perspectives. For instance, in this project, Support Vector Machines and Decision Trees can be useful when prioritizing interpretability or when the goal is to minimize specific types of errors, such as false positives.

## **How can it be improved**

- Explore whether the selection of predictive variables can be further optimized.
- Apply variable transformation techniques to satisfy linearity assumptions.
- Implement more robust methods for outlier treatment.
- Incorporate more extensive **cross-validation** strategies.

## **Running the project**

To run the project, simply open the Jupyter Notebook `Credit_Approval_Using_ML_Models`, load the csv file `bank_loan` and run all cells.
