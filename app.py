from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#import requests
#import json
#import pandas as pd
#import datetime
#from bokeh.plotting import figure, output_file, show
#from bokeh.models import ColumnDataSource

#def getURL(ticker, key = 'XXX'):
  #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
  #response = requests.get(url)
  #return response

#def processing(response, price):
  #df = pd.read_json(response)
  #df_sub = df[5:]
  #df_sub.reset_index(inplace=True)
  #df_sub['index'] = pd.to_datetime(df_sub['index'])
  #df_sub['Time Series (Daily)'].apply(pd.Series)
  #df_sub = pd.concat([df_sub, df_sub['Time Series (Daily)'].apply(pd.Series)], axis=1)
  #df_final = df_sub[['price']]
  #return df_final

#def make_graph(df):
  #p = figure(x_axis_type='datetime')
  #p.line(x='index', y='price',
       #source=source,
       #line_width=2, color='green')
  #p.title.text = ticker
  #p.xaxis.axis_label = 'Date'
  #p.yaxis.axis_label = 'Price in USD'
  #return p

@app.route('/', methods=['GET','POST'])
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/graph', methods=['POST'])
def graph():
  ticker = request.form['tickerInput'].upper()
  price = request.form['priceInput']

  response = getURL(ticker)
  df = processing(response, price)

  p = make_graph(df)

  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
