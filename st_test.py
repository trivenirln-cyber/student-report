import streamlit as st
st.title("student report App")
name = st.text_input("Student name")
subject = st.text_input("Enter subject name")
marks = st.number_input("Enter your marks")
if st.button("save") :
    with open ("students.txt","a") as file:
        file.write(f"Name:{name},subject :{subject},Marks:{marks}\n")
        st.success("Data saved successfully!")
if st.button ("View students Details"):
    with open("students.txt","r") as file:
        st.text(file.read())
else:
    st.warning("Try again")



    

                        