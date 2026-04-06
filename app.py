import streamlit as st
import pandas as pd

# Sample data structure to store employee records
employee_data = {}

# Function to add employee
def add_employee(emp_id, name, position):
    employee_data[emp_id] = {'Name': name, 'Position': position}

# Function to update employee
def update_employee(emp_id, name, position):
    if emp_id in employee_data:
        employee_data[emp_id] = {'Name': name, 'Position': position}

# Function to delete employee
def delete_employee(emp_id):
    if emp_id in employee_data:
        del employee_data[emp_id]

# Function to display employees
def display_employees():
    if employee_data:
        st.write(pd.DataFrame.from_dict(employee_data, orient='index'))
    else:
        st.write("No employee records found.")

# Streamlit app layout
st.title('Employee Management System')
st.sidebar.header('Manage Employees')

option = st.sidebar.selectbox('Select Action', ['Add Employee', 'Update Employee', 'Delete Employee', 'Display Employees'])

if option == 'Add Employee':
    emp_id = st.text_input('Employee ID')
    name = st.text_input('Name')
    position = st.text_input('Position')
    if st.button('Add'):
        add_employee(emp_id, name, position)
        st.success(f"Added employee: {name}")

elif option == 'Update Employee':
    emp_id = st.text_input('Employee ID')
    name = st.text_input('Name')
    position = st.text_input('Position')
    if st.button('Update'):
        update_employee(emp_id, name, position)
        st.success(f"Updated employee: {name}")

elif option == 'Delete Employee':
    emp_id = st.text_input('Employee ID')
    if st.button('Delete'):
        delete_employee(emp_id)
        st.success(f"Deleted employee with ID: {emp_id}")

elif option == 'Display Employees':
    display_employees()