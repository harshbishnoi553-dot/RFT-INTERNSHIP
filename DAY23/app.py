import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Employee Performance Dashboard", layout="wide")

st.title("Employee Performance Analytics Dashboard")

df = pd.read_csv("employee_performance.csv")

df = df.drop_duplicates().dropna()

departments = ["All"] + sorted(df["Department"].unique().tolist())
selected_department = st.sidebar.selectbox("Select Department", departments)

if selected_department != "All":
    data = df[df["Department"] == selected_department]
else:
    data = df

min_attendance = st.sidebar.slider(
    "Minimum Attendance (%)", 0, 100, 0
)

data = data[data["Attendance"] >= min_attendance]

col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(data))
col2.metric("Average Performance", round(data["Performance"].mean(), 2))
col3.metric("Average Attendance", round(data["Attendance"].mean(), 2))

st.subheader("Employee Data")
st.dataframe(data)

st.subheader("Top 10 Performers")
st.dataframe(
    data.nlargest(10, "Performance")
    [["Employee_Name", "Department", "Performance", "Attendance"]]
)

st.subheader("Performance Comparison")

dept_avg = data.groupby("Department")["Performance"].mean()

fig, ax = plt.subplots()
dept_avg.plot(kind="bar", ax=ax)
ax.set_xlabel("Department")
ax.set_ylabel("Average Performance")
st.pyplot(fig)

st.subheader("Attendance Trend")

fig, ax = plt.subplots()
ax.plot(data["Employee_Name"], data["Attendance"], marker="o")
ax.set_xlabel("Employee")
ax.set_ylabel("Attendance (%)")
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("Department Distribution")

fig, ax = plt.subplots()
data["Department"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)
ax.set_ylabel("")
st.pyplot(fig)

st.subheader("Employees Below 75% Attendance")

low_attendance = data[data["Attendance"] < 75]

st.dataframe(
    low_attendance[
        ["Employee_Name", "Department", "Performance", "Attendance"] 
    ]
)