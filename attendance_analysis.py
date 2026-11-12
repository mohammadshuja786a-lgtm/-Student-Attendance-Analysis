import pandas as pd

df = pd.read_csv("students.csv")

#print(df)

print("\nFirst 5 Students:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())

# Average Attendance
average_attendance = df["Attendance"].mean()
print("\nAverage Attendance:", average_attendance)

# Average Final Marks
average_marks = df["Final_Marks"].mean()
print("Average Final Marks:", average_marks)

# Highest Attendance
highest_attendance = df["Attendance"].max()
print("Highest Attendance:", highest_attendance)

# Lowest Attendance
lowest_attendance = df["Attendance"].min()
print("Lowest Attendance:", lowest_attendance)

# Highest Final Marks
highest_marks = df["Final_Marks"].max()
print("Highest Final Marks:", highest_marks)

# Lowest Final Marks
lowest_marks = df["Final_Marks"].min()
print("Lowest Final Marks:", lowest_marks)

# Students with Attendance below 75%
low_attendance = df[df["Attendance"] < 75]

print("\nStudents with attendance below 75%:")
print(low_attendance[["Name", "Attendance", "Final_Marks"]])

import matplotlib.pyplot as plt

# Attendance Distribution
plt.hist(df["Attendance"], bins=5)
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.title("Student Attendance Distribution")
plt.show()

# Attendance vs Final Marks
plt.scatter(df["Attendance"], df["Final_Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.show()

# Correlation between Attendance and Final Marks
correlation = df["Attendance"].corr(df["Final_Marks"])

print("\nCorrelation between Attendance and Final Marks:", correlation)

# Create Attendance Categories
def attendance_category(attendance):
    if attendance < 75:
        return "Low"
    elif attendance < 90:
        return "Average"
    else:
        return "High"

df["Attendance_Category"] = df["Attendance"].apply(attendance_category)

print("\nAttendance Categories:")
print(df[["Name", "Attendance", "Attendance_Category", "Final_Marks"]])

# Average Final Marks by Attendance Category
category_marks = df.groupby("Attendance_Category")["Final_Marks"].mean()

print("\nAverage Final Marks by Attendance Category:")
print(category_marks)

# Bar Chart
category_marks.plot(kind="bar")

plt.xlabel("Attendance Category")
plt.ylabel("Average Final Marks")
plt.title("Average Final Marks by Attendance Category")
plt.xticks(rotation=0)
plt.show()

# Final Insights

print("\n--- FINAL INSIGHTS ---")

# High attendance students
high_attendance = df[df["Attendance"] >= 90]
print("\nHigh Attendance Students:", len(high_attendance))

# Low attendance students
low_attendance = df[df["Attendance"] < 75]
print("Low Attendance Students:", len(low_attendance))

# Average marks of high attendance students
print(
    "Average marks of High Attendance Students:",
    round(high_attendance["Final_Marks"].mean(), 2)
)

# Average marks of low attendance students
print(
    "Average marks of Low Attendance Students:",
    round(low_attendance["Final_Marks"].mean(), 2)
)

# Top performer
top_student = df.loc[df["Final_Marks"].idxmax()]
print(
    "\nTop Performer:",
    top_student["Name"],
    "| Final Marks:",
    top_student["Final_Marks"]
)

# Lowest performer
lowest_student = df.loc[df["Final_Marks"].idxmin()]
print(
    "Lowest Performer:",
    lowest_student["Name"],
    "| Final Marks:",
    lowest_student["Final_Marks"]
)

# Final Conclusion

print("\n--- PROJECT CONCLUSION ---")

print("1. The average attendance of students is:",
      round(df["Attendance"].mean(), 2), "%")

print("2. The average final marks are:",
      round(df["Final_Marks"].mean(), 2))

print("3. The correlation between attendance and final marks is:",
      round(df["Attendance"].corr(df["Final_Marks"]), 4))

print("4. Students with attendance below 75%:",
      len(df[df["Attendance"] < 75]))

print("\nConclusion:")
print("The dataset shows a very strong positive relationship between")
print("attendance and final marks. Students with higher attendance")
print("generally have higher final marks in this dataset.")


# =========================================
# 1. IMPORT LIBRARIES
# =========================================

import pandas as pd
import matplotlib.pyplot as plt


# =========================================
# 2. LOAD DATASET
# =========================================

df = pd.read_csv("students.csv")


# =========================================
# 3. DATA INSPECTION
# =========================================

print("\nFirst 5 Students:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())


# =========================================
# 4. BASIC ANALYSIS
# =========================================

average_attendance = df["Attendance"].mean()
average_marks = df["Final_Marks"].mean()

print("\nAverage Attendance:", average_attendance)
print("Average Final Marks:", average_marks)

print("Highest Attendance:", df["Attendance"].max())
print("Lowest Attendance:", df["Attendance"].min())

print("Highest Final Marks:", df["Final_Marks"].max())
print("Lowest Final Marks:", df["Final_Marks"].min())


# =========================================
# 5. LOW ATTENDANCE ANALYSIS
# =========================================

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with attendance below 75%:")
print(low_attendance[["Name", "Attendance", "Final_Marks"]])


# =========================================
# 6. ATTENDANCE DISTRIBUTION
# =========================================

plt.hist(df["Attendance"], bins=5)
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.title("Student Attendance Distribution")
plt.show()


# =========================================
# 7. ATTENDANCE VS FINAL MARKS
# =========================================

plt.scatter(df["Attendance"], df["Final_Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.show()


# =========================================
# 8. CORRELATION ANALYSIS
# =========================================

correlation = df["Attendance"].corr(df["Final_Marks"])

print("\nCorrelation between Attendance and Final Marks:", correlation)


# =========================================
# 9. ATTENDANCE CATEGORIES
# =========================================

def attendance_category(attendance):
    if attendance < 75:
        return "Low"
    elif attendance < 90:
        return "Average"
    else:
        return "High"

df["Attendance_Category"] = df["Attendance"].apply(attendance_category)

print("\nAttendance Categories:")
print(df[["Name", "Attendance", "Attendance_Category", "Final_Marks"]])


# =========================================
# 10. CATEGORY-WISE AVERAGE MARKS
# =========================================

category_marks = df.groupby("Attendance_Category")["Final_Marks"].mean()

print("\nAverage Final Marks by Attendance Category:")
print(category_marks)

category_marks.plot(kind="bar")
plt.xlabel("Attendance Category")
plt.ylabel("Average Final Marks")
plt.title("Average Final Marks by Attendance Category")
plt.xticks(rotation=0)
plt.show()


# =========================================
# 11. FINAL INSIGHTS
# =========================================

high_attendance = df[df["Attendance"] >= 90]

print("\n--- FINAL INSIGHTS ---")

print("High Attendance Students:", len(high_attendance))
print("Low Attendance Students:", len(low_attendance))

print(
    "Average marks of High Attendance Students:",
    round(high_attendance["Final_Marks"].mean(), 2)
)

print(
    "Average marks of Low Attendance Students:",
    round(low_attendance["Final_Marks"].mean(), 2)
)

top_student = df.loc[df["Final_Marks"].idxmax()]
lowest_student = df.loc[df["Final_Marks"].idxmin()]

print(
    "\nTop Performer:",
    top_student["Name"],
    "| Final Marks:",
    top_student["Final_Marks"]
)

print(
    "Lowest Performer:",
    lowest_student["Name"],
    "| Final Marks:",
    lowest_student["Final_Marks"]
)


# =========================================
# 12. FINAL CONCLUSION
# =========================================

print("\n--- PROJECT CONCLUSION ---")

print(
    "The dataset shows a very strong positive relationship between "
    "attendance and final marks."
)

print(
    "Students with higher attendance generally have higher final marks "
    "in this dataset."
)