# Student Grade Processing System

A simple Python system for processing and validating student scores from various data sources.

Created by: Kasra Afzali  
Course: SIADS 643 - University of Michigan  
Term: Fall 2024

## Features

- Load data from CSV files or Kaggle datasets
- Validate student scores (ensures values between 0-100)
- Clean student IDs (removes duplicates, standardizes format)
- Export preprocessed data to CSV (optional)

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage in your Python code:
```python
from load_scores import preprocess

# Load from local CSV
df = preprocess(file_path="data/scores.csv")

# Load from Kaggle
df = preprocess(kaggle_path="mexwell/student-scores")

# Load and save preprocessed data
df = preprocess(file_path="data/scores.csv", 
                output=True, 
                output_path="data/processed.csv")
```

## Input Data Format

The system expects a CSV file with:
- `student_id`: Unique identifier
- Any columns ending with `_score` (e.g., `math_score`, `science_score`)

## Data Processing Steps

1. Data Loading
   - Reads CSV files or Kaggle datasets
   - Validates file existence and format

2. Score Validation
   - Replaces missing scores with 0
   - Ensures scores are between 0-100

3. Student ID Cleaning
   - Removes rows with missing IDs
   - Eliminates duplicate IDs
   - Standardizes ID format

## File Structure

- `load_scores.py`: Main processing functions
- `requirements.txt`: Required Python packages
- `README.md`: This documentation

## Dependencies

- pandas
- kagglehub

## Contributing

Feel free to submit issues and pull requests.

---
Note: This repository is created for academic purposes as part of SIADS 643 coursework at the University of Michigan.