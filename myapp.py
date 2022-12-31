import pandas as pd
import yfinance as yf
from datetime import datetime
import streamlit as st

tickers = "MA,V,AMZN,JPM,BA".split(",")


df = yf.download(tickers,'2022-1-1',datetime.today(), auto_adjust=True)['Close']

st.write(df.head())