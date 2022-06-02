## Getting updated currency exchange data for CAN, USD, GBP

## loading the required libraries
import datetime
from datetime import timedelta

# pandas and numpy for data manipulation
import pandas as pd
import numpy as np

# matplotlib and seaborn for plotting graphs
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

## yahoo finance used to get the data
import yfinance as yf
from yahoofinancials import YahooFinancials

## streamlit
import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_option_menu import option_menu

## Plotly
import plotly.graph_objects as go

import emoji
import PIL
from PIL import Image

## Importing functions:
from currency_data_retrieval import gbpcad_x, cadgbp_x, usdcad_x, cadusd_x, eurcad_x, cadeur_x
from cad_eur_charts import eur_can_chart, can_eur_chart, usd_can_chart, can_usd_chart, gbp_can_chart, can_gbp_chart



## Getting today's date
today = datetime.datetime.today()
today_text = today.strftime("%A %B %d, %Y")

## Yesterdays Date:
yest_day = today - timedelta(days=1)

## 1 week ago
#last_week = today - timedelta(weeks=4)

## 3 months ago
#three_months_ago = today - \
#                   pd.offsets.DateOffset(months=3)

## Today's date, time and timezone
date_time_tz = today.astimezone().strftime("%A %B %d, %Y  %H:%M.%S %Z")

## Today's date and time
date_time = today.strftime("%A %B %d, %Y  %T")


#len_prices = len(eur_can.get_historical_price_data(str(three_months_ago.date()), str(today.date()), 'daily')['CADEUR=X']['prices'])


# #print("Euro to Canadian")
# eur_can = YahooFinancials('EURCAD=X')
# eur_to_can = eur_can.get_current_price()
# eur_to_can = round(eur_to_can,3)
# #print("Previous Close Price: Euro - Can")
# prev_close_eur_can = eur_can.get_prev_close_price()
# #print()
# #print("Canadian to Euro")
# can_eur = YahooFinancials('CADEUR=X')
# can_to_eur = can_eur.get_current_price()
# can_to_eur = round(can_to_eur,3)
# #print("Previous Close Price: Can - Eur")
# prev_close_can_eur = can_eur.get_prev_close_price()


#print("US to Canadian")
# usd_can = YahooFinancials('USDCAD=X')
# usd_to_can = usd_can.get_current_price()
# usd_to_can = round(usd_to_can,3)
# #print("Previous Close Price: USD - Can")
# prev_close_us_can = usd_can.get_prev_close_price()
# #print()
# #print("Canadian to US")
# can_us = YahooFinancials('CADUSD=X')
# can_to_us = can_us.get_current_price()
# can_to_us = round(can_to_us, 3)
# #print("Previous Close Price: CAN - USD")
# prev_close_can_us = can_us.get_prev_close_price()


#print("GBP to Canadian")
# gbp_can = YahooFinancials('GBPCAD=X')
# gbp_to_can = gbp_can.get_current_price()
# gbp_to_can = round(gbp_to_can,3)
# #print("Previous Close: GBP - CAN")
# prev_close_gbp_can = gbp_can.get_prev_close_price()
# #print()
# #print("CAN to GBP")
# can_gbp = YahooFinancials('CADGBP=X')
# can_to_gbp = can_gbp.get_current_price()
# can_to_gbp = round(can_to_gbp,3)
# prev_close_can_gbp = can_gbp.get_prev_close_price()

currencies = ['CADGBP=X','GBPCAD=X', 'CADUSD=X', 'USDCAD=X','CADEUR=X', 'EURCAD=X']

# def currency_prices(c):
#     closing_prices = []
#     dates = []
#     for i in range(0, len_prices):
#         close = eur_can.get_historical_price_data(str(three_months_ago.date()), str(today.date()), 'daily')[c]['prices'][i]['close']
#         date = eur_can.get_historical_price_data(str(three_months_ago.date()), str(today.date()), 'daily')[c]['prices'][i]['formatted_date']
#         closing_prices.append(round(close,3))
#         dates.append(date)
#
#     d2 = {"Date" : dates, "Closing Price" : closing_prices}
#     df3 = pd.DataFrame(d2)


#st.title("Enter Title Here:")

## Horizontal Menu Bar
choose = option_menu("Select to view updated exchange rate", ['CAN-EUR/EUR-CAN', 'CAN-US/US-CAN', 'CAN-GBP/GBP-CAN'],
                     icons=['currency-euro', 'currency-dollar', 'currency-pound'],
                     menu_icon="app-indicator", default_index=0,
                     styles={
                         "font" : {"color": "#F2E3D5"},
                         "container": {"padding": "5!important", "background-color": "#32A89C", "border-style": "none", "border-left-color" : "#00635A" },
                         "icon": {"color": "#F2E3D5", "font-size": "18px"},
                         "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "font-color" : "#F2E3D5",
                                      "--hover-color": "#00E3CC"},
                         "nav-link-selected": {"background-color": "#00635A"},
                     },
                     orientation='horizontal'
                     )

## Updating the currency echange based on selection:

