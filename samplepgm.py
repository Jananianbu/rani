import streamlit as st

def square_number(num):
    return num ** 2

def main():
    st.title('Square Number Calculator')
    
    # Create a slider for selecting a number
    number = st.slider('Select a number', 0, 100, 1)
    
    # Calculate the square of the number
    result = square_number(number)
    
    # Display the result
    st.write(f'The square of {number} is {result}')

if __name__ == "__main__":
    main()
