import streamlit as st
import requests

st.set_page_config(page_title="Dataset Lie Detector", layout="wide")

st.title("📊 Dataset Lie Detector")
st.markdown("Detect bias, missing values, and hidden risks in your dataset")

data = st.text_area("Paste your CSV data here:")

if st.button("Analyze Dataset"):
    with st.spinner("Analyzing dataset..."):
        response = requests.post(
            "http://localhost:5000/",
            json={
                "jsonrpc": "2.0",
                "id": "1",
                "method": "message/send",
                "params": {
                    "session_id": "123",
                    "message": {
                        "role": "user",
                        "messageId": "msg-1",
                        "parts": [
                            {"kind": "text", "text": data}
                        ]
                    }
                }
            }
        )

        try:
            result = response.json()

            text_output = result["result"]["artifacts"][0]["parts"][0]["text"]

            st.success("Analysis Complete!")
            st.text(text_output)

        except:
            st.error("Something went wrong")