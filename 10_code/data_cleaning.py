import pandas as pd
from nltk import tokenize
from datetime import datetime
import matplotlib.pylab as plt
import yfinance as yf
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from numba import jit, prange

def clean_nvidia_df(df_str):
    # input data
    nvidia_df = pd.read_csv(df_str)
    
    # Cleaning step1: fix the issue were the data was appended incorrectly
    correct_df = nvidia_df.iloc[0:16268].copy()
    incorrect_df = nvidia_df.iloc[16268:].copy()

    # relable incoorect columns to be appendsed back correctly
    incorrect_df.rename(
        columns={
            "captionString": "drop",
            "Unnamed: 0": "Index",
            "Unnamed: 0.1": "videoID",
            "videoID": "datePub",
            "datePub": "searchedDate",
            "searchedDate": "VideoTitle",
            "VideoTitle": "channelTitle",
            "channelTitle": "viewCount",
            "viewCount": "likeCount",
            "likeCount": "dislikeCount",
            "dislikeCount": "captionString",
        },
        inplace=True,
    )

    # drop the access coulmn created by AWS appending
    incorrect_df = incorrect_df.drop(columns=["drop"])

    #relable columns to match the corrected df
    correct_df.rename(columns={"Unnamed: 0.1": "Index"}, inplace=True)
    correct_df = correct_df.drop(columns=["Unnamed: 0"])

    #create new nvida data frame to begin cleaning and working with
    nvidia_df_1 = correct_df.append(incorrect_df, sort=False)
    
    return nvidia_df_1
    
def main(df = "../00_data/nvidia_caption_data_21FEB.gz"):
    cleaned_nvidia_df_prefeatures = clean_nvidia_df(df)
    print("Below is the head of the cleaned dataframe \n")
    print(cleaned_nvidia_df_prefeatures.head())
    print("\n Below is the tail of the cleaned dataframe \n")
    print(cleaned_nvidia_df_prefeatures.tail())

    
if __name__ == "__main__": 
    import sys
    df_str = str(sys.argv[1])
    main(df_str)