# Van_Rental_Fortune_Telling
Time series dataset used to predict van rental sales demand.

<!-- #region -->
# BackGround

A National Van Rental company’s has expenses that are variables based on demand. The largest and most volatile expense is the fleet cost. If the fleet is too large, then massive quantities of car notes are paid on unused vans. If the fleet is too small, then revenues and market share are lossed.


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

# The Issue
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
     
     
### Years Split/Time Series
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/eda_years_split.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


## Algorithms Outline

1. Custom Trailing Moving Average Function (TMA)
2. ARIMA
3. fbprophet
4. LSTM



## Scoring Metric
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/scoring_metric.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


## Stationarity: Original Data

<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/stationarity_plot_orig.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />


<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/dickery_fuller_orig.png"
     alt="Markdown Monster icon"
     height="300" width="600"
     style="float: left; margin-right: 10px;" />

# The Results
<img src="https://github.com/Prvargas/Van_Rental_Fortune_Telling/blob/master/img/model_results.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

# Interpretation

```python

```
