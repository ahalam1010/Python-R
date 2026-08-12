import pandas as pd
import numpy as np

df = pd.read_excel("Lab_Exam_1_Raw_Data.xlsx", sheet_name="Raw_Data")

print(df.head())
print(df.shape)

# Part B

df = df.drop_duplicates(subset="Student_ID", keep="first")
print(df["Student_ID"])

df["Name"] = df["Name"].str.strip()
df["Department"] = (df["Department"].str.strip().str.title())

print(df[["Name", "Department"]])

df["Assignment"] = df["Assignment"].replace("Absent", 0)

df["Quiz"] = pd.to_numeric(df["Quiz"], errors="coerce")
df["Assignment"] = pd.to_numeric(df["Assignment"], errors="coerce")
df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")

df.loc[~df["Quiz"].between(0,20), "Quiz"] = np.nan
df.loc[~df["Assignment"].between(0,20), "Assignment"] = np.nan
df.loc[~df["Attendance"].between(0,100), "Attendance"] = np.nan

df["Quiz"] = df["Quiz"].fillna(df["Quiz"].median())
df["Assignment"] = df["Assignment"].fillna(df["Assignment"].median())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print(df[["Quiz", "Assignment", "Attendance"]])

# Part C

df["Total_Score"] = (df["Quiz"] + df["Assignment"])

df["Percentage"] = ((df["Total_Score"]/40) * 100).round(2)

df["Result"] = np.where(
    (df["Percentage"] >=50) & (df["Attendance"] >=75), "Pass", "Fail"
)

# Part D

df = df.sort_values(by="Percentage", ascending=False)
df = df.reset_index(drop=True)

# Part E

df.to_excel("Cleaned_Student_Data.xlsx", sheet_name="Cleaned_Data", index=False)