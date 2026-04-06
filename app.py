import streamlit as st
import pandas as pd

from main import WorkforceApp
from core.employee import Employee

app = WorkforceApp()

st.set_page_config(layout="wide")
st.title("Smart Workforce Analytics System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Manage Employees", "Analytics"]
)

# ================= DASHBOARD =================
if menu == "Dashboard":

    st.header("Workforce Overview")

    data = app.get_all()

    if len(data) == 0:
        st.warning("No employees yet")
    else:
        df = pd.DataFrame(data,
            columns=["ID","Name","Age","Dept","Salary","Performance"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Employees", len(df))
        col2.metric("Avg Salary", round(df["Salary"].mean(),2))
        col3.metric("Avg Performance", round(df["Performance"].mean(),2))

        st.dataframe(df, use_container_width=True)


# ================= CRUD =================
elif menu == "Manage Employees":

    st.header("Employee Management")

    tab1, tab2, tab3 = st.tabs(["Add","Update","Delete"])

    # ---------- ADD ----------
    with tab1:

        col1, col2 = st.columns(2)

        with col1:
            emp_id = st.number_input("Employee ID")
            name = st.text_input("Name")
            age = st.number_input("Age")

        with col2:
            dept = st.selectbox("Department",
                    ["IT","HR","Finance","Sales","Marketing"])
            sal = st.number_input("Salary")
            perf = st.slider("Performance",1.0,5.0)

        if st.button("Add Employee"):
            emp = Employee(emp_id,name,age,dept,sal,perf)
            app.add_employee(emp)
            st.success("Employee Added")

    # ---------- UPDATE ----------
    with tab2:

        st.subheader("Update Salary")

        up_id = st.number_input("Employee ID to Update")
        new_sal = st.number_input("New Salary")

        if st.button("Update"):
            app.update_salary(up_id,new_sal)
            st.success("Updated Successfully")

    # ---------- DELETE ----------
    with tab3:

        st.subheader("Delete Employee")

        del_id = st.number_input("Employee ID to Delete")

        if st.button("Delete"):
            app.delete_employee(del_id)
            st.success("Deleted Successfully")

    st.divider()

    st.subheader("Employee Records")

    data = app.get_all()

    if len(data) > 0:
        df = pd.DataFrame(data,
            columns=["ID","Name","Age","Dept","Salary","Performance"])
        st.dataframe(df, use_container_width=True)


# ================= ANALYTICS =================
else:

    st.header("Analytics Dashboard")

    data = app.get_all()

    if len(data) == 0:
        st.warning("No data available")
    else:

        df, stats = app.get_analytics()

        col1,col2,col3,col4 = st.columns(4)

        col1.metric("Mean Salary", round(stats["Mean"],2))
        col2.metric("Median", round(stats["Median"],2))
        col3.metric("Std Dev", round(stats["Std Dev"],2))
        col4.metric("Correlation", round(stats["Correlation"],2))

        charts = app.generate_reports()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Department Salary")
            st.pyplot(charts["bar"])

            st.subheader("Salary Distribution")
            st.pyplot(charts["hist"])

        with col2:
            st.subheader("Performance vs Salary")
            st.pyplot(charts["scatter"])

            st.subheader("Department Distribution")
            st.pyplot(charts["pie"])