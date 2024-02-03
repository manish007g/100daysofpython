import requests
from twilio.rest import Client

STOCK_NAME = "HDFCBANK.BSE"
COMPANY_NAME = "HDFC"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "ACc42850297f530347f585718ccf09b264"
TWILIO_AUTH = "ed03725ac16f8ccfb063f735e7a93de7"

 ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "P8GBX6GXPJA8FME4"
}

r = requests.get(STOCK_ENDPOINT, params=stock_params)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]

new_data = [value for (key,value) in data.items()]
yesterday_data = new_data[0]

yesterday_closing_price=float(yesterday_data["4. close"])
print(yesterday_closing_price)

# #TODO 2. - Get the day before yesterday's closing stock price
#
day_before_yes_data = new_data[1]
day_before_yes_closing_price = float(day_before_yes_data["4. close"])

print(day_before_yes_closing_price)

# #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#
price_change = (yesterday_closing_price - day_before_yes_closing_price)
up_down = None
if price_change > 0:
  up_down = "🔺"
else:
  up_down = "🔻"
# #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#
price_percent = round(price_change / int(day_before_yes_closing_price) * 100)

print(price_percent)
# #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
#
if abs(price_percent) > 0:
    news_param = {
        "qInTitle": COMPANY_NAME,
        "apiKey": "4c0e12b249084ea18da7c8b869f7fe73"

    }
    req = requests.get(NEWS_ENDPOINT, params=news_param)
    data_news = req.json()["articles"]
    print(data_news)

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles= data_news[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_article = [f"{STOCK_NAME}: {up_down}{price_percent} \n Headline: {news['title']}. \n Brief: {news['description']}" for news in three_articles]

    print(formatted_article)

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(TWILIO_SID, TWILIO_AUTH)

    for art in formatted_article:
        message = client.messages.create(
            body=art,
            from_="+12034429630",
            to="+918605698837"
        )

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

