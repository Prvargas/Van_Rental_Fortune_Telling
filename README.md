# Van_Rental_Fortune_Telling
Time series dataset used to predict van rental sales demand.

<!-- #region -->
# BackGround

A National Van Rental company has expenses that are variables based on demand. The largest and most volatile expense is the fleet cost. If the fleet is too large, then massive quantities of car notes are paid on unused vans. If the fleet is too small, then revenues and market shares are lossed.


## Questions to solve this business problem: 

- What are the peak Days? Weeks? Months? Quarters? Season?
- What are the slow periods? How long do they last?
- How often is the company under fleeted?
- How often is the company over fleeted?
- Can the company optimize fleeting patterns?


## Goals

- Build an accurate model to predict van rental sales demand.
- Help the Van Rental company optimize variable expenses.


<!-- #endregion -->

# The Problem
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/predictions.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

# The Experimentation Process

<!-- #region -->
## Machines Used:
- **Macbook:** CPU 4; 16gb Ram; With GPU
- **AWS EC2:** CPU 16; 64gb Ram; No GPU

## Data

**Raw Data:** CSV
- **DataFrame:** (Rows, Columns)
- **2019 Revenue:** (106494, 171)
- **2018 Revenue:** (106563, 165)
- **2017 Revenue:** (96909, 159)


**Prepped Data:**
- **Total Days:** 1,095	 
- **Total Sales Count:** 305,353

<!-- #endregion -->

## EDA

### Years Combined
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/eda_years_combined.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- The bell curve shape histogram indicates sales follows a Normal Distribution.
- In the boxplot we see the monthly seasonality via the wavy shape.
     
### Years Split/Time Series
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/eda_years_split.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- The Sales By Month bar chart shows peak months are in the summer.
- The Sales by Day of Week bar chart shows the peak day is Friday.

## Algorithms Outline

1. Custom Trailing Moving Average Function (TMA)
2. ARIMA
3. fbprophet
4. LSTM



## Scoring Metric
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/scoring_metric.png"
     alt="Markdown Monster icon"
     height="300" width="700"
     style="float: left; margin-right: 10px;" />

- The lower the error the better the model.

## Stationarity: Original Data

<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/stationarity_plot_orig.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/dickery_fuller_orig.png"
     alt="Markdown Monster icon"
     height="300" width="600"
     style="float: left; margin-right: 10px;" />

- The Dickey Fuller test is a mathematical test for stationarity. 
- This data is NOT stationary. 
- In order to use certain algorithms the data must be stationary.


# The Results
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/model_results.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


## Best Model Train/Tune/Test 
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/fbprophet_tuning.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- The Graphs above show RMSE on the y-axis and fbprophet trend hyperparameters on the x-axis.
- The smallest RMSE is indicated by the dotted redline per graph.


<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/fbprophet_plot.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
- I used 70% of the data to train the model and 30% of the data to test and evaluate model performance.
- The blue line represents the **PREDICTIONS** and the orange line represents the **ACTUALS** from the test data.
- The blue **PREDICTION** line and the orange **ACTUALS** line **OVERLAP** nicely, indicating the model is performing well. 

# Model Application Experiment
**Experiment Reality:**
1. Cars can be purchased and sold every day with no lag.
2. There is always an immediate buyer when vans are being sold.
3. There is always immediate funding when vans are being purchased.




**Experiment Rules:**

**First Rule.** Optimal fleet availability is double the predicted demand.

**Second Rule.** Any time fleet is greater than one BUT less than optimal, the company will benefit 400 Dollars per car.

**Third Rule.** Any time fleet is over the optimal mark it will cost the company 400 Dollars per vehicle.

**Fourth Rule.** Anytime fleet is in the negative it will cost the company 400 Dollars in revenue per vehicle.

<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/model_application.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

**Model Application Results**
- The highest amount of over fleeting cost happens late December to early January.
- Performance between man and model oscillated between profit and loss.
- If the model was deployed the company would have save $360K thousand dollars for the Los Angeles Location!

# Tableau Dashboard
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/tableau.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- I created a Tableau dashboard with an interactive map showing sales demand by state & by city
- The pie chart shows the split between repeat customers and non-repeat customers.
- The horizontal bar graph shows demand by van type.
- A dashboard like this could be utilized by a company's non technical employees to observe the results of some of these very technical time series analyses. 

# Business Question Answers
- Peak Day: Friday
- Peak Months: June & July
- Slow Day: Sunday
- Slow Months: January & December
- The company should look into drastically reducing fleet late December to early January.


# Conclusion
For this van rental company COMPLETE fleet automation may be too ambitious, BUT AUGMENTING fleet decisions is very possible and it would contribute immense value to this organization.

```python

```
