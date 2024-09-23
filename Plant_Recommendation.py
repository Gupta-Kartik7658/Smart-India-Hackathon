import streamlit as st
import pandas as pd
import csv
st.set_page_config(page_title = "Plant Recommendation System",layout="wide") 
st.sidebar.title("Select Functionality")

# Title of the app

st.title("Plant Recommendation System")

# CSS for Dark Theme and custom styling
st.markdown(f"""
    <style>
    /* Set background colors */
    
    /* Form style with secondary background color */
    .form-style {{
        padding: 20px;
        background-color: #0e1117;
        width: 50%; /* Set the width to 50% */
    }}
    
    /* Margin between form elements */
    .space-all {{
        margin: 50px;
    }}
    
    .space-button {{
        margin: 30px;
        margin-bottom: 110px;
    }}
    
    .space-all-first {{
        margin-bottom: 0px;
    }}
    
    .space-title{{
        margin-top: 10px;
        margin-bottom: 5px;
        padding: 1px 1px;
    }}


    /* Button styling */
    .stButton button {{
        background-color: #ff4b4b;
        color: #fafafa;
        border-radius: 10px;
        font-size: 16px;
        padding: 8px 20px;
    }}
    
    /* Input box and dropdown styling */
    .stTextInput, .stSelectbox {{
        background-color: #0e1117;
        color: #fafafa;
        border-color: #ff4b4b;
        font-size: 16px;
    }}
    
    /* Text color for results */
    .stImage {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column; 
    }}
    </style>
""", unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns([3, 2], gap="large")  # Adjusting width of columns (col1 narrower, col2 wider)

# Load and process the CSV
with open(r"C:\\Users\\hp\\Desktop\\SIH\\Districts.csv", newline='') as f:
    reader = csv.reader(f)
    t = [str(row).replace("[", "").replace("]", " ").replace("'", "").replace('"', "").replace("ï»¿", "") for row in reader]
    t.sort()
    t.insert(0,'')

# Form inside column 1
with col1:
    # Form styling
    form1 = st.form(key="Form1")
    form1.markdown('<div class="form-style">', unsafe_allow_html=True)
    
    form1.markdown('<div class="space-title">', unsafe_allow_html=True) 
    form1.title("Set Preferences")
    
    # Add space and selectbox for location
    form1.markdown('<div class="space-all-first"></div>', unsafe_allow_html=True)
    city = form1.selectbox("Location", t, key="city", help="Select the location")
    
    # Add space and selectbox for crop type
    form1.markdown('<div class="space-all"></div>', unsafe_allow_html=True)
    crop_type = form1.selectbox("Crop Type", ['',"Commercial Use", "Non-Commercial Use"], key="crop_type", help="Select the crop type")
    
    # Add space and submit button
    
    form1.markdown('<div class="space-button"></div>', unsafe_allow_html=True)
    submit = form1.form_submit_button("Find Recommendations")
    
    
    form1.markdown('</div>', unsafe_allow_html=True)

# Apply padding and margin for col2
with col2:
    st.markdown('<div class="col2-style">', unsafe_allow_html=True)
    # Output inside column 2 if the form is submitted
    if submit:
        # Check if crop type is Non-Commercial Use to recommend plants
        if crop_type == "Non-Commercial Use":
            st.write("Recommended Plants:")
            
            # Create a grid layout for images (2 images per row)
            row1_col1, row1_col2 = st.columns(2,gap="medium")  # First row with two columns
            row2_col1, row2_col2 = st.columns(2,gap="medium")  # Second row with two columns
            
            # First row of images
            with row1_col1:
                with st.popover("Neem"):
                    st.title("Neem")
                    st.markdown("**Scientific Name**: *Azadirachta indica*")
                    st.markdown("**Common Name:** Indian lilac")
                    st.markdown("""
                        **Medicinal Properties:**
                        - Antiseptic and antinflamatory properties
                        - Cancer Management
                        - Reduces joint pain
                        - Insect and Mosquito repellent
                        - Neem oil is spermicidal and may be a nontoxic contraceptive.
                    """)
                st.image('Neem.jpg', width=130)
            
            with row1_col2:
                with st.popover("Tulsi"):
                    st.title("Tulsi")
                    st.markdown("**Scientific Name**: *Ocimum tenuiflorum*")
                    st.markdown("**Common Name:** Holy Basil")
                    st.markdown("""
                        **Medicinal Properties:**
                        - Antibacterial and antifungal properties
                        - Supports immunity
                        - Reduces stress and inflammation
                        - Aids digestion
                        - Acts as a natural remedy for colds and respiratory issues
                    """)
                st.image('Tulsi.jpeg', width=130)
            
            # Second row of images
            with row2_col1:
                with st.popover("Moringa"):
                    st.title("Moringa")
                    st.markdown("**Scientific Name**: *Moringa oleifera*")
                    st.markdown("**Common Name:** Drumstick Tree, Miracle Tree")
                    st.markdown("""
                        **Medicinal Properties:**
                        - Rich in antioxidants
                        - Reduces inflammation
                        - Supports brain health
                        - Helps in regulating blood sugar levels
                        - Aids in lowering cholesterol
                        - Provides essential vitamins and minerals (Vitamin C, Calcium, Potassium)
                    """)
                st.image('Moringa.jpg',  width=130)
            
            with row2_col2:
                with st.popover("Aloe Vera"):
                    st.title("Aloe Vera")
                    st.markdown("**Scientific Name**: *Aloe barbadensis miller*")
                    st.markdown("**Common Name:** Aloe Vera")
                    st.markdown("""
                        **Medicinal Properties:**
                        - Soothes skin irritations and burns
                        - Promotes wound healing
                        - Supports digestive health
                        - Hydrates and moisturizes skin
                        - Contains antioxidants and vitamins (A, C, E)
                        - Helps in reducing inflammation
                    """)
                st.image('Aloe vera.jpeg', width=110)
    
    st.markdown('</div>', unsafe_allow_html=True)
