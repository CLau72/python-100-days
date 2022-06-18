from dotenv import load_dotenv
import os
from datetime import datetime
import requests
from twilio.rest import Client

load_dotenv()
STOCK = os.getenv("STOCK")
COMPANY_NAME = os.getenv("COMPANY_NAME")
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_API_KEY =  os.getenv("TWILIO_API_KEY")
FROM_PHONE = os.getenv("FROM_PHONE")
TO_PHONE = os.getenv("TO_PHONE")


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
    parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 3
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)

    data = response.json()
    
    articles = [article["title"] for article in data["articles"]]
    return articles

    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_message(percent, articles):

    if percent > 0:
        text_message = f"""
        {COMPANY_NAME} is 📈 {percent} today.\n
        Related Stories:
        {articles[0]}\n
        {articles[1]}\n
        {articles[2]}
        """
    else:
        text_message = f"""
        {COMPANY_NAME} is 📉 {percent} today.\n
        Related Stories:
        {articles[0]}\n
        {articles[1]}\n
        {articles[2]}
        """

    client = Client(TWILIO_SID, TWILIO_API_KEY)

    message = client.messages \
                    .create(
                        body = text_message,
                        from_= FROM_PHONE,
                        to= TO_PHONE
                    )

    print(message.sid)


articles = get_news()

send_message(6,articles)




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

