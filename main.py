## Getting updated currency exchange data for CAN, USD, GBP

## loading the required libraries
import datetime
from datetime import timedelta

# pandas and numpy for data manipulation
import pandas as pd
import numpy as np


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

## Today's date, time and timezone
date_time_tz = today.astimezone().strftime("%A %B %d, %Y  %H:%M.%S %Z")

## Today's date and time
date_time = today.strftime("%A %B %d, %Y  %T")

## Emojis
can = '🇨🇦'
usa = '🇺🇸'
gb = '🇬🇧'
europe = '🇪🇺'


currencies = ['CADGBP=X','GBPCAD=X', 'CADUSD=X', 'USDCAD=X','CADEUR=X', 'EURCAD=X']

## Attributions:




#st.title("Enter Title Here:")
st.set_page_config(
                   page_title="CAD to USD & EUR CONVERSION",
                   page_icon="💵")

## Horizontal Menu Bar
choose = option_menu("Select to view updated exchange rate", ['CAD-EUR', 'CAD-USD', 'CAD-GBP'],
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

if choose == 'CAD-EUR':
    eur_can, eur_to_can, prev_close_eur_can = eurcad_x("EURCAD=X")
    can_eur, can_to_eur, prev_close_can_eur = cadeur_x("CADEUR=X")

    st.title('CAD to EUR exchange rates')

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


    fig.update_traces(delta_decreasing_color='#B3483D',
                      delta_increasing_color='#00E3CC')
    fig.add_annotation(dict(font=dict(color = 'lightgrey', size = 16, family = 'Arial'),
                             text = f'€1 Euro will return ${eur_to_can} Canadian',
                             x = 0.5,
                             y = 0,
                             xref = 'paper',
                             yref = 'paper',
                             showarrow = False
    ))

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

    fig2.update_traces(delta_decreasing_color='#B3483D',
                       delta_increasing_color='#00E3CC')
    fig2.add_annotation(dict(font=dict(color = 'lightgrey', size = 16, family = 'Arial'),
                             text = f'$1 Canadian will return €{can_to_eur} Euro',
                             x = 0.5,
                             y = 0,
                             xref = 'paper',
                             yref = 'paper',
                             showarrow = False
    ))

    st.caption("🔺/🔻 Change from previous day close")
    col1, col2 = st.columns([1,1])

    with col1:
        st.plotly_chart(fig, use_container_width=True)
        #st.caption("Testing the caption for this column-1")
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
        #st.caption("testing the caption for this column-2")


    st.sidebar.subheader("Currency Exchange Calculator")

    #st.sidebar.write(f"{can} {europe}")
    with st.sidebar:
        col3, col4 = st.columns((1,1))
        with col3:
            st.image("images/cad_coin.png", width=70)
            st.write(f"{can}")
        with col4:
            st.image("images/eur_coin3.png", width=80)
            st.write(f"{europe}")
    value = st.sidebar.slider("Select amount to exchange",
                        min_value=1,
                        max_value=1000,
                        value=100,
                        step=1, key="exchange")
    column1, column2 = st.columns([1, 1])
    new_eur_can = round(value * eur_to_can, 2)
    eur_can_text = '<p style="color:#ABE1CA; font-weight:600; font-size:18px;">€{value} EUR is equal to: ${new_eur_can} CAD</p>'.format(value = value, new_eur_can = new_eur_can)

    with column1:
        st.sidebar.markdown(eur_can_text, unsafe_allow_html=True)
        #st.sidebar.subheader(f"€{value} EUR is equal to: ${round(value * eur_to_can, 3)}CAD ")
        #st.sidebar.subheader(f"${round(value * eur_to_can, 3)} Canadian dollars")

    with column2:
        st.sidebar.subheader(f"${value} CAD is equal to: €{round(value * can_to_eur,2)} Euros")
        #st.sidebar.subheader(f"€{round(value * can_to_eur,2)} Euros")


    with st.expander("Expand to view a chart of yearly exchange rate values"):
        eur_can_chart()
        can_eur_chart()
        radio = st.radio("Select to view yearly currency trend EURO and CAD", ["1 Year EUR-CAD Chart", "1 Year CAD-EUR Chart"])

        if radio == "1 Year EUR-CAD Chart":
            image_1 = Image.open("images/euro_can_high_low_chart.png")

            st.subheader("€1 EUR to CAD Yearly High vs Low")
            st.image(image_1,
                     use_column_width=True,
                     caption = "")

        if radio == "1 Year CAD-EUR Chart":
            image_2 = Image.open("images/can_euro_high_low_chart.png")

            st.subheader("$1 CAD to EUR Yearly High vs Low")
            st.image(image_2,
                     use_column_width=True,
                     caption = "")



    st.subheader(" ")

    c1, c2, c3 = st.columns([1, 4, 1])

    with c1:
        st.caption("")
    with c2:
        st.caption(f"Last Updated {date_time_tz}")
    with c3:
        st.caption("")


    st.sidebar.markdown("""
    
    
    """)

    st.sidebar.markdown('')
    st.sidebar.write("Select button below to clear the stored data and retrieve the latest currency exchange rates from YahooFinancials")
    clear_data = st.sidebar.button("Clear stored data")
    if clear_data:
        cadeur_x.clear()
        eurcad_x.clear()

    st.sidebar.markdown("""___
    """)


    with st.sidebar.expander(
        emoji.emojize(':information:  About App')
    ):
        st.markdown(f"""
        > A currency exchange app that retrieves data from the [yfinance](https://pypi.org/project/yfinance/) & [yahoofinancials](https://pypi.org/project/yahoofinancials/) python libraries.
        > It currently works with the exchange of the {can} dollar to {europe} | {usa} | {gb} & 🔙.
        """)
        st.caption(f"©️ stanalytics, {datetime.datetime.today().strftime('%Y')}")


if choose == 'CAD-USD':
    usd_can, usd_to_can, prev_close_us_can = usdcad_x("USDCAD=X")
    can_us, can_to_us, prev_close_can_us = cadusd_x("CADUSD=X")


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

    fig3.update_traces(delta_decreasing_color='#B3483D',
                      delta_increasing_color='#00E3CC')
    fig3.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
                             text=f'$1 US Dollar will return ${usd_to_can} Canadian',
                             x=0.5,
                             y=0,
                             xref='paper',
                             yref='paper',
                             showarrow=False
                             ))

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
    fig4.update_traces(delta_decreasing_color='#B3483D',
                       delta_increasing_color='#00E3CC')

    fig4.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
                             text=f'$1 Canadian will return ${round(can_to_us,3)} US',
                             x=0.5,
                             y=0,
                             xref='paper',
                             yref='paper',
                             showarrow=False
                             ))
    st.title("CAD to USD exchange rates")

    st.caption("🔺/🔻 Change from previous day close")

    col1, col2 = st.columns([1,1])

    with col1:
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        st.plotly_chart(fig4, use_container_width=True)

    st.sidebar.subheader("Currency Exchange Calculator")
    #st.sidebar.write(f"{can} {usa}")
    with st.sidebar:
        col5, col6 = st.columns((1,1))
        with col5:
            st.image("images/cad_coin.png", width=70)
            st.write(f"{can}")
        with col6:
            st.image("images/usd_coin.png", width=75)
            st.write(f"{usa}")


    value = st.sidebar.slider("Select amount to exchange",
                      min_value=1,
                      max_value=1000,
                      value=100,
                      step=1, key="exchange")

    column1, column2 = st.sidebar.columns([1, 1])
    new_us_can = round(value * usd_to_can,2)
    us_can_text = '<p style="color:#ABE1CA; font-weight:600; font-size:18px;">${value} USD is equal to: ${new_us_can} CAD</p>'.format(value = value, new_us_can = new_us_can)

    with column1:
        st.sidebar.markdown(us_can_text, unsafe_allow_html=True)
        #st.sidebar.subheader(f"$ {value} USD is equal to  {round(value*usd_to_can,3)} CAD")

    with column2:
        st.sidebar.subheader(f"$ {value} CAD is equal to  {round(value*can_to_us,3)} USD")

    st.sidebar.markdown("""___
      """)
    st.sidebar.markdown('')
    st.sidebar.write(
        "Select button below to clear the stored data and retrieve the latest currency exchange rates from YahooFinancials")
    clear_data = st.sidebar.button("Clear stored data")
    if clear_data:
        cadusd_x.clear()
        usdcad_x.clear()

    with st.expander("Expand to view a chart of yearly exchange rate values"):

        radio = st.radio("Select to view yearly currency trend USD and CAD",
                         ["1 Year USD-CAD Chart", "1 Year CAD-USD Chart"])
        can_usd_chart()
        usd_can_chart()

        if radio == "1 Year USD-CAD Chart":
            image_1 = Image.open("images/usd_can_high_low_chart.png")

            st.subheader("$1 USD to CAD Yearly High vs Low")
            st.image(image_1, use_column_width=True)

        if radio == "1 Year CAD-USD Chart":
            image_2 = Image.open("images/can_usd_high_low_chart.png")

            st.subheader("$1 CAD to USD Yearly High vs Low")
            st.image(image_2, use_column_width=True)


    c1, c2, c3 = st.columns([1, 3, 1])

    with c1:
        st.caption("")
    with c2:
        st.caption(f"Last Updated {date_time_tz}")
    with c3:
        st.caption("")


