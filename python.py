import streamlit as st

def Gen_Eff(V, CL, IL, K, Rse, Ra):
    # Calculate Core Losses (CUL) and Efficiency
    CUL = (K * IL)**2 * (Rse + Ra)
    output_power = K * V * IL
    input_power = output_power + CL + CUL
    eff = (output_power / input_power) * 100
    return eff, CUL

# Streamlit UI setup
st.title("2305a21l03-PS10")

# Create two columns for input and output
col1, col2 = st.columns(2)

# Input section for user
with col1:
    V = st.number_input("Enter the Voltage (V) in Volts", value=1)
    CL = st.number_input("Enter Core Losses (CL) in Watts", value=1)
    IL = st.number_input("Enter Full Load Current (IL) in Amps", value=1)
    K = st.number_input("Enter Loading on Generator (K)", value=1)
    Rse = st.number_input("Enter Series Field Resistance (Rse) in Ohms", value=1)
    Ra = st.number_input("Enter Armature Resistance (Ra) in Ohms", value=1)

    # Calculate button
    if st.button("Calculate"):
        # Calling function to get efficiency and core losses
        eff, CUL = Gen_Eff(V, CL, IL, K, Rse, Ra)

        # Results displayed after calculation
        with col2:
            st.subheader("Results:")
            st.write(f"Efficiency: {eff:.2f}%")
            st.write(f"Core Losses (CUL): {CUL:.2f} Watts")
