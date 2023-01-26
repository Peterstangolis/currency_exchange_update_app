## Retrieving the Euro to Canadian and Canadian to Euro Data
## Along with the chart creation

## Libraries
from datetime import datetime, timedelta


import streamlit as st
from yahoofinancials import YahooFinancials


## EURCAD=X
@st.experimental_memo
def eurcad_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    eur_can = YahooFinancials(c)
    eur_can_today = eur_can.get_historical_price_data(start_date=today, end_date=today,
                                                      time_interval='daily')
    eur_can_yest = eur_can.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                     time_interval='daily')
    eur_can_last_year = eur_can.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                          time_interval='daily')

    eur_to_can = round(eur_can_today['EURCAD=X']['prices'][0]['adjclose'],2)
    prev_close_eur_can = round(eur_can_yest['EURCAD=X']['prices'][0]['adjclose'],2)


    return eur_can, eur_to_can, prev_close_eur_can

## CADEUR=X
@st.experimental_memo
def cadeur_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    can_eur = YahooFinancials(c)
    can_eur_today = can_eur.get_historical_price_data(start_date=today, end_date=today,
                                                      time_interval='daily')
    can_eur_yest = can_eur.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                     time_interval='daily')
    can_eur_year = can_eur.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                          time_interval='daily')

    can_to_eur = round(can_eur_today['CADEUR=X']['prices'][0]['adjclose'],2)
    prev_close_can_eur = round(can_eur_yest['CADEUR=X']['prices'][0]['adjclose'],2)

    return can_eur, can_to_eur, prev_close_can_eur

## USDCAD=X
@st.experimental_memo
def usdcad_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    usd_can = YahooFinancials(c)
    usd_can_today = usd_can.get_historical_price_data(start_date=today, end_date=today,
                                                      time_interval='daily')
    usd_can_yest = usd_can.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                     time_interval='daily')
    usd_can_year = usd_can.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                          time_interval='daily')

    usd_to_can = round(usd_can_today['USDCAD=X']['prices'][0]['adjclose'], 3)
    prev_close_us_can = round(usd_can_yest['USDCAD=X']['prices'][0]['adjclose'], 3)

    return usd_can, usd_to_can, prev_close_us_can

## CADUSD=X
@st.experimental_memo
def cadusd_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    can_us = YahooFinancials('CADUSD=X')
    can_us_today = can_us.get_historical_price_data(start_date=today, end_date=today,
                                                      time_interval='daily')
    can_us_yest = can_us.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                     time_interval='daily')
    can_us_year = can_us.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                     time_interval='daily')

    can_to_us = round(can_us_today['CADUSD=X']['prices'][0]['adjclose'], 3)
    prev_close_can_us = round(can_us_yest['CADUSD=X']['prices'][0]['adjclose'], 3)
    print(can_to_us, prev_close_can_us)

    return can_us, can_to_us, prev_close_can_us

##GBPCAD=X
@st.experimental_memo
def gbpcad_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    gbp_can = YahooFinancials('GBPCAD=X')
    gbp_can_today = gbp_can.get_historical_price_data(start_date=today, end_date=today,
                                                    time_interval='daily')
    gbp_can_yest = gbp_can.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                   time_interval='daily')
    gbp_can_year = gbp_can.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                   time_interval='daily')

    gbp_to_can = round(gbp_can_today['GBPCAD=X']['prices'][0]['adjclose'], 3)
    prev_close_gbp_can = round(gbp_can_yest['GBPCAD=X']['prices'][0]['adjclose'], 3)

    return gbp_can, gbp_to_can, prev_close_gbp_can

##CADGBP=X
@st.experimental_memo
def cadgbp_x(c):
    from yahoofinancials import YahooFinancials
    from datetime import timedelta
    import datetime as dt

    today = dt.datetime.today().strftime("%Y-%m-%d")
    yesterday = (dt.datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    last_year = (dt.datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")

    can_gbp = YahooFinancials('CADGBP=X')
    can_gbp_today = can_gbp.get_historical_price_data(start_date=today, end_date=today,
                                                     time_interval='daily')
    can_gbp_yest = can_gbp.get_historical_price_data(start_date=yesterday, end_date=yesterday,
                                                     time_interval='daily')
    can_gbp_year = can_gbp.get_historical_price_data(start_date=last_year, end_date=last_year,
                                                     time_interval='daily')

    can_to_gbp = round(can_gbp_today['CADGBP=X']['prices'][0]['adjclose'], 3)
    prev_close_can_gbp = round(can_gbp_yest['CADGBP=X']['prices'][0]['adjclose'], 3)

    return can_gbp, can_to_gbp, prev_close_can_gbp