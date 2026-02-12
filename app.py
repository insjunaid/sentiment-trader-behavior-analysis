import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sentiment vs Trader Performance", layout="wide")

st.title("Market Sentiment vs Trader Performance Dashboard")

# Load Processed Dataset

@st.cache_data
def load_data():
    return pd.read_csv("merged_data.csv")

data = load_data()


# Sidebar Filters

st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment Regime",
    options=data['Classification'].unique(),
    default=data['Classification'].unique()
)

filtered = data[data['Classification'].isin(sentiment_filter)]

# KPI Metrics

st.subheader(" Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(filtered))
col2.metric("Average PnL", round(filtered['Closed PnL'].mean(), 2))
col3.metric("Average Trade Size", round(filtered['Size USD'].mean(), 2))


# PnL Distribution

st.subheader(" PnL Distribution by Sentiment")

fig1, ax1 = plt.subplots(figsize=(8,4))
sns.boxplot(data=filtered, x='Classification', y='Closed PnL', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)


# Trade Size Distribution

st.subheader(" Trade Size Distribution by Sentiment")

fig2, ax2 = plt.subplots(figsize=(8,4))
sns.boxplot(data=filtered, x='Classification', y='Size USD', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)


# Trade Frequency

st.subheader(" Trade Frequency by Sentiment")

freq = filtered.groupby('Classification').size()
st.bar_chart(freq)


# Summary Statistics Table

st.subheader(" Summary Statistics (PnL)")

summary = filtered.groupby('Classification')['Closed PnL'].describe()
st.dataframe(summary)

st.markdown("---")
st.markdown("Built for behavioral regime analysis of Hyperliquid traders.")
