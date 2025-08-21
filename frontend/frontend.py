import streamlit as st
import requests

st.set_page_config(page_title="Material Submittal Comment Sheet", layout="wide")
st.title("Material Submittal Comment Sheet Generator")

st.write("Upload a material submittal PDF to receive an automated comment sheet. Only text-based and basic scanned PDFs supported.")

uploaded_file = st.file_uploader("Upload Material Submittal PDF", type=["pdf"])
if uploaded_file:
    with st.spinner("Processing your PDF and generating comment sheet..."):
        files = {'file': (uploaded_file.name, uploaded_file, 'application/pdf')}
        try:
            response = requests.post("http://localhost:8000/upload_pdf/", files=files)
            if response.status_code == 200:
                comment = response.json().get('comment_sheet', 'No comments generated.')
                st.subheader("Generated Comment Sheet")
                st.text_area("", comment, height=300)
            else:
                st.error("Failed to generate comment sheet. Please try again.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
