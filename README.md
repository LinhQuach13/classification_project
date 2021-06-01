# Classification Project

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

### Project Planning 

Access to Trello Board3: https://trello.com/b/oBy4gxFx/classification-project

Here is a snapshot of my project planning/setup on the morning of 3/6/21

![image info](S(https://user-images.githubusercontent.com/80718476/120330558-8a963880-c2b2-11eb-9d3e-5fc710e9b5c3.png)

### Project Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.

#### Business Goals
> - Find drivers for customer churn at Telco.
> - Construct a ML classification model that accurately predicts customer churn.
> - Document your process well enough to be presented or read like a report.

#### Audience
> - Codeup Data Science team

#### Project Deliverables
> - A final report notebook 
> - A final report notebook presentation
> - All necessary modules to make my project reproducible
> - A csv file of prediction probabilities and actual values for churn.


#### Data Dictionary
    
- This is a data dictionary as a reference for the variables used within in the data set.
 

|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  customer_id | object   | unique customer ID   |
| payment_type_id   | int64 |Type of payment: credit card(automatic), Bank transfer(automatic), Mailed check|
| partner   | object   | 0= no partner, 1= has partner|
| phone_service  | object   |Yes or No for phone service|
| tenure   | int64 |# of months with company|
| total_charges   | int64 | total charges since day 1|
| churn  | object| Yes = Churn, No = Not Churned|
| churn_No  | object| 0 = Churn, 1 = Not Churned|
| churn_Yes  | object| 1 = Churn, 0 = Not Churned|
| no_partner_depend   | int64 | no partner & no dependents|
| phone_lines   | int64 | 1 = has phone lines, 0 = No phone|
| stream_tv_mov   | int64 | has streaming tv & streaming movie|
| online_sec_bckup  | int64 | has online security & online backup|
| female  | uint8| 1 = female, 0 = not female|
| male  | uint8| 1 = male, 0 = not male|
| no_partner  | uint8 | 1 = no partner, 0 = has partner|
| has_partner  | unit8 | 1 = has partner, 0 = no partner|
| dependents_no   | unit8| 1 = no dependents, 0 = has dependents|
| dependents_yes   | unit8| 1 = has dependents, 0 = no dependents|
| device_proctection_no   | uint8 | 1 = no protection, 0 = has protection|
| device_proctection_no_int   | uint8 | 1 = no internet, 0 = has internet|
| device_proctection_yes   | uint8 | 1 = has protection, 0 = no protection|
| tech_support_No  | uint8 | 1 = no tech support, 0 = has tech support|
| tech_support_No internet service   | uint8 | 1 = no internet, 0 = has internet|
| tech_support_yes  | uint8 | 1 = has tech support, 0 = no tech support|
| paperless_billing_no   | uint8 | 1 = no paperless billing 0 = has paperless billing|
| paperless_billing_yes   | uint8 | 1 = has paperless billing, 0 = no paperless billing
| contract_type_Month-to-month   | uint8 | 1 = on monthly contract, 0 = no monthly contract|
| contract_type_One year    | uint8 | 1 = on 1 yr contract, 0 = not on 1 yr contract|
| contract_type_Two year     | uint8 | 1 = on 2 yr contract, 0 = not on 2 yr contract|
| internet_service_type_DSL   | uint8 | 1 = has dsl, 0 = no dsl|
| internet_service_type_Fiber optic    | uint8 | 1 = has fiber optic, 0 = no fiber optic|
| internet_service_type_None | uint8 | 1 = no internet, 0 = has internet|
| payment_type_Bank transfer (automatic)   | uint8 | 1 = pay w/bank transfer, 0 = no bank transfer|
| payment_type_Credit card (automatic)   | uint8 | 1 = pays w/credit card, 0 = no credit card|
| payment_type_Electronic check  | uint8 | 1 = pays w/elec check, 0 = no elec check|
| payment_type_Mailed check  | uint8 | 1 = pays w/mail check, 0 = no mail check|


#### Initial Hypotheses

> - **Hypothesis 1 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_0$: contract month to month has no affect on customers who churn(they are independent). 
> - $H_a$: contract month to month has an affect on customers who churn  (they are dependent). 

> - **Hypothesis 2 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_0$: contract month to month has no affect on customers who do not churn  (they are independent).
> - $H_a$: contract month to month has an affect on customers who do not churn  (they are dependent).

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
<b>The following are key takeways:</b>

  -There is not one main driver churn.

  -The customers who are leaving are mainly month to month contract holder with no tech support and no online security
  
  -Decision Tree has a good accuracy score for the train and validate data but Logistic regression model has higher accuracy score
  
  -KNeighbors has the highest training accuracy score but the validate score is fairly different. KNN model is overfitted for the training model.
  
 - Logistic regression model 1 is best model in terms of accuracy.
 
 - Logistic regression model 1 is better than baseline but with more time I would continue to work with this model to improve the accuracy score
  
  - The models I created were a  LogisticRegression, DecisionTree, and KNeighbors predicted similar accuracy scores for the training dataset. The model I chose was the Logistic Regression model 1 as my best model with a 77.8% accuracy rate for predicting features of contract_type: month-to-month, No online security, No tech support, internet service type: Fiber optic, and monthly charges.
  
  -  The logistic model 1 outperformed my baseline score of 73.5 % thus it has value.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

- Acquire the data
- Prepare and clean data
- Explore 
- Model & Evaluate
- Recommendataions


___

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>



### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the telco_final.ipynb notebook
