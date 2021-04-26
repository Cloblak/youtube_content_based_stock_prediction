
<h1 align="center">Youtube Content Based Stock Prediction Sentiment</h1>

<p align="center">This Repo is a representation of Team 2's Final Project for Duke MIDS IDS 705: Machine Learning, Spring 2021 class</p>

<h3 align="center">Authors:</h3>
<p align="center">Dapo Adegbile, 
Sutianyi Wen,
Jiaman Betty Wu,
Yiwen Wang, and
Christopher Oblak</p>

## Using This Repo

The repo contains major coding notebooks that allowed us to reach our results posted below.  To repeat these steps and allow a visitor to use this code, we have placed the consolidated main notebook in the parent folder 10_code, and subsequent code used to explore and work toward are end goal in a sub folder 11_usefulCode.  

To explore, tune, run, and predict stock fluctuations please use the notebook “Final_Youtube_Content_NoteBook_23APR.ipynb” in the parent 10_code folder and install dependencies from the requirement.txt file.  All required data sets that have been cleaned and aggregated are in the 00_data folder and are properly referenced.  

Note:  For real time prediction outside of the data provided you will need to acquire a YouTube API v2 Authorization key.


## Project Overview

### Abstract: 

In this project, we built predictive models using YouTube to predict "buy", "hold", and "sell" on Nvidia stock.  We explored many avenues for feature building and concluded on the use of basic video metrics, sentiment analysis on captions and video titles.  Using this information, we achieved a validation accuracy of 80.4% for buy, a hold accuracy of 84.6%, and a sell accuracy of 62.9%. In the past, research was conducted using text based social media to predict the stock price but we believed YouTube could perform better as videos have more information than tweets. As a result, we found YouTube has promising predictive power over stock prices. 

Questions we wish to tackle:
  - Does content of top searched youtube videos provide an accurate indicator for stock fluctuations 
  - Can we use the youtube content (captions, title names) to decide trading actions(buy, sell and hold)? 


### Method Visualization:

![Method Flow Chart](Method_Flowchart_23APR.png?raw=true&s=100)

### Data

Building out the dataset occurred in two phases.  By scrapping YouTube daily for the top 25 videos related to Nvidia, we obtained raw data on videos for that snapshot in time-related to their basic video metrics (view count, likes, dislikes, publication date, ect.), as well as all caption data by using Amazon Web Service (AWS). From this data, we were able to build and aggregate features over every hour in which data was collected. 

The second step is to create the response variable based on 96-hour later percentage change of Nvidia stock price. Because we were interested in predicting stable stock price shifts instead of the stock volatility, we found that using future 96-hour price change yields more stable and significant price change compared to using shorter future periods such as future 24-hour, 48-hour and 72-hour price change. The rules of generating the response variable is: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i)  future 96-hour stock price percentage change is < -3%, the response variable is “sell”; </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii) future 96-hour stock price percentage change is between +/- 3% , the response variable is “hold”; </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii) future 96-hour stock price percentage change is greater than +3%, the response variable is “buy”. </br>

### Summarized Results

Of the models we ran on our data, we found the Light Gradient Boosting Machine to be the most effective, giving us a buy accuracy of 80.4%, a hold accuracy of 84.6%, and a sell accuracy of 62.9% on our validation data. Conversely, our baseline model (Logistic Regression) generated accuracies of 33.9% for buy, 83.85% for hold, and 44.4% for sell.

![Confusion Matrix](ConfusionMatrixs_26APR.png?raw=true&s=100)

Our analysis highlighted that information from YouTube videos were useful to facilitate investment decisions in the stock market because our models showed promising results in confusion matrices and accuracy scores. From the feature importance plots, the sentiments of video titles and captions  are the top three important features in our model. However, our model was only trained on a small dataset and did not account for the time series property of stock price so the model may not perform well for unseen data. For instance, Nvidia’s stock price rocketed from $552 on April 1st to $623 USD on April 14 but our model still predicted “sell” actions. 

### Summarized Conclusion

Despite the limitations discussed previously, our project has one important takeaway: YouTube videos contain useful information such as video captions and titles to predict the trend of stock price. Our model suggested there exists a correlation between video sentiment and stock prices. Future work includes obtaining information from other social platforms such as Twitter to increase predictive power on stock prices. As a result, individuals can leverage massive information on social media to make investment decisions.


#### Acknowledgement

The major package used to pull the captions themselves was the 
youtube_transcript_api package.  You can find details on it at the below link.

https://github.com/jdepoix/youtube-transcript-api

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
