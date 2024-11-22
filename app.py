import streamlit as st

# Import the DELTA_STAR function
def DELTA_STAR(R12, R23, R31):
    # Calculate the resistances of the STAR network
    denominator = R12 + R23 + R31
    R1 = (R12 * R31) / denominator
    R2 = (R12 * R23) / denominator
    R3 = (R31 * R23) / denominator
    return R1, R2, R3

# Streamlit web application
def main():
    st.title("2205A21005 - ps05")

    st.markdown("""
    This web application calculates the resistances (R1, R2, R3) of a STAR connection network 
    based on the given DELTA connection resistances (R12, R23, R31).
    """)

    # Get inputs from user
    R12 = st.number_input("Enter the resistance R12 (in ohms):", value=100)
    R23 = st.number_input("Enter the resistance R23 (in ohms):",value=100)
    R31 = st.number_input("Enter the resistance R31 (in ohms):", value=100)

    if st.button("Calculate"):
        if R12 > 0 and R23 > 0 and R31 > 0:
            # Calculate R1, R2, and R3 using DELTA_STAR function
            R1, R2, R3 = DELTA_STAR(R12, R23, R31)
            st.write(f"The resistance R1 is: {R1:.2f} ohms")
            st.write(f"The resistance R2 is: {R2:.2f} ohms")
            st.write(f"The resistance R3 is: {R3:.2f} ohms")
        else:
            st.error("Please enter valid values for R12, R23, and R31.")

if __name__ == "__main__":
    main()
