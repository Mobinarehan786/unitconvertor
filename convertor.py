# project#1 uni convertor
# Build a Google Unit Convertor using python and streamlit

# import streamlit as st

# st.markdown(
#     """
#     <style>
#     body{
#         background-color:rgb(18, 18, 19);
#         color:white;
#     }
#     .stApp{
#         background:linear-gradient(to right,rgb(114, 114, 117),rgb(88, 88, 92));
#         padding:30px;
#         border-radius:10px;
#         box-shadow:0 0 10px 0 rgba(255, 255, 255, 0.1);
#     }
#     h1{
#         text-align:center;
#         font-size:18px;
#         color:white;
#     .stButton>button{
#     background:linear -gradient:rgb(255, 255, 255);
#     paddingL:10px 20px,
#     border-radius:10px,
#     transition:0.3s,
#     box -shadow:0px 05px 15px rgba(255, 255, 255, 0.1);
#     }
#     .stButton>button:hover{
#     transform:scale(1.05);}
#     background:linear-gradient(45deg,rgb(255, 255, 255),rgb(255, 255, 255)
#     color:black;
#     }
#     .result-box{
#     font-size:24px;
#     font-weight:bold;
#     text-align:center;
#     background:rgba(255, 255, 255, 0.1);
#     padding:20px;
#     border-radius:10px;
#     margin-top:20px;
#     box-shadow:0 0 10px 0 rgba(255, 255, 255, 0.1);
#     }
#     .footer{
#     text-align:center;
#     font-size:14px;
#     color:black;
#     margin-top:50px;
#     }


#   </style>
   
 
#     """,
#     unsafe_allow_html=True, 
# )


# # title  and description
# st.markdown ("<h1 >Unit Convertor using Python and Stremlit</h1>" ,"unsafe_allow_html=True")
# st.Write ("Easily convert between different units of length , weight and Temperature.")


# # side bar menu
# conversion_type=st.sidebar.selectbox("Schoose the conversion type",["Length","Weight","Temperature"])
# value =st.number_input("Enter the value to convert",value=0.0,step=0.1,min_value=0.0)
# col1,col2=st.columns(2)
# if conversion_type=="Length":
#     with col1:
#         from_unit=st.selectbox("From Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer"])
#     with col2:
#         to_unit=st.selectbox("To Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer"])
#     if conversion_type=="Weight":
#         with col1:
#             from_unit=st.selectbox("From Unit",["Kilogram","Gram","Milligram","Microgram","Nanogram"])
#         with col2:
#             to_unit=st.selectbox("To Unit",["Kilogram","Gram","Milligram","Microgram","Nanogram"])
#     if conversion_type=="Temperature":
#         with col1:
#             from_unit=st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
# if conversion_type=="Temperature":
#     with col1:
#         from_unit=st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
#     with col2:
#         to_unit=st.selectbox("To Unit",["Celsius","Fahrenheit","Kelvin"])



# #conversion function
# def convert_length(value,from_unit,to_unit):
#     length_units={
#         "Meter":1.0,
#         "Kilometer":1000.0,
#         "Centimeter":0.01,
#         "Millimeter":0.001,
#         "Micrometer":0.000001,
#         "Nanometer":0.000000001,
#     }
#     return( value/length_units[from_unit]/length_units[to_unit])
# def convert_weight(value,from_unit,to_unit):
#     weight_units={
#         "Kilogram":1.0,
#         "Gram":0.001,
#         "Milligram":0.000001,
#         "Microgram":0.000000001,
#         "Nanogram":0.000000000001,
#     }
#     return(value/weight_units[from_unit]/weight_units[to_unit])
# def convert_temperature(value,from_unit,to_unit):
#     if from_unit=="Celsius" :
#         return(value*9/5+32) if to_unit=="Fahrenheit" else value+273.15 if to_unit=="Kelvin" else value
#     elif from_unit=="Fahrenheit" :
#         return((value-32)*5/9) if to_unit=="Celsius" else (value+459.67)*5/9 if to_unit=="Kelvin" else value
#     elif from_unit=="Kelvin":
#         return(value-273.15) if to_unit=="Celsius" else (value-459.67)*5/9 if to_unit=="Fahrenheit" else value
#     return value
#     #button for conversion
#     if st.button("🤖Convert"):
#         if conversion_type=="Length":
#             result=length_convertor(value, from_unit, to_unit)
#         elif conversion_type=="Weight":
#             result=weight_convertor(value, from_unit, to_unit)
#         elif conversion_type=="Temperature":
#             result=temp_convertor(value,from_unit,to_unit)
#         st.markdown(f"<div class='result-box'>{value} {from_unit}= {result:.4f} {to_unit}</div>",unsafe_allow_html=True)
#         st.markdown("<div class='footer'>Developed by Mobina Khatoon<a href='https://github.com/yourusername'>@yourusername</a></div>",unsafe_allow_html=True)

   

import streamlit as st

# Apply custom CSS for better styling
st.markdown(
    """
    <style>
    body {
        background-color: rgb(18, 18, 19);
        color: white;
    }
    .stApp {
        background: linear-gradient(to right, rgb(114, 114, 117), rgb(88, 88, 92));
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 0 10px 0 rgba(255, 255, 255, 0.1);
    }
    h1 {
        text-align: center;
        font-size: 24px;
        color: white;
    }
    .stButton > button {
        background: linear-gradient(45deg, white, lightgray);
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.1);
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 0 10px 0 rgba(255, 255, 255, 0.1);
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: white;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>Universal Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of Length, Weight, and Temperature.")

# Sidebar menu for selecting conversion type
conversion_type = st.sidebar.selectbox("Choose the conversion type", ["Length", "Weight", "Temperature"])

# User input for value to be converted
value = st.number_input("Enter the value to convert", value=0.0, step=0.1, min_value=0.0)

# Column layout for unit selection
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Nanogram"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Nanogram"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])


# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
    }
    return (value * length_units[from_unit]) / length_units[to_unit]


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Microgram": 1e-9,
        "Nanogram": 1e-12,
    }
    return (value * weight_units[from_unit]) / weight_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5 / 9) if to_unit == "Celsius" else ((value + 459.67) * 5 / 9) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else (value * 9 / 5 - 459.67) if to_unit == "Fahrenheit" else value
    return value


# Button for conversion
if st.button("🤖 Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    # Display the result
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by Mobina Khatoon</div>", unsafe_allow_html=True)
