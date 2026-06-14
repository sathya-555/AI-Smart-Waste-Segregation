import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="AI Smart Waste Segregation Assistant",
    page_icon="♻️",
    layout="wide"
)

st.title("♻️ AI Smart Waste Segregation & Sustainability Advisor")
st.markdown("### SDG 12 - Responsible Consumption and Production")

st.info(
    "This AI-powered system helps users identify waste categories, "
    "understand environmental impact, and receive disposal guidance."
)

waste_data = {
    "plastic bottle": {
        "category": "Recyclable Waste",
        "impact": "Plastic may remain in the environment for hundreds of years.",
        "disposal": "Place in recycling bin.",
        "score": 60
    },
    "banana peel": {
        "category": "Wet Waste",
        "impact": "Biodegradable and suitable for composting.",
        "disposal": "Place in compost bin.",
        "score": 95
    },
    "battery": {
        "category": "E-Waste",
        "impact": "Contains hazardous materials that may contaminate soil and water.",
        "disposal": "Take to an authorized e-waste collection center.",
        "score": 20
    },
    "glass bottle": {
        "category": "Recyclable Waste",
        "impact": "Can be recycled multiple times.",
        "disposal": "Place in glass recycling container.",
        "score": 85
    }
}

tab1, tab2 = st.tabs(["Text Classification", "Image Upload"])

with tab1:
    item = st.text_input("Enter Waste Item")

    if st.button("Analyze Waste"):
        item = item.lower().strip()

        if item in waste_data:
            result = waste_data[item]

            st.success("Analysis Completed")

            st.subheader("Waste Category")
            st.write(result["category"])

            st.subheader("Environmental Impact")
            st.write(result["impact"])

            st.subheader("Disposal Recommendation")
            st.write(result["disposal"])

            st.subheader("Sustainability Score")
            st.progress(result["score"] / 100)
            st.write(f"{result['score']}/100")

        else:
            st.warning("Waste item not available in knowledge base.")

with tab2:
    uploaded_file = st.file_uploader(
        "Upload Waste Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        st.success("Demo Classification")

        st.write("Predicted Category: Recyclable Waste")
        st.write("Environmental Impact: Plastic waste contributes to pollution.")
        st.write("Recommendation: Recycle properly.")
        st.progress(0.60)

st.markdown("---")

st.subheader("Why Proper Waste Segregation Matters")

st.write("""
- Reduces landfill waste
- Improves recycling efficiency
- Protects ecosystems
- Supports sustainable communities
- Promotes circular economy
""")
