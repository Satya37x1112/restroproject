import streamlit as st

st.title("welcome to my website")
name=st.text_input("enter your name")
address=st.text_area("enter your address")
course=st.text_input("enter your course")
year=st.selectbox("select your year :",(1,2,3,4,5))
button=st.button("done")

menu={
    "Pizza":70,
    "Burger":50,
    "Pasta":40,
    "Macaroni":60,
    "Tea":5,
    "Coffee":15,
    "Fluids":60

}

st.write("Welcome To BTech restro+cafe\n The menu is\n Pizza 70\n Burger 50\n Pasta 40\n Macaroni 60\n Tea 5\n Coffee 15\n Fluids 60\n ")
total_amount=0
while True:
    order=st.text_input("Enter your order please ")
    quantity=st.number_input("enter quantity please ")
    if order in menu:
        total_amount=total_amount+(menu[order]*quantity)
    ch=input("Anything else you want to add Y for Yes and N for no ")
    if ch in "Nn":
        break
st.write("Your bill is",total_amount)

