import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from pathlib import Path


def tabel_musim(df):
    tb_musim = df.groupby(by="season").instant.nunique().reset_index()
    tb_musim.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return tb_musim





def tabel_harilibur(df):
    tb_libur = df.groupby(by="holiday").instant.nunique().reset_index()
    tb_libur.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return tb_libur


def tabel_harikerja(df):
    tb_kerja = df.groupby(by="workingday").instant.nunique().reset_index()
    tb_kerja.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return tb_kerja


def tabel_cuaca(df):
    tb_cuaca = df.groupby(by="weathersit").instant.nunique().reset_index()
    tb_cuaca.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return tb_cuaca


def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:

        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Rentang Waktu",
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date],
            on_change=on_change
        )

    return date


def musim(df):
    st.subheader("Season")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="season",
        y="sum",
        data=df.sort_values(by="season", ascending=False),
        ax=ax
    )
    ax.set_title("Jumlah Bike Sharing Berdasarkan Musim", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)




def harilibur(df):
    st.subheader("Holiday")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="holiday",
        y="sum",
        data=df.sort_values(by="holiday", ascending=False),
        ax=ax
    )
    ax.set_title("Jumlah Bike Sharing pada Hari libur", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def harikerja(df):
    st.subheader("Working Day")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="workingday",
        y="sum",
        data=df.sort_values(by="workingday", ascending=False),
        ax=ax
    )
    ax.set_title("Jumlah Bike Sharing pada Hari kerja", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


def cuaca(df):
    st.subheader("Weather Sit")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="weathersit",
        y="sum",
        data=df.sort_values(by="weathersit", ascending=False),
        ax=ax
    )
    ax.set_title("Jumlah Bike Sharing Berdasarkan Cuaca", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)


if __name__ == "__main__":
    sns.set(style="dark")

    st.header("Bike Sharing Dashboard :bike:")

    day_df_csv = Path(__file__).parents[1] / 'dashboard/dashboard_daynew.csv'

    day_df = pd.read_csv(day_df_csv)

    date = sidebar(day_df)
    if (len(date) == 2):
        main_df = day_df[(day_df["dteday"] >= str(date[0])) & (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[
            (day_df["dteday"] >= str(st.session_state.date[0])) & (day_df["dteday"] <= str(st.session_state.date[1]))]

    season_df = tabel_musim(main_df)
    musim(season_df)
    holiday_df = tabel_harilibur(main_df)
    harilibur(holiday_df)
    workingday_df = tabel_harikerja(main_df)
    harikerja(workingday_df)
    weathersit_df = tabel_cuaca(main_df)
    cuaca(weathersit_df)

