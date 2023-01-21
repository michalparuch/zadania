import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pad Lab_06", layout="wide")

st.sidebar.title("Menu")
page = st.sidebar.selectbox("Wybór aplikacji", ["Ankieta", "Staty"])

if page == "Ankieta":
    st.title("Ankieta")
    name = st.text_input("Imię")
    surname = st.text_input("Nazwisko")
    if st.button("Zapisz"):
        st.success("Kwestionariusz poprawnie zapisany!")

elif page == "Staty":
    st.title("Statystyki")
    data = st.file_uploader("Wybierz plik csv", type="csv")
    if data is not None:
        import time
        with st.spinner("Wczytywanie danych..."):
            time.sleep(3)
        st.success("Zakończono!")
        df = pd.read_csv(data)
        st.dataframe(df.head(10))

        chart_type = st.selectbox("Wybierz typ wykresu", ["SCATTER", "BAR CHART"])
        if chart_type == "SCATTER":
            fig = px.scatter(data_frame=df, x='BasePay', y='TotalPayBenefits',
            labels={'BasePay':'Base Pay', 'TotalPayBenefits':'Total Pay and Benefits'},
            title='Base Pay vs Total Pay and Benefits', width=1000, height=500)
            st.plotly_chart(fig)

        if chart_type == "BAR CHART":
            fig = px.bar(data_frame=df, x='JobTitle', y='TotalPay',
            labels={'Year':'Year', 'TotalPay':'Total Pay'},
            title='Total Pay by Year', width=1000, height=500)
            st.plotly_chart(fig)