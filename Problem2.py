import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    exam=examinations
    exam['attended_exams'] = exam.groupby(['student_id','subject_name'])['subject_name'].transform('count')
    exam=exam.drop_duplicates()

    df=students.merge(subjects, how='cross')
    df=df.merge(exam, on=['student_id','subject_name'], how='left')
    df['attended_exams'] = df['attended_exams']. fillna (0)
    df = df.sort_values(by=['student_id', 'subject_name'])
    return(df[['student_id', 'student_name', 'subject_name', 'attended_exams']])