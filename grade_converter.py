import pandas as pd
import numpy as np

def scores_to_letter_grades(df):
    '''
    Convert scores to letter grades
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    score_columns = df.columns[df.columns.str.endswith('_score')]
    for column in score_columns:
        column_name = column.replace('_score', '_letter_grade')
        bins = { -float('inf'): 'F', 50: 'D', 60: 'C', 70: 'B', 80: 'A', float('inf'): None }
        labels = list(bins.values())[:-1]
        bins = list(bins.keys())
        df[column_name] = pd.cut(df[column], bins=bins, labels=labels)
    return df

def scores_to_z_score(df):
    '''
    Convert scores to z-scores
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    score_columns = df.columns[df.columns.str.endswith('_score')]
    for column in score_columns:
        mean = df[column].mean()
        std = df[column].std()
        column_name = column.replace('_score', '_zscore')
        df[column_name] = (df[column] - mean) / std
    return df

def grades_converter(df, letter_grade = True, zscore = True, drop_scores = False):
    '''
    Convert scores to letter grades and z-scores
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    if letter_grade:
        df = scores_to_letter_grades(df)
    if zscore:
        df = scores_to_z_score(df)
    if drop_scores:
        score_columns = df.columns[df.columns.str.endswith('_score')]
        df = df.drop(columns=score_columns)
    return df