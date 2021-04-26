<p align="center">

# Youtube Content Based Stock Prediction Sentiment

This Repo is a representation of Team 2's Final Project for Duke MIDS IDS 705: Machine Learning, Spring 2021 class

### Authors:
Dapo Adegbile, 
Sutianyi Wen,
Jiaman Betty Wu,
Yiwen Wang, and
Christopher Oblak

</p>

### Abstract: 

In this project, we built predictive models using YouTube to predict "buy", "hold", and "sell" on Nvidia stock.  We explored many avenues for feature building and concluded on the use of basic video metrics, sentiment analysis on captions and video titles.  Using this information, we achieved a validation accuracy of 80.4% for buy, a hold accuracy of 84.6%, and a sell accuracy of 62.9%. In the past, research was conducted using text based social media to predict the stock price but we believed YouTube could perform better as videos have more information than tweets. As a result, we found YouTube has promising predictive power over stock prices. 

Questions we wish to tackle:
  - Does content of top searched youtube videos provide an accurate indicator for stock fluctuations 
  - Can we use the youtube content (captions, title names) to decide trading actions(buy, sell and hold)? 


Text Here

![Alt text](Method_Flowchart_23APR.png?raw=true "Title")

#### Acknowledgement

The major package used to pull the captions themselves was the 
youtube_transcript_api package.  You can find details on it at the below link.

https://github.com/jdepoix/youtube-transcript-api

## Usage (Coming Soon)

#### Youtube Caption Data and Metric Pulling


#### stock_pred_model.py

The stock_pred_model.py code will take the (current) caption data that the lambda 
fuction builds that then plot that with the associated Stock data.  In this case
the data and code has been written for Nvidia Youtube Searches and Stock 
comparisons (see below image for exmple of plot, and this codes potential usefulness)


![Alt text](10_plots/NVDA_Sentiment_Stock_ComparisonPlot.jpeg?raw=true "Title")


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
