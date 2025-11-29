import streamlit as st

st.title("Simple Calculator")

# Inputs
a = st.number_input("Enter first number", value=0.0)
b = st.number_input("Enter second number", value=0.0)

# Operation
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])

# Button
if st.button("Calculate"):
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            st.error("Cannot divide by zero")
        else:
            result = a / b

    # Show result
    if operation != "/" or b != 0:
        st.success(f"Result: {result}")
