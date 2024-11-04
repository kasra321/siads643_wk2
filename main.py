import argparse
from load_scores import preprocess
from grade_converter import grades_converter
from generate_report import generate_report

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--file_path", type=str, default="data\student-scores.csv")
    args.add_argument("--student_ids", type=str, nargs='+', default=["001"])
    args = args.parse_args()

    df = preprocess(file_path=args.file_path)
    df = grades_converter(df)
    generate_report(df, args.student_ids)

