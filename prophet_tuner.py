from __future__ import division
from datetime import datetime, timedelta,date
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np


import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

import plotly as py
import plotly.offline as pyoff
import plotly.graph_objs as go

#Import Prophet
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.plot import plot_plotly
import plotly.offline as py


#Create a function for Trend tuning
def FBProphet_Trend_Tuning(df, n_changepoints=25, changepoint_range=0.8, changepoints=None, changepoint_prior_scale=0.05):
    #Going to perform a Train Test Split to better evaluate the model

    full_len = len(df)
    train_len = int(.7*len(df))
    test_len = int(.3*len(df)+1)
    
    #print('100%:{}\n70%:{}\n30%:{}'.format(full_len, train_len, test_len))
    
    
    train = df.iloc[:766]
    test = df.iloc[766:]

    #print('Train df:{}\nTest df: {}'.format(train.shape,test.shape))
    
    #Intialilze model and fit training data
    m = Prophet( n_changepoints=n_changepoints, changepoint_range=changepoint_range, changepoints=changepoints, changepoint_prior_scale=changepoint_prior_scale)
    m.add_country_holidays(country_name='US')
    
    m.fit(train)
    future = m.make_future_dataframe(periods=test_len, freq='D')
    forecast = m.predict(future)
    #print('Forecast df: {}'.format(forecast.shape))

    
    from statsmodels.tools.eval_measures import rmse

    predictions = forecast.iloc[-test_len:]['yhat']
    #print('Predicions Shape: {}'.format(predictions.shape))
    
    rmse = rmse(predictions, test['y'])
    #print("RMSE Score: {}".format(rmse))
    return rmse


# +
#Create a function that optimizes for Number of Changepoints

def FBProphet_Optimizer_nChangepoints_Plot(df, param_lst = np.arange(1,10,1),
                                           changepoint_range=0.8, changepoints=None, changepoint_prior_scale=0.05):
    from numbers import Number
    
    score_lst =[]
    index_lst = []
    
    for i, p in enumerate(param_lst):
        if isinstance(p, Number)==True:
            score = FBProphet_Trend_Tuning(df, n_changepoints=p, 
                                           changepoint_range=changepoint_range, changepoints=changepoints, 
                                           changepoint_prior_scale=changepoint_prior_scale )
            score_lst.append(score)
        
        else:
            index_lst.append(i)
            
    best_param = int(np.array(param_lst)[np.array(score_lst).argsort()[:1]])
    best_score = np.array(score_lst).min()
    
    
    
    plt.figure(figsize=(15,5))
    plt.plot(param_lst, score_lst)
    plt.title('Optimization Plot: n_changepoints')
    plt.ylabel('RMSE')
    plt.xlabel('Parameter Value')
    plt.axvline(best_param, color='r', linestyle='--')
    plt.grid()

    print('Best Parameter Found: {}'.format(best_param))
    print('Best RMSE: {}'.format(best_score))
    
    print('test_avg: {:.02f}'.format(df['y'].mean()))
    print('RMSE/test_avg: {:.02f}\n'.format(best_score/df['y'].mean()))
    
    print('Changepoints Model Params\nn_changepoints= {}\nchangepoint_range= {}\nchangepoints= {}\nchangepoint_prior_scale= {}'.format( 
    best_param, changepoint_range, changepoints, changepoint_prior_scale ))
    
    return best_param, best_score


# +
#Create a function to optimize Change point range

def FBProphet_Optimizer_CP_Range_Plot(df, param_lst= np.linspace(0.1,1,10),
                                     n_changepoints=25, changepoints=None, changepoint_prior_scale=0.05):
    from numbers import Number
    
    score_lst =[]
    index_lst = []
    
    for i, p in enumerate(param_lst):
        if isinstance(p, Number)==True:
            score = FBProphet_Trend_Tuning(df, changepoint_range=p)
            score_lst.append(score)
        
        else:
            index_lst.append(i)
            
    best_param = float(np.array(param_lst)[np.array(score_lst).argsort()[:1]])
    best_score = np.array(score_lst).min()
    
    
    
    plt.figure(figsize=(15,5))
    plt.plot(param_lst, score_lst)
    plt.title('Optimization Plot: changepoint_range')
    plt.ylabel('RMSE')
    plt.xlabel('Parameter Value')
    plt.axvline(best_param, color='r', linestyle='--')
    plt.grid()

    print('Best Parameter Found: {}'.format(best_param))
    print('Best RMSE: {}'.format(best_score))
    
    print('test_avg: {:.02f}'.format(df['y'].mean()))
    print('RMSE/test_avg: {:.02f}\n'.format(best_score/df['y'].mean()))
    
    print('CP Range Model Params\nn_changepoints= {}\nchangepoint_range= {}\nchangepoints= {}\nchangepoint_prior_scale= {}'.format( 
    n_changepoints,best_param, changepoints, changepoint_prior_scale ))
    
    return best_param, best_score


# +
#Create a function that optimizes Changepoint prior scale

def FBProphet_Optimizer_CP_Scale_Plot(df, param_lst= np.linspace(.0001, .0009, 9), n_changepoints=25, 
                                      changepoint_range=0.8, changepoints=None):
    from numbers import Number
    
    score_lst =[]
    index_lst = []
    
    
    for i, p in enumerate(param_lst):
        if isinstance(p, Number)==True:
            score = FBProphet_Trend_Tuning(df, changepoint_prior_scale=p)
            score_lst.append(score)
        
        else:
            index_lst.append(i)
            
    best_param = float(np.array(param_lst)[np.array(score_lst).argsort()[:1]])
    best_score = np.array(score_lst).min()
    
    
    plt.figure(figsize=(15,5))
    plt.plot(param_lst, score_lst)
    plt.title('Optimization Plot: changepoint_prior_scale')
    plt.ylabel('RMSE')
    plt.xlabel('Parameter Value')
    plt.axvline(best_param, color='r', linestyle='--')
    plt.grid()

    print('Best Parameter Found: {}'.format(best_param))
    print('Best RMSE: {}'.format(best_score))
    
    print('test_avg: {:.02f}'.format(df['y'].mean()))
    print('RMSE/test_avg: {:.02f}\n'.format(best_score/df['y'].mean()))
    
    print('CP Scale Model Params\nn_changepoints= {}\nchangepoint_range= {}\nchangepoints= {}\nchangepoint_prior_scale= {}'.format( 
    n_changepoints, changepoint_range, changepoints, best_param ))
    
    return best_param, best_score


# -

def Trend_God(df, changepoints=True, cprange=True, cpscale=True,
             n_chng=25, chng_r=0.8, chng_pts=None, chng_pr_sc=0.05):
    
    score_dict = {}
    
    if changepoints:
        score_dict['n_changepoints']= FBProphet_Optimizer_nChangepoints_Plot(df, changepoint_range=chng_r, 
                                                                             changepoints=chng_pts, 
                                                                             changepoint_prior_scale=chng_pr_sc )
    
    if cprange:
        score_dict['change_point_range']= FBProphet_Optimizer_CP_Range_Plot(df, n_changepoints=n_chng, 
                                                                            changepoints=chng_pts, changepoint_prior_scale=chng_pr_sc)
    
    if cpscale:
        score_dict['change_point_scale']= FBProphet_Optimizer_CP_Scale_Plot(df, n_changepoints=n_chng, 
                                                                            changepoint_range=chng_r, changepoints=chng_pts,
                                                                           )
    
    return score_dict 


