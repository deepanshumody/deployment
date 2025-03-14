import streamlit as st

def main():
    st.set_page_config(page_title="App Moved", page_icon="🚀")
    
    st.title("🚨 App Moved 🚨")
    st.write("This application has been moved to a new location.")
    
    new_url = "https://rmpanalysis.streamlit.app/"  # Replace with the actual new link
    st.markdown(f"### [Click here to access the new app]({new_url})")
    
    
    st.balloons()
    
if __name__ == "__main__":
    main()
