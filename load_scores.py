import pandas as pd
import kagglehub

def load_csv(file_path = "data\student-scores.csv"):
    '''
    Load a csv file
    input:
        file_path: str
    output:
        df: dataframe
    '''
    df = pd.read_csv(file_path)
    print(f"Loaded {file_path} with {df.shape[0]} rows and {df.shape[1]} columns")
    return df

def load_kaggle(kaggle_path = "mexwell/student-scores"):
    '''
    Load a kaggle dataset
    input:
        kaggle_path: str
    output:
        df: dataframe
    '''
    path = kagglehub.dataset_download(kaggle_path)
    df = pd.read_csv(path)
    print(f"Loaded {kaggle_path} with {df.shape[0]} rows and {df.shape[1]} columns")
    return df

def validate_scores(df):
    '''
    Validate scores
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    score_columns = df.columns[df.columns.str.endswith('_score')]
    for column in score_columns:
        df[column] = df[column].fillna(0)
        df[column] = df[column].clip(lower=0, upper=100)
    return df

def validate_student_ids(df):
    '''
    Validate student ids
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    df = df.dropna(subset=['id'])
    df = df.drop_duplicates(subset=['id'])
    df['id'] = df['id'].astype(str)
    max_student_id = df['id'].max()
    max_student_id_length = len(str(max_student_id))
    df['id'] = df['id'].str.zfill(max_student_id_length)
    return df

def select_columns(df):
    '''
    Select columns
    input:
        df: dataframe
    output:
        df: dataframe
    '''
    score_columns = df.columns[df.columns.str.endswith('_score')]
    columns_to_keep = ['id', 'first_name', 'last_name'] + score_columns.tolist()
    df = df[columns_to_keep]
    return df

def export_csv(df, file_path):
    '''
    Export a dataframe to a csv file
    input:
        df: dataframe
        file_path: str
    output:
        None
    '''
    df.to_csv(file_path, index=False)
    print(f"Exported {file_path} with {df.shape[0]} rows and {df.shape[1]} columns")

def preprocess(file_path=None, kaggle_path=None, output=False, output_path="data/scores_preprocessed.csv"):
    '''
    Preprocess the scores
    input:
        file_path: str
        kaggle_path: str
        output: bool
        output_path: str
    output:
        df: dataframe
    '''
    if kaggle_path:
        df = load_kaggle(kaggle_path)
    elif file_path:
        df = load_csv(file_path)
    else:
        raise ValueError("Either file_path or kaggle_path must be provided")
        
    df = validate_scores(df)
    df = validate_student_ids(df)
    df = select_columns(df)
    if output:
        export_csv(df, output_path)
    return df