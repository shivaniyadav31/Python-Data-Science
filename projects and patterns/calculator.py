import streamlit as st

st.title("Simple Calculator")   #heading
#st.subheader("Built with Streamlit")
st.markdown("This is a simple calculator app built with Streamlit.")  #to add a description or st.write("text")

c1,c2 = st.columns(2)  #to create two columns instead of row
fnum = c1.number_input("First Number", value=0) #'value='for setting default value to 0 and + and - for incrementing and decrementing the value by default
snum = c2.number_input("Second Number", value=0)

options = ["Add", "Sbtract", "Multiply", "Divide"]  #list of options for the radio button
choice = st.radio("Select Operation", options) #radio button for selecting operation

button = st.button ("Calculate")  #button to perform calculation

result = 0
if button:  #if button is clicked
    if choice == "Add":
        result = fnum + snum
    elif choice == "Sbtract":
        result = fnum - snum
    elif choice == "Multiply":
        result = fnum * snum
    elif choice == "Divide":
        result = fnum / snum
st.success(f'Result:{result}')  #to display the result agr success ki jagah warning ho to yellow color ayega green ki jagah

st.snow() #to display balloons animation when result is displayed or st.ballons() for ballons animation

