from dotenv import load_dotenv
import os
from datetime import datetime
import requests

load_dotenv()
STOCK = os.getenv("STOCK")
COMPANY_NAME = os.getenv("COMPANY_NAME")
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def five_percent_swing():
    parameters ={
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": AV_API_KEY
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    data = response.json()

    last_trade_days = []
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day

    while len(last_trade_days) < 2:
        try:
            print
            last_trade_days.append(data["Time Series (Daily)"][str(date.date())]["4. close"])
        except KeyError:
            print(f"No trade activity on {date.date}")
            day -= 1
            date = datetime(year,month,day)
        else:
            day -= 1
            date = datetime(year,month,day)
    print(last_trade_days)
    percent_diff = (float(last_trade_days[1])/float(last_trade_days[0])) * 100 - 100

    return percent_diff
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    pass
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


if abs(five_percent_swing()) >= 5:
    print("Get News")
else:
    print("Nothing to see here")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