if choose == 'CAD-GBP':
    gbp_can, gbp_to_can, prev_close_gbp_can = gbpcad_x("GBPCAD=X")
    can_gbp, can_to_gbp, prev_close_can_gbp = cadgbp_x("CADGPD=X")

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
    fig5.update_traces(delta_decreasing_color='#B3483D',
                      delta_increasing_color='#00E3CC')
    fig5.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
                             text=f'£1 will return ${round(gbp_to_can, 3)} Canadian',
                             x=0.5,
                             y=0,
                             xref='paper',
                             yref='paper',
                             showarrow=False
                             ))


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
    fig6.update_traces(delta_decreasing_color='#B3483D',
                       delta_increasing_color='#00E3CC')
    fig6.add_annotation(dict(font=dict(color='lightgrey', size=16, family='Arial'),
                             text=f'$1 Canadian will return £{round(can_to_gbp, 3)} British pounds ',
                             x=0.5,
                             y=0,
                             xref='paper',
                             yref='paper',
                             showarrow=False
                             ))

    st.title('CAD to GBP exchange rates')

    st.caption("🔺/🔻 Change from previous day close")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.plotly_chart(fig5, use_container_width=True)
    with col2:
        st.plotly_chart(fig6, use_container_width=True)

    st.sidebar.subheader("Currency Exchange Calculator")
    #st.sidebar.write(f"{can} {gb}")
    with st.sidebar:
        col7, col8 = st.columns((1,1))
        with col7:
            st.image("images/cad_coin.png", width=70)
            st.write(f"{can}")
        with col8:
            st.image("images/gbd_coin.png", width=75)
            st.write(f"{gb}")

    value = st.sidebar.slider("Select amount to exchange",
              min_value=1,
              max_value=1000,
              value=100,
              step=1, key="exchange")
    column1, column2 = st.sidebar.columns([1,1])

    new_gbp_can = round(value * gbp_to_can,2)
    gbd_can_text = '<p style="color:#ABE1CA; font-weight:600; font-size:18px;">£{value} GBP is equal to: ${new_gbp_can} CAD</p>'.format(value = value, new_gbp_can = new_gbp_can)

    with column1:
        st.sidebar.markdown(gbd_can_text, unsafe_allow_html=True)
        #st.sidebar.subheader(f"£{value} GBP is equal to: ${round(value*gbp_to_can,2)} CAD")

    with column2:
        st.sidebar.subheader(f"${value} CAD is equal to: £{round(value*can_to_gbp,2)} GBP")

    st.sidebar.markdown("""___
       """)
    st.sidebar.markdown('')
    st.sidebar.write(
        "Select button below to clear the stored data and retrieve the latest currency exchange rates from YahooFinancials")
    clear_data = st.sidebar.button("Clear stored data")
    if clear_data:
        cadgbp_x.clear()
        gbpcad_x.clear()

    with st.expander("Expand to view a chart of yearly exchange rate values"):
        radio = st.radio("Select to view yearly trend", ["1 Year GBP-CAD Chart", "1 Year CAD-GBP Chart"])
        gbp_can_chart()
        can_gbp_chart()

        if radio == "1 Year GBP-CAD Chart":
            image_1 = Image.open("images/gbp_can_high_low_chart.png")

            st.subheader("£1 GBP to CAD Yearly High vs Low")
            st.image(image_1, use_column_width=True)

        if radio == "1 Year CAD-GBP Chart":
            image_2 = Image.open("images/can_gbp_high_low_chart.png")

            st.subheader("$1 CAD to GBP Yearly High vs Low")
            st.image(image_2, use_column_width=True)



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


