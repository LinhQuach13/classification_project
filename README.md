# Classification Project

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
> - Create modules (acquire.py, prepare.py) that make your process repeateable.
> - Construct a model to predict customer churn using classification techniques.
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
> - Answer panel questions about your code, process, findings and key takeaways, and model.

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

#### Project Context
> - The Iris dataset I'm using came from the Codeup database.
> - Find out more about Fisher's Iris Dataset [here](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5).


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
- The following are key takeways:

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

##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> **Acquire ->** Prepare -> Explore -> Model -> Deliver
> - Store functions that are needed to acquire data from the measures and species tables from the iris database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> **Prepare ->** Explore -> Model -> Deliver
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> **Explore ->** Model -> Deliver
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, species. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> **Model ->** Deliver
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> **Deliver**
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>



### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the telco_final.ipynb notebook
