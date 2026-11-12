import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Page title
st.title("Student Attendance Analysis Dashboard")

st.write("Analysis of student attendance and academic performance")

# Student Filter
selected_student = st.selectbox(
    "Select a Student",
    ["All Students"] + df["Name"].tolist()
)

if selected_student != "All Students":
    student_data = df[df["Name"] == selected_student]

    st.subheader(f"Details of {selected_student}")

    st.write(student_data)

# Key statistics
average_attendance = df["Attendance"].mean()
average_marks = df["Final_Marks"].mean()
correlation = df["Attendance"].corr(df["Final_Marks"])
low_attendance_count = len(df[df["Attendance"] < 75])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Attendance", f"{average_attendance:.2f}%")
col2.metric("Average Final Marks", f"{average_marks:.2f}")
col3.metric("Correlation", f"{correlation:.4f}")
col4.metric("Low Attendance Students", low_attendance_count)

# Attendance distribution
st.subheader("Attendance Distribution")

fig1, ax1 = plt.subplots()
ax1.hist(df["Attendance"], bins=5)
ax1.set_xlabel("Attendance (%)")
ax1.set_ylabel("Number of Students")
ax1.set_title("Student Attendance Distribution")
st.pyplot(fig1)

# Attendance vs Final Marks
st.subheader("Attendance vs Final Marks")

fig2, ax2 = plt.subplots()
ax2.scatter(df["Attendance"], df["Final_Marks"])
ax2.set_xlabel("Attendance (%)")
ax2.set_ylabel("Final Marks")
ax2.set_title("Attendance vs Final Marks")
st.pyplot(fig2)

# Category analysis
def attendance_category(attendance):
    if attendance < 75:
        return "Low"
    elif attendance < 90:
        return "Average"
    else:
        return "High"

df["Attendance_Category"] = df["Attendance"].apply(attendance_category)

category_marks = df.groupby("Attendance_Category")["Final_Marks"].mean()

st.subheader("Average Final Marks by Attendance Category")

fig3, ax3 = plt.subplots()
category_marks.plot(kind="bar", ax=ax3)
ax3.set_xlabel("Attendance Category")
ax3.set_ylabel("Average Final Marks")
ax3.set_title("Average Final Marks by Attendance Category")
ax3.tick_params(axis="x", rotation=0)
st.pyplot(fig3)

# Pass / Fail Analysis

df["Result"] = df["Final_Marks"].apply(
    lambda marks: "Pass" if marks >= 50 else "Fail"
)

st.subheader("Student Result Analysis")

result_counts = df["Result"].value_counts()

st.write("Number of students in each result category:")
st.write(result_counts)

fig4, ax4 = plt.subplots()
result_counts.plot(kind="bar", ax=ax4)

ax4.set_xlabel("Result")
ax4.set_ylabel("Number of Students")
ax4.set_title("Pass vs Fail Students")
ax4.tick_params(axis="x", rotation=0)

st.pyplot(fig4)

# Final Conclusion

st.subheader("Final Conclusion")

st.write(
    "The analysis shows a very strong positive relationship between "
    "student attendance and final marks in this dataset."
)

st.write(
    f"The average attendance is {average_attendance:.2f}% and "
    f"the average final marks are {average_marks:.2f}."
)

st.write(
    f"The correlation coefficient is {correlation:.4f}, "
    "indicating a very strong positive relationship in this dataset."
)

st.info(
    "Note: Correlation shows an association between attendance and marks; "
    "it does not by itself prove that attendance causes higher marks."
)