wimport streamlit as st

st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight:", min_value=1.0)
weight_unit = st.selectbox("Select weight unit:", ["kgs", "lbs"])
height = st.number_input("Enter your height:", min_value=1.0)
height_unit = st.selectbox("Select height unit:", ["cms", "inches"])

# Convert weight to kg
if weight_unit.lower() == "lbs":
    weight = weight * 0.453592

# Convert height to meters
if height_unit.lower() == "cms":
    height = height * 0.01
elif height_unit.lower() == "inches":
    height = height * 0.0254

# Calculate BMI
if weight > 0 and height > 0:
    BMI = weight / (height ** 2)
    st.write(f"Your BMI is: **{BMI:.2f}**")

    # BMI Categories
    if BMI < 18.5:
        st.info("You are underweight, need to gain some weight.")
    elif 18.5 <= BMI < 25:
        st.success("You are normal, don’t listen to others.")
    elif 25 <= BMI < 30:
        st.warning("You are overweight, not obese but still need to lose some weight.")
    elif 30 <= BMI < 40:
        st.error("You are obese and need to lose some weight.")
    else:
        st.error("You are severely obese, it is serious and possibly harmful.")
        
    if BMI < 18.5: 
     x = 18.5 * (b**2)
     v = x - a
     print('you need to gain ' + str(v) + ' kgs')
    elif BMI > 25:
     x = 25 * (b**2)
     v = a - x
     print('you need to lose ' + str(v) + ' kgs'),
    

st.write("Results are for adults only and do not apply to teenagers or kids. THANK YOU!")