if choose == 'CAN-EUR/EUR-CAN':
    eur_can, eur_to_can, prev_close_eur_can = eurcad_x("EURCAD=X")
    can_eur, can_to_eur, prev_close_can_eur = cadeur_x("CADEUR=X")

    eur_can_chart()
    can_eur_chart()

    image_1 = Image.open("images/euro_can_high_low_chart.png")
    image_2 = Image.open("images/can_euro_high_low_chart.png")

    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=eur_to_can,
        number={'prefix': "$"},
        delta={'position': 'bottom', 'reference': prev_close_eur_can},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    fig.update_layout(paper_bgcolor='#00635A',
                      font_family="Overpass",
                      font_color="white",
                      title_font_size=24,
                      font_size=24,
                      title={
                          'text': '💶 1 EUR to CAN',
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                          'font_family': 'Overpass',
                      })
    # fig.add_layout_image(
    #     xref='paper',
    #     yref='paper',
    #     x=-0.4,
    #     y=0.4,
    #     sizex=1.6,
    #     sizey=1.5,
    #     layer='above',
    #     source=Image.open('images/euro_can_high_low_chart.png')
    # )

    fig.update_traces(delta_decreasing_color='#00E3CC',
                      delta_increasing_color='#B3483D')

    fig2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=can_to_eur,
        number={'prefix': "€"},
        delta={'position': 'bottom', 'reference': prev_close_can_eur},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    fig2.update_layout(paper_bgcolor='#32A89C',
                       font_family="Overpass",
                       font_color="#184F4A",
                       font_size=24,
                       title_font_size=24,
                       title_font_color='white',
                       title={
                           'text': '🍁 1 CAN to EUR',
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font_family': 'Overpass',
                       },
                       )
    # fig2.add_layout_image(
    #     xref='paper',
    #     yref='paper',
    #     x=-0.4,
    #     y=0.4,
    #     sizex= 1.6,
    #     sizey= 1.5,
    #     layer='above',
    #     source = Image.open('images/euro_can_high_low_chart_dark.png')
    #)
    fig2.update_traces(delta_decreasing_color='#00E3CC',
                       delta_increasing_color='#B3483D')
    # fig2.add_annotation(dict(font=dict(color = 'lightgrey', size = 16, family = 'Arial'),
    #                          text = 'Change from previous day close',
    #                          x = 0.5,
    #                          y = 0.2,
    #                          xref = 'paper',
    #                          yref = 'paper',
    #                          showarrow = False
    # ))

    st.caption("🔺/🔻 Change from previous day close")
    col1, col2 = st.columns([1,1])

    with col1:
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    #st.expander

    radio = st.radio("Select to view yearly currency trend EURO and CAD", ["1 Year EUR-CAD Chart", "1 Year CAD-EUR Chart"])
    if radio == "1 Year EUR-CAD Chart":
        st.subheader("€1 EUR to CAD Yearly High vs Low")
        st.image(image_1,
                 use_column_width=True,
                 caption = "")

    if radio == "1 Year CAD-EUR Chart":
        st.subheader("$1 CAD to EUR Yearly High vs Low")
        st.image(image_2,
                 use_column_width=True,
                 caption = "")


    # c1, c2 = st.columns([1, 1])
    #
    # with c1:
    #     st.image(image_1,
    #     use_column_width = True,
    #     caption = "")
    #
    # with c2:
    #     st.image(image_2,
    #     use_column_width = True,
    #     caption = "")

    st.subheader(" ")

    c1, c2, c3 = st.columns([1, 4, 1])

    with c1:
        st.caption("")
    with c2:
        st.caption(f"Last Updated {date_time_tz}")
    with c3:
        st.caption("")


