
from pprint import pprint
from alpha_vantage.timeseries import TimeSeries

#########################################################
#                     Variables                         # 

trys = 5 # Number of re-attempts to connect
form = 'json' # Options: json, csv, pandas
info_as = False # Boolean
ind = 'date' # Index key

ops = 'compact' # Options: compact, full
intr = '15min' # Options: 1min, 5min, 15min, 30min, 60min.
ticker = 'MSFT' # Company tickers
scope = 'monthly' # Options: batch_stock_quotes, daily, daily_adjusted, intraday,
                  # weekly, weekly_adjusted, monthly, monthly_adjusted
                   

##########################################################


ts = TimeSeries(key='II0VU3FTX7AAEU99') # , retries=trys , output_format=form , treat_info_as_error=info_as,
#                indexing_type=ind )

def operation(ts, scope, ticker, ops, intr):
    if scope == 'intraday':
        operates = "%s.get_%s(symbol=%s, outputsize=%s, interval=%s)" % (ts, scope, ticker, ops, intr)
    elif scope == 'daily' or scope == 'daily_adjusted':
        operates = "%s.get_%s(symbol=%s, outputsize=%s)" % (ts, scope, ticker, ops)
    else:
        operates = "%s.get_%s(symbol=%s)" % (ts, scope, ticker)
    return operates

##data, meta_data  = exec(operation)
      
print (operation(ts, scope, ticker, ops, intr))
