import pandas as pd
from tabulate import tabulate

def print_header(df, student_id):
    '''
    Print the header for a student
    input:
        df: dataframe
        student_id: str
    output:
        None
    '''
    student_data = df[df['id'] == student_id].iloc[0]
    print(f"\nStudent: {student_data['first_name']} {student_data['last_name']} (ID: {student_data['id']})\n")

def print_grades(df, student_id):
    '''
    Print the grades for a student
    input:
        df: dataframe
        student_id: str
    output:
        None
    '''
    # Get student's row
    student_data = df[df['id'] == student_id].iloc[0]
    
    # Create grades dataframe excluding id and name columns
    grades = pd.DataFrame(student_data.drop(['id', 'first_name', 'last_name'])).reset_index()
    grades.columns = ['metric', 'value']  # Rename columns
    
    # Split the metric into topic and type
    grades['topic'] = grades['metric'].str.split('_').str[0]
    grades['type'] = grades['metric'].str.split('_').str[1:]
    grades['type'] = grades['type'].str.join('_')
    
    # Pivot the data
    df_pivot = grades.pivot(
        index='topic',
        columns='type',
        values='value'
    )
    

    # Reorder and rename columns - Updated to match actual column names
    df_pivot = df_pivot[['letter_grade', 'score', 'zscore']]  # This line stays the same
    df_pivot.columns = ['Grade', 'Score', 'Z-Score']
    
    # Print using tabulate
    print(tabulate(df_pivot, headers='keys', tablefmt='simple'))
    print("\n")

def generate_report(df, student_ids):
    '''
    Print the report for a list of student ids
    input:
        df: dataframe
        student_ids: list of str
    output:
        None
    '''
    for student_id in student_ids:
        print_header(df, student_id)
        print_grades(df, student_id)

