import sys
sys.path.insert(0, '../')
from bibliotecas import base_estudantes, job, magalu, alunos, petrobras, sns, np, pd, plt, yf, px, go, sp, wn, quandl, date, db, geobr, gpd, os
wn.filterwarnings('ignore')
import pmdarima
import streamlit as st

# @st.cache
def plot(temp):
    f = go.Figure(data=[
    go.Candlestick(
        x=temp.index,
        open= temp['Open'],
        high=temp['High'],
        low=temp['Low'],
        close=temp['Close'],
        showlegend=False
    )
    ])

    lay = go.Layout(
        yaxis_tickformat='$',
        xaxis=dict(rangeslider=dict(visible=False))
    )

    f.update_layout(lay)

    # f.show()
    
    return f


def main():
    st.set_page_config(page_title='Luis')  
    st.title('Graf')  
    btc = yf.Ticker('BTC-USD').history(period='max')[['Open', 'Close', 'High', 'Low', 'Volume']]
    temp = btc['2021-1-1':]
    fig = plot(temp)

    if st.checkbox('Gostou?'):
        st.write('Valeu')
        moving = temp.rolling(2).mean() #media movel a cada 2 registros
        fig.add_trace(
            go.Scatter(
                x=moving.index,
                y=moving['Close'].values,
                line= dict(color= 'black')
            )
        )

    st.plotly_chart(fig) #mostra a figura

    with st.expander('Infos de open'):
        st.text("muitos dados")

main()
# streamlit run 