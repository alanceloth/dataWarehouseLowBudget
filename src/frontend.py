import streamlit as st 

class CSVValidatorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="CSV Validator",
            page_icon=":bar_chart:",
            layout="wide",
            initial_sidebar_state="expanded",
        )
    
    def display_header(self):
        st.title("Insert your CSV file here")

    def upload_file(self):
        uploaded_file = st.file_uploader("Choose an CSV file", type="csv")
        return uploaded_file
    
    def display_results(self, result, error):
        if error:
            st.error(f"Validation Error: {error}", icon="🚨")
        else:
            st.success("Schema correct!", icon="✅")
    
    def display_save_button(self):
        st.button("Save", key="save_button")

    def display_wrong_message(self):
        return st.error("Please upload a CSV file with the correct schema", icon="🚨")
    
    def display_success_message(self):
        return st.success("Data saved in the database", icon="✅")



