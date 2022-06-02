## Retrieving the Euro to Canadian and Canadian to Euro Data
## Along with the chart creation

## Libraries
from datetime import datetime, timedelta
import datetime

from yahoofinancials import YahooFinancials

## EURCAD=X
def eurcad_x(c):
    eur_can = YahooFinancials(c)
    eur_to_can = round(eur_can.get_current_price(),3)
    prev_close_eur_can = eur_can.get_prev_close_price()
    return eur_can, eur_to_can, prev_close_eur_can

## CADEUR=X
def cadeur_x(c):
    can_eur = YahooFinancials(c)
    can_to_eur = round(can_eur.get_current_price(),3)
    prev_close_can_eur = can_eur.get_prev_close_price()
    return can_eur, can_to_eur, prev_close_can_eur

## USDCAD=X
def usdcad_x(c):
    usd_can = YahooFinancials('USDCAD=X')
    usd_to_can = round(usd_can.get_current_price(),3)
    prev_close_us_can = usd_can.get_prev_close_price()
    return usd_can, usd_to_can, prev_close_us_can

## CADUSD=X
def cadusd_x(c):
    can_us = YahooFinancials('CADUSD=X')
    can_to_us = can_us.get_current_price()
    prev_close_can_us = can_us.get_prev_close_price()
    return can_us, can_to_us, prev_close_can_us

##GBPCAD=X
def gbpcad_x(c):
    gbp_can = YahooFinancials('GBPCAD=X')
    gbp_to_can = round(gbp_can.get_current_price(),3)
    prev_close_gbp_can = gbp_can.get_prev_close_price()
    return gbp_can, gbp_to_can, prev_close_gbp_can

##CADGBP=X
def cadgbp_x(c):
    can_gbp = YahooFinancials('CADGBP=X')
    can_to_gbp = round(can_gbp.get_current_price(),2)
    prev_close_can_gbp = can_gbp.get_prev_close_price()
    return can_gbp, can_to_gbp, prev_close_can_gbp