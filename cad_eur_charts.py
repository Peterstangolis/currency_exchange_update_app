## CAD and EUR line charts

## Import libraries

## Libraries
from datetime import datetime, timedelta
import datetime

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import yfinance as yf

from currency_data_retrieval import gbpcad_x, cadgbp_x, usdcad_x, cadusd_x, eurcad_x, cadeur_x


#can_eur, can_to_eur, prev_close_can_eur = cadeur_x("CADEUR=X")


def eur_can_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                   pd.offsets.DateOffset(years=1)
    eur_can, eur_to_can, prev_close_eur_can = eurcad_x("EURCAD=X")

    df = yf.download("EURCAD=X",
                     start=one_year_ago,
                     end=today,
                     progress=False)
    df = df[["Close"]]

    eur_cad_df = df.reset_index()

    eur_can_yr_low_index = list(eur_cad_df.loc[eur_cad_df["Close"] == eur_cad_df["Close"].max()].index)[0]
    eur_can_yr_high_index = list(eur_cad_df.loc[eur_cad_df["Close"] == eur_cad_df["Close"].min()].index)[0]

    eur_can_yr_high_date = eur_cad_df.iloc[eur_can_yr_high_index, :]["Date"].date()
    eur_can_yr_high_value = round(eur_cad_df.iloc[eur_can_yr_high_index, :]["Close"], 3)

    eur_can_yr_low_date = eur_cad_df.iloc[eur_can_yr_low_index, :]["Date"].date()
    eur_can_yr_low_value = round(eur_cad_df.iloc[eur_can_yr_low_index, :]["Close"], 3)

    ## Euro to Canadian Line Chart
    bbox_props = dict(boxstyle='Round,pad=0.4', fc='#42DBCC', lw=1,
                      edgecolor=None,
                      alpha=0.7)

    plt.plot(eur_cad_df["Date"], eur_cad_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.annotate(f"${eur_can_yr_high_value}\n{eur_can_yr_high_date.strftime('%d %b, %y')}",
                 xytext=(eur_can_yr_high_date - datetime.timedelta(days=23), eur_can_yr_high_value + 0.055),
                 xy=(eur_can_yr_high_date, eur_can_yr_high_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#00E3CC')
                 )

    plt.annotate(f"${eur_can_yr_low_value}\n{eur_can_yr_low_date.strftime('%d %b, %y')}",
                 xytext=(eur_can_yr_low_date - datetime.timedelta(days=60), eur_can_yr_low_value + 0.0133),
                 xy=(eur_can_yr_low_date, eur_can_yr_low_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=0.2",
                                 color='#00E3CC'))

    # plt.annotate(" €1 Euro to Can \n Yearly High vs Low",
    #              xy=(eur_can_yr_low_date - datetime.timedelta(days=55), 1.355),
    #              size=15,
    #              color='#00635A',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold',
    #              bbox=None)

    plt.savefig('images/euro_can_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();


def can_eur_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                   pd.offsets.DateOffset(years=1)
    can_eur, can_to_eur, prev_close_can_eur = cadeur_x("CADEUR=X")

    closing_prices2 = []
    dates2 = []

    df = yf.download("CADEUR=X",
                     start=one_year_ago,
                     end=today,
                     progress=False)
    df = df[["Close"]]

    cad_eur_df = df.reset_index()

    can_eur_yr_low_index = list(cad_eur_df.loc[cad_eur_df["Close"] == cad_eur_df["Close"].max()].index)[0]
    can_eur_yr_high_index = list(cad_eur_df.loc[cad_eur_df["Close"] == cad_eur_df["Close"].min()].index)[0]

    can_eur_date_yr_low = cad_eur_df.iloc[can_eur_yr_low_index, :]["Date"].date() + datetime.timedelta(days=0)
    can_eur_value_yr_low = round(cad_eur_df.iloc[can_eur_yr_low_index, :]["Close"], 3)

    can_eur_date_yr_high = cad_eur_df.iloc[can_eur_yr_high_index, :]["Date"].date() + datetime.timedelta(days=5)
    can_eur_value_yr_high = round(cad_eur_df.iloc[can_eur_yr_high_index, :]["Close"], 3)

    plt.plot(cad_eur_df["Date"], cad_eur_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.annotate(f"€{can_eur_value_yr_high}\n{can_eur_date_yr_high.strftime('%d %b, %y')}",
                 xytext=(can_eur_date_yr_high + datetime.timedelta(days=33), can_eur_value_yr_high + 0.005),
                 xy=(can_eur_date_yr_high, can_eur_value_yr_high),
                 xycoords="data",
                 textcoords="data",
                 color='#004A44',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#004A44')
                 )

    plt.annotate(f"€{can_eur_value_yr_low}\n{can_eur_date_yr_low.strftime('%d %b, %y')}",
                 xytext=(can_eur_date_yr_low + datetime.timedelta(days=25), can_eur_value_yr_low - 0.0233),
                 xy=(can_eur_date_yr_low, can_eur_value_yr_low),
                 xycoords="data",
                 textcoords="data",
                 color='#004A44',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=0.2",
                                 color='#004A44'))

    # plt.annotate(" $1 CAN to EURO \n Yearly High vs Low",
    #              xy=(can_eur_date_yr_low - datetime.timedelta(days=365), 0.739),
    #              size=15,
    #              color='#004A44',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold')

    plt.tight_layout()
    plt.savefig('images/can_euro_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();


## USD - CAD Chart ###
def usd_can_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                   pd.offsets.DateOffset(years=1)
    usd_cad, usd_to_cad, prev_close_usd_cad = usdcad_x("USDCAD=X")

    df = yf.download("USDCAD=X",
                     start=one_year_ago,
                     end=today,
                     progress=False)
    df = df[["Close"]]

    usd_cad_df = df.reset_index()

    usd_can_yr_low_index = list(usd_cad_df.loc[usd_cad_df["Close"] == usd_cad_df["Close"].max()].index)[0]
    usd_can_yr_high_index = list(usd_cad_df.loc[usd_cad_df["Close"] == usd_cad_df["Close"].min()].index)[0]

    usd_can_yr_high_date = usd_cad_df.iloc[usd_can_yr_high_index, :]["Date"].date()
    usd_can_yr_high_value = round(usd_cad_df.iloc[usd_can_yr_high_index, :]["Close"], 3)

    usd_can_yr_low_date = usd_cad_df.iloc[usd_can_yr_low_index, :]["Date"].date()
    usd_can_yr_low_value = round(usd_cad_df.iloc[usd_can_yr_low_index, :]["Close"], 3)

    plt.plot(usd_cad_df["Date"], usd_cad_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.annotate(f"${usd_can_yr_high_value}\n{usd_can_yr_high_date.strftime('%d %b, %y')}",
                 xytext=(usd_can_yr_high_date + datetime.timedelta(days=23), usd_can_yr_high_value - 0.005),
                 xy=(usd_can_yr_high_date, usd_can_yr_high_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#00635A')
                 )

    plt.annotate(f"${usd_can_yr_low_value}\n{usd_can_yr_low_date.strftime('%d %b, %y')}",
                 xytext=(usd_can_yr_low_date + datetime.timedelta(days=50), usd_can_yr_low_value - 0.0103),
                 xy=(usd_can_yr_low_date, usd_can_yr_low_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=0.2",
                                 color='#00635A'))

    # plt.annotate(" $1 USD to CAN \n Yearly High vs Low",
    #              xy=(usd_can_yr_low_date + datetime.timedelta(days=0), 1.21),
    #              size=15,
    #              color='#00E3CC',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold',
    #              bbox=None)

    plt.savefig('images/usd_can_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();

###  CAD - USD Chart  ###
def can_usd_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                   pd.offsets.DateOffset(years=1)
    can_us, can_to_us, prev_close_can_us = cadusd_x("CADUSD=X")

    df = yf.download("CADUSD=X",
                     start=one_year_ago,
                     end=today,
                     progress=False)
    df = df[["Close"]]

    usd_cad_df = df.reset_index()

    usd_can_yr_low_index = list(usd_cad_df.loc[usd_cad_df["Close"] == usd_cad_df["Close"].max()].index)[0]
    usd_can_yr_high_index = list(usd_cad_df.loc[usd_cad_df["Close"] == usd_cad_df["Close"].min()].index)[0]

    usd_can_yr_high_date = usd_cad_df.iloc[usd_can_yr_high_index, :]["Date"].date()
    usd_can_yr_high_value = round(usd_cad_df.iloc[usd_can_yr_high_index, :]["Close"], 3)

    usd_can_yr_low_date = usd_cad_df.iloc[usd_can_yr_low_index, :]["Date"].date()
    usd_can_yr_low_value = round(usd_cad_df.iloc[usd_can_yr_low_index, :]["Close"], 3)

    plt.plot(usd_cad_df["Date"], usd_cad_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.annotate(f"${usd_can_yr_high_value}\n{usd_can_yr_high_date.strftime('%d %b, %y')}",
                 xytext=(usd_can_yr_high_date + datetime.timedelta(days=23), usd_can_yr_high_value - 0.005),
                 xy=(usd_can_yr_high_date, usd_can_yr_high_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=11,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#00635A')
                 )

    plt.annotate(f"${usd_can_yr_low_value}\n{usd_can_yr_low_date.strftime('%d %b, %Y')}",
                 xytext=(usd_can_yr_low_date + datetime.timedelta(days=60), usd_can_yr_low_value - 0.0133),
                 xy=(usd_can_yr_low_date, usd_can_yr_low_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=11,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=0.2",
                                 color='#00635A'))

    # plt.annotate(" $1 CAD to USD \n Yearly High vs Low",
    #              xy=(usd_can_yr_low_date + datetime.timedelta(days=340), .82),
    #              size=15,
    #              color='#00635A',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold',
    #              bbox=None)

    plt.savefig('images/can_usd_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();

### GBP - CAD Chart ###
def gbp_can_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                    pd.offsets.DateOffset(years=1)
    gbp_can, gbp_to_can, prev_close_gbp_can = gbpcad_x("GBPCAD=X")

    df = yf.download("GBPCAD=X",
                    start=one_year_ago,
                    end=today,
                    progress=False)
    df = df[["Close"]]
    gbp_cad_df = df.reset_index()

    gbp_can_yr_low_index = list(gbp_cad_df.loc[gbp_cad_df["Close"] == gbp_cad_df["Close"].max()].index)[0]
    gbp_can_yr_high_index = list(gbp_cad_df.loc[gbp_cad_df["Close"] == gbp_cad_df["Close"].min()].index)[0]

    gbp_can_yr_high_date = gbp_cad_df.iloc[gbp_can_yr_high_index, :]["Date"].date()
    gbp_can_yr_high_value = round(gbp_cad_df.iloc[gbp_can_yr_high_index, :]["Close"], 3)

    gbp_can_yr_low_date = gbp_cad_df.iloc[gbp_can_yr_low_index, :]["Date"].date()
    gbp_can_yr_low_value = round(gbp_cad_df.iloc[gbp_can_yr_low_index, :]["Close"], 3)

    plt.plot(gbp_cad_df["Date"], gbp_cad_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.annotate(f"${gbp_can_yr_high_value}\n{gbp_can_yr_high_date.strftime('%d %b, %y')}",
                 xytext=(gbp_can_yr_high_date - datetime.timedelta(days=113), gbp_can_yr_high_value + 0.025),
                 xy=(gbp_can_yr_high_date, gbp_can_yr_high_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad= 0.3",
                                 color='#00635A')
                 )

    plt.annotate(f"${gbp_can_yr_low_value}\n{gbp_can_yr_low_date.strftime('%d %b, %y')}",
                 xytext=(gbp_can_yr_low_date + datetime.timedelta(days=42), gbp_can_yr_low_value - 0.0103),
                 xy=(gbp_can_yr_low_date, gbp_can_yr_low_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad= 0.3",
                                 color='#00635A'))

    # plt.annotate(" £1 GBP to CAD \n Yearly High vs Low",
    #              xy=(gbp_can_yr_low_date - datetime.timedelta(days=85), 1.583),
    #              size=15,
    #              color='#00635A',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold',
    #              bbox=None)

    plt.savefig('images/gbp_can_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();

### CAD - GBP Chart  ###
def can_gbp_chart():
    today = datetime.datetime.today()
    one_year_ago = today - \
                   pd.offsets.DateOffset(years=1)
    can_gbp, can_to_gbp, prev_close_can_gbp = cadgbp_x("CADGPD=X")

    df = yf.download("CADGBP=X",
                     start=one_year_ago,
                     end=today,
                     progress=False)
    df = df[["Close"]]

    cad_gbp_df = df.reset_index()

    can_gbp_yr_low_index = list(cad_gbp_df.loc[cad_gbp_df["Close"] == cad_gbp_df["Close"].max()].index)[0]
    can_gbp_yr_high_index = list(cad_gbp_df.loc[cad_gbp_df["Close"] == cad_gbp_df["Close"].min()].index)[0]

    can_gbp_yr_high_date = cad_gbp_df.iloc[can_gbp_yr_high_index, :]["Date"].date()
    can_gbp_yr_high_value = round(cad_gbp_df.iloc[can_gbp_yr_high_index, :]["Close"], 3)

    can_gbp_yr_low_date = cad_gbp_df.iloc[can_gbp_yr_low_index, :]["Date"].date()
    can_gbp_yr_low_value = round(cad_gbp_df.iloc[can_gbp_yr_low_index, :]["Close"], 3)

    #fig = plt.figure()
    #fig.patch.set_facecolor("yellow")

    plt.plot(cad_gbp_df["Date"], cad_gbp_df["Close"],
             color='#00635A')
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.annotate(f"£{can_gbp_yr_high_value}\n{can_gbp_yr_high_date.strftime('%d %b, %y')}",
                 xytext=(can_gbp_yr_high_date + datetime.timedelta(days=23), can_gbp_yr_high_value - 0.005),
                 xy=(can_gbp_yr_high_date, can_gbp_yr_high_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#00635A')
                 )

    plt.annotate(f"£{can_gbp_yr_low_value}\n{can_gbp_yr_low_date.strftime('%d %b, %y')}",
                 xytext=(can_gbp_yr_low_date - datetime.timedelta(days=130), can_gbp_yr_low_value - 0.0103),
                 xy=(can_gbp_yr_low_date, can_gbp_yr_low_value),
                 xycoords="data",
                 textcoords="data",
                 color='#00635A',
                 size=12,
                 weight='normal',
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3, rad=-0.3",
                                 color='#00635A'))

    # plt.annotate(" $1 CAD to GBP \n Yearly High vs Low",
    #              xy=(can_gbp_yr_low_date - datetime.timedelta(days=355), 0.63),
    #              size=15,
    #              color='#00E3CC',
    #              horizontalalignment='left',
    #              verticalalignment='center',
    #              weight='bold',
    #              bbox=None)



    plt.savefig('images/can_gbp_high_low_chart.png',
                bbox_inches='tight',
                dpi=140,
                facecolor='#C9F0DB',
                transparent=True)
    plt.close();
