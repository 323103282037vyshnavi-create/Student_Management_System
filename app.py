
import streamlit as st
import csv
import os
import pandas as pd

FILENAME = "students.csv"

# Create CSV file if not exists
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["VID", "Name", "Citizen", "Course", "Status"])

# Functions
def add_student(vid, name, citizen, course, status):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([vid, name, citizen, course, status])

def read_students():
    return pd.read_csv(FILENAME)

def update_student(vid, name, citizen, course, status):
    df = pd.read_csv(FILENAME)
    df.loc[df['VID'] == vid] = [vid, name, citizen, course, status]
    df.to_csv(FILENAME, index=False)

def delete_student(vid):
    df = pd.read_csv(FILENAME)
    df = df[df['VID'] != vid]
    df.to_csv(FILENAME, index=False)

# ----------------- Streamlit UI ----------------- #
st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add New Student")
    vid = st.number_input("VID", step=1)
    name = st.text_input("Name")
    citizen = st.text_input("Citizen")
    course = st.text_input("Course")
    status = st.text_input("Status")

    if st.button("Add"):
        add_student(vid, name, citizen, course, status)
        st.success("Student added successfully")

elif choice == "View Students":
    st.subheader("All Students")
    st.dataframe(read_students())

elif choice == "Update Student":
    st.subheader("Update Student")
    vid = st.number_input("VID to Update", step=1)
    name = st.text_input("New Name")
    citizen = st.text_input("New Citizen")
    course = st.text_input("New Course")
    status = st.text_input("New Status")

    if st.button("Update"):
        update_student(vid, name, citizen, course, status)
        st.success("Student updated successfully")

elif choice == "Delete Student":
    st.subheader("Delete Student")
    vid = st.number_input("VID to Delete", step=1)

    if st.button("Delete"):
        delete_student(vid)
        st.success("Student deleted successfully")
