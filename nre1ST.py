import streamlit as st
import json
def jsontotxt(data):
    jsonstr = json.dumps(data, indent=4)
    return jsonstr
def main():
    st.title("JSON to Text File Converter and PDF Downloader")
    inputfile = st.file_uploader("Upload a JSON file", type="json")
    if inputfile is not None:
        data = json.load(inputfile)
        txtdata = jsontotxt(data)
        st.subheader("Converted JSON Data:")
        st.text(txtdata)
        st.subheader("Download the Converted Text File:")
        st.download_button(
            label="Download Text File",
            data=txtdata,
            file_name="output.txt",
            mime="text/plain"
        )
if __name__ == "__main__":
    main()
