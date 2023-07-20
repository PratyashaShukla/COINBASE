# importing flask
from flask import Flask, render_template,request,redirect,jsonify

# importing pandas module
import pandas as pd
import ccxt.async_support as ccxt
import configparser
import ccxt
# print(ccxt.exchanges)
app = Flask(__name__)
config_file = configparser.ConfigParser()

# ADD SECTION
config_file.add_section("FTPSettings")
# ADD SETTINGS TO SECTION
config_file.set("FTPSettings", "ftpUrl", "demoftp.codeteddy.com")
config_file.set("FTPSettings", "userName", "codeteddy")
config_file.set("FTPSettings", "password", "my#supersecret#password")

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

# print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
# print("Content of the config file are:\n")
# print(content)
read_file.flush()
read_file.close()
import ccxt

exchange = ccxt.coinbasepro({
    'apiKey': 'b21af270f6340cfb9e691cb962278d81',
    'secret': 'IuD4qv+FNHExc4DaXriqMdKw/YiJ0uFmKLC75GEWZH7PLOWbn0nL4lAJRktrjFtefDRJZ5sPh8P0S59rDCTWZA==',
    'password': 'os7d8cfb50s'
})
balance = exchange.fetch_balance()

@app.route("/exchange/<exchangeName>/balances")
def index(exchangeName):
    answer={'info': None ,'balances': None}
    balance = exchange.fetch_balance()
    for exchng in balance['info']:
        answer['info']=exchng;
        if exchng['currency'] == exchangeName:       
         result={'currency':exchangeName};
         result.update(balance[exchangeName]);
         answer['balances']=result
    return jsonify(answer)

@app.route("/")
def home():
     balance = exchange.fetch_balance()
     item = list(balance.keys())[2:]
     return render_template("home.html",item=item)
    
@app.route('/exchangeName',methods=["POST"]) 
def exchng():
    exchangeName = request.form['itemName']
    link="/exchange/" + exchangeName + "/balances";
    return redirect(link)



# balance = exchange.fetch_balance()
# print(balance)




if __name__ == "__main__":
    app.secret_key = 'super secret key'
app.run( port=3000)