if choose == 'CAN-US/US-CAN':
    usd_can, usd_to_can, prev_close_us_can = usdcad_x("USDCAD=X")
    can_us, can_to_us, prev_close_can_us = cadusd_x("CADUSD=X")

    usd_can_chart()
    can_usd_chart()

    image_1 = Image.open("images/usd_can_high_low_chart.png")
    image_2 = Image.open("images/can_usd_high_low_chart.png")


    ## Plotly Indicator
    fig3 = go.Figure(go.Indicator(
        mode="number+delta",
        value=usd_to_can,
        number={'prefix': "$"},
        delta={'position': 'bottom', 'reference': prev_close_us_can},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))

    fig3.update_layout(paper_bgcolor='#00635A',
                      font_family="Overpass",
                      font_color="white",
                      title_font_size=24,
                      font_size=24,
                      title={
                          'text': '💵 1 US to CAN',
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                          'font_family': 'Overpass',
                      })

    fig3.update_traces(delta_decreasing_color='#00E3CC',
                      delta_increasing_color='#B3483D')

    fig4 = go.Figure(go.Indicator(
        mode="number+delta",
        value=can_to_us,
        number={'prefix': "$"},
        delta={'position': 'bottom', 'reference': prev_close_can_us},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))

    fig4.update_layout(paper_bgcolor='#32A89C',
                       font_family="Overpass",
                       font_color="#184F4A",
                       font_size=24,
                       title_font_size=24,
                       title_font_color='white',
                       title={
                           'text': '🍁 1 CAN to USD',
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font_family': 'Overpass',
                       },
                       )
    fig4.update_traces(delta_decreasing_color='#00E3CC',
                       delta_increasing_color='#B3483D')

    # fig4.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
    #                          text='Change from previous day close',
    #                          x=0.5,
    #                          y=0.2,
    #                          xref='paper',
    #                          yref='paper',
    #                          showarrow=False
    #                          ))
    st.title("Canadian to US exchange rates:")

    st.caption("🔺/🔻 Change from previous day close")

    col1, col2 = st.columns([1,1])

    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.plotly_chart(fig4, use_container_width=True)

    radio = st.radio("Select to view yearly currency trend USD and CAD",
                     ["1 Year USD-CAD Chart", "1 Year CAD-USD Chart"])

    if radio == "1 Year USD-CAD Chart":
        st.subheader("$1 USD to CAD Yearly High vs Low")
        st.image(image_1,
                 use_column_width=True,
                 caption="")

    if radio == "1 Year CAD-USD Chart":
        st.subheader("$1 CAD to USD Yearly High vs Low")
        st.image(image_2,
                 use_column_width=True,
                 caption="")

    # c1, c2 = st.columns([1, 1])
    #
    # with c1:
    #     st.image(image_1,
    #              use_column_width=True,
    #              caption="USD-CAD")
    #
    # with c2:
    #     st.image(image_2,
    #              use_column_width=True,
    #              caption="CAD-USD")

    c1, c2, c3 = st.columns([1, 3, 1])

    with c1:
        st.caption("")
    with c2:
        st.caption(f"Last Updated {date_time_tz}")
    with c3:
        st.caption("")


if choose == 'CAN-GBP/GBP-CAN':
    gbp_can, gbp_to_can, prev_close_gbp_can = gbpcad_x("GBPCAD=X")
    can_gbp, can_to_gbp, prev_close_can_gbp = cadgbp_x("CADGPD=X")

    gbp_can_chart()
    can_gbp_chart()

    image_1 = Image.open("images/gbp_can_high_low_chart.png")
    image_2 = Image.open("images/can_gbp_high_low_chart.png")

    ## Plotly Indicator
    fig5 = go.Figure(go.Indicator(
        mode="number+delta",
        value=gbp_to_can,
        number={'prefix': "$"},
        delta={'position': 'bottom', 'reference': prev_close_gbp_can},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    fig5.update_layout(paper_bgcolor='#00635A',
                      font_family="Overpass",
                      font_color="white",
                      title_font_size=24,
                      font_size=24,
                      title={
                          'text': '💷 1 GBP to CAN',
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top',
                          'font_family': 'Overpass',
                      })
    fig5.update_traces(delta_decreasing_color='#00E3CC',
                      delta_increasing_color='#B3483D')

    fig6 = go.Figure(go.Indicator(
        mode="number+delta",
        value=can_to_gbp,
        number={'prefix': "£"},
        delta={'position': 'bottom', 'reference': prev_close_can_gbp},
        domain={'x': [0, 1], 'y': [0, 1]}
    ))
    fig6.update_layout(paper_bgcolor='#32A89C',
                       font_family="Overpass",
                       font_color="#184F4A",
                       font_size=24,
                       title_font_size=24,
                       title_font_color='white',
                       title={
                           'text': '🍁 1 CAN to GBP',
                           'y': 0.9,
                           'x': 0.5,
                           'xanchor': 'center',
                           'yanchor': 'top',
                           'font_family': 'Overpass',
                       },
                       )
    fig6.update_traces(delta_decreasing_color='#00E3CC',
                       delta_increasing_color='#B3483D')
    # fig6.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
    #                          text='Change from previous day close',
    #                          x=0.5,
    #                          y=0.2,
    #                          xref='paper',
    #                          yref='paper',
    #                          showarrow=False
    #                          ))

    st.title('Canadian to GBP exchange rates')

    st.caption("🔺/🔻 Change from previous day close")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.plotly_chart(fig5, use_container_width=True)
    with col2:
        st.plotly_chart(fig6, use_container_width=True)

    radio = st.radio("Select to view yearly trend", ["1 Year GBP-CAD Chart", "1 Year CAD-GBP Chart"])

    if radio == "1 Year GBP-CAD Chart":
        st.subheader("£1 GBP to CAD Yearly High vs Low")
        st.image(image_1,
                 use_column_width=True)

    if radio == "1 Year CAD-GBP Chart":
        st.subheader("$1 CAD to GBP Yearly High vs Low")
        st.image(image_2,
                 use_column_width=True)

    # c1, c2 = st.columns([1,1])
    #
    # with c1:
    #     st.image(image_1,
    #              use_column_width=True,
    #              caption="GBP-CAD")
    #
    # with c2:
    #     st.image(image_2,
    #              use_column_width=True,
    #              caption="CAD-GBP")

    st.caption("")

    c1,c2,c3 = st.columns([1, 3, 1])

    with c1:
        st.caption("")
    with c2:
        st.caption(f"Last Updated {date_time_tz}")
    with c3:
        st.caption("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(today)


