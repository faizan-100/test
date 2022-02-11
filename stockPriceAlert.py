import requests
api_key = '790b1ff41b344d8c7ea4dfa4ff9bfa35'
import smtplib
import time
password = ""




def send_email():


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("faizan.hussain2003@gmail.com", password)
    subject = "Price is down"
    body = "price down"
    msg = f'subject: {subject} {body}'

    server.sendmail(
        'faizan.hussain2003@gmail.com'        
        'faizan.hussain2003@gmail.com',
        msg
    )
    print('email is sent')
    server.quit()

def check_stock (api_key, password):
    prices = requests.get(f'https://financialmodelingprep.com/api/v3/profile/AAPL?apikey={api_key}').json()
    stock_price = prices[0]['price']
    print("£" + str(stock_price))
    if stock_price < 170:
        send_email(password)

    #run every 10 mins:
while(True):
    check_stock(api_key, password)
    time.sleep(600)
