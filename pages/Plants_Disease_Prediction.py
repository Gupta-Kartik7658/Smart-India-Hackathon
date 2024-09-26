import streamlit as st
import csv
import time
st.set_page_config(page_title = "Plant Disease Recommendation System",layout="wide") 
st.markdown("<h1 style='text-align: center; color: #fafafa;'>Plant Disease Prediction System</h1>", unsafe_allow_html=True)

form1 = st.form(key="Hello")
with form1:
    file = st.file_uploader("Upload The image of your Crop/Plant",type=["png","jpg","jpeg","tiff"])
    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
    upload_button = col4.form_submit_button("Submit")
    

if(upload_button and file):
    mybar = st.progress(0,"Analysing the Image")  
    for i in range(101):
        time.sleep(0.01)
        mybar.progress(i)
    time.sleep(1)
    mybar.empty()
    
    st.success("Image Uploaded Succesfully ",icon="✅")
    st.header("Diseases With Most Matches")
    
    with st.expander("Cercospora ocimicola"):
        st.markdown("**Symptoms**")
        st.write("Circular to irregular dark spots on leaves with light centers")
        
        st.markdown("**Cause**")
        st.write("Fungus")
        
        st.write("**Management**")
        st.write("Avoid overhead irrigation and splashing plants with water, instead water plants from the base and apply a layer of mulch around the plants to reduce water splash; remove and destroy any symptomatic leaves; minor infections can be controlled by spraying weekly with a fungicide containing potassium bicarbonate")
    

    with st.expander("Peronospora belbahrii"):
        st.markdown("**Symptoms**")
        st.write("Yellowing leaves; discoloration often begins around middle vein and spreads outwards; gray fuzzy or downy growth on lower surface of the leaves; brown to black angular necrotic patches on the plant.")
        
        st.markdown("**Cause**")
        st.write("Fungus")
        
        st.write("**Management**")
        st.write("Grow tolerant varieties; apply protective fungicide; ensure good air circulation around greenhouse grown plants; use drip irrigation to avoid wetting foliage.")
    
    
    with st.expander("Pseudomonas cichorii"):
        st.markdown("**Symptoms**")
        st.write("Angular or irregular brown or black water-soaked spots on leaves; streaks on stems.")
        
        st.markdown("**Cause**")
        st.write("Bacteria")
        
        st.write("**Management**")
        st.write("No treatment when present; use disease free seed and/or transplants; use wide field spacing to promote air circulation around plants; remove diseased leaves from plant and soil surface immediately.")
    
if(upload_button and not file):
    st.success("Upload an Valid Image ",icon="❎")
