import streamlit as st
from transformers import pipeline

# ✅ Load your trained model or pre-trained model
MODEL_PATH = "C:/Users/talha/news_model"  # <-- Change if you want to use another model
classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)

# ✅ Label Mapping
label_map = {
    0: "Business",
    1: "Entertainment",
    2: "Health/Medical",
    3: "Science/Technology"
}

# ✅ Streamlit UI
st.title("📰 News Topic Classifier")
st.write("Enter a news headline or text, and the model will predict the topic.")

user_input = st.text_area("Enter News Text Here", "Microsoft announces new AI features in Windows")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠ Please enter some text to classify.")
    else:
        result = classifier(user_input)
        predicted_label_num = int(result[0]['label'].split('_')[-1])
        predicted_topic = label_map[predicted_label_num]
        confidence = result[0]['score']

        st.success(f"**Predicted Topic:** {predicted_topic}")
        st.info(f"**Confidence:** {confidence:.2f}")