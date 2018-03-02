import click
from alpha_Vantage.timeseries import TimeSeries

@click.command('TimeSeries')

@click.option('-i','-intraday',
              help='This API returns intraday time series'
              '(timestamp, open, high, low, close, volume)'
              'of the equity specified, updated realtime.')

@click.option('-d','--daily',
               help='This API returns daily time series'
              '(date, daily open, daily high, daily low,'
              'daily close, daily volume) of the equity'
              'specified, covering up to 20 years of'
              'historical data.')

@click.option('-dA','--dailyAdjust',
               help='This API returns daily time series'
              '(date, daily open, daily high, daily low,'
              'daily close, daily volume, daily adjusted'
              'close, and split/dividend events) of the'
              'equity specified, covering up to 20 years of'
              'historical data.')

@click.option('-w','--weekly',
              help='This API returns weekly time series'
              '(last trading day of each week, weekly open,'
              'weekly high, weekly low, weekly close, weekly'
              'volume) of the equity specified, covering up'
              'to 20 years of historical data.')

@click.option('-wA','--weeklyAdjust',
               help='This API returns weekly adjusted time'
              'series (last trading day of each week, weekly'
              'open, weekly high, weekly low, weekly close,'
              'weekly adjusted close, weekly volume, weekly'
              'dividend) of the equity specified, covering up'
              'to 20 years of historical data.')

@click.option('-m','--monthly',
               help='This API returns monthly time series'
              '(last trading day of each month, monthly open,'
              'monthly high, monthly low, monthly close,'
              'monthly volume) of the equity specified,'
              'covering up to 20 years of historical data.')

@click.option('-mA','--monthlyAdjust',
               help='This API returns monthly adjusted time'
              'series (last trading day of each month, monthly'
              'open, monthly high, monthly low, monthly close,'
              'monthly adjusted close, monthly volume, monthly'
              'dividend) of the equity specified, covering up to'
              '20 years of historical data.')

@click.option('-b','--batch',
               help='The batch stock quotes API enables the'
              'querying of multiple stock quotes with a single'
              'API request, updated realtime. It may serve as'
              'a lightweight alternative to our core stock'
              'time series APIs above (which have richer'
              'content but are symbol-specific).')


def timeSeries():
    
