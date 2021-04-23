# Youtube Content Based Stock Prediction Sentiment

This Repo is a representation of Team 2's Final Project for Duke MIDS IDS 705: Machine Learning, Spring 2021 class

### Authors:
Dapo Adegbile, 
Sutianyi Wen,
Jiaman Betty Wu,
Yiwen Wang, and
Christopher Oblak

### Abstract: 

YouTube is a source of generally untapped expert knowledge and popular opinion trends when it comes to automated modeling.   Much like the news, online forums, and Twitter posts, YouTube is an outlet for information sharing.  The large difference in most cases is that individuals who are able to amass a large following are garnering huge influential power in the way products and services are received by the population that would use them.  In this specific instance, we are interested in YouTube’s top return search content for Nvidia from October 2020 to the present day.  We hope to show that the top videos on a given day have potential predictive properties associated with their influence for new and upcoming products that could shape the markets they are tied to.  To do this we will look at standard easy to retrieve metrics such as views, video titles, likes, dislikes, and dates published.  We also wish to harness the content of the video themselves through the use of YouTube’s automated captions. These captions have improved significantly over the course of the last five years, and are not being utilized in the manner Twitter and other easy-to-access media is.  The influential power of youtube content creators, along with mining captions is manner not seen elsewhere, we hope to find predictive power to anticipate market shifts, ultimately highlighting the influential power of youtube and its content. 

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
