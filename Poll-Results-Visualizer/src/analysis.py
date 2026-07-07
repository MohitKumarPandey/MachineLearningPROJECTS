import pandas as pd

def overall_analysis(df):
    counts = df['response'].value_counts()
    percentages = (counts / len(df)) * 100
    return counts, percentages

def region_analysis(df):
    return pd.crosstab(df['region'], df['response'])

def age_analysis(df):
    return pd.crosstab(df['age_group'], df['response'])