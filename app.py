
"""
====================================================
AI Studio
====================================================
Author : Lakshman

Features
---------
✔ Gemini Chat
✔ Gemini Vision
✔ AI Image Generator
✔ PDF RAG
====================================================
"""

import os
import streamlit as st

from chatbot import ask_ai

from vision import (
    describe_image,
    extract_text,
    ask_image
)

from image_generator import generate_image

from rag import (
    build_vector_database,
    ask_pdf
)

from config import (
    APP_NAME,
    PDF_FOLDER
)

# ====================================================
# Page Configuration
# ====================================================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide"
)

# ====================================================
# Title
# ====================================================

st.title("🤖 AI Studio")

st.markdown("---")

# ====================================================
# Sidebar
# ====================================================

menu = st.sidebar.radio(

    "Select Module",

    [
        "💬 Chatbot",
        "👁 Vision",
        "🎨 Image Generator",
        "📄 RAG PDF"
    ]

)

# ====================================================
# Chatbot
# ====================================================

if menu == "💬 Chatbot":

    st.header("Gemini Chatbot")

    prompt = st.text_area(
        "Enter your question"
    )

    if st.button("Ask"):

        if prompt:

            with st.spinner("Thinking..."):

                answer = ask_ai(prompt)

            st.success(answer)

# ====================================================
# Vision
# ====================================================

elif menu == "👁 Vision":

    st.header("Gemini Vision")

    image = st.file_uploader(

        "Upload Image",

        type=["png", "jpg", "jpeg"]

    )

    if image:

        path = os.path.join(
            "uploads",
            image.name
        )

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        with open(path, "wb") as f:

            f.write(image.read())

        st.image(path)

        option = st.selectbox(

            "Choose Task",

            [
                "Describe Image",
                "Extract Text",
                "Ask Question"
            ]

        )

        if option == "Describe Image":

            if st.button("Run"):

                st.write(
                    describe_image(path)
                )

        elif option == "Extract Text":

            if st.button("Run"):

                st.write(
                    extract_text(path)
                )

        else:

            question = st.text_input(
                "Question"
            )

            if st.button("Ask"):

                st.write(
                    ask_image(
                        path,
                        question
                    )
                )

# ====================================================
# Image Generator
# ====================================================

elif menu == "🎨 Image Generator":

    st.header("AI Image Generator")

    prompt = st.text_area(
        "Enter Prompt"
    )

    if st.button("Generate Image"):

        with st.spinner("Generating..."):

            image_path = generate_image(
                prompt
            )

        if os.path.exists(image_path):

            st.image(image_path)

            with open(image_path, "rb") as f:

                st.download_button(

                    "Download",

                    data=f,

                    file_name=os.path.basename(
                        image_path
                    )

                )

        else:

            st.error(image_path)

# ====================================================
# RAG
# ====================================================

elif menu == "📄 RAG PDF":

    st.header("PDF Question Answering")

    pdf = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )

    if pdf:

        os.makedirs(
            PDF_FOLDER,
            exist_ok=True
        )

        pdf_path = os.path.join(
            PDF_FOLDER,
            pdf.name
        )

        with open(pdf_path, "wb") as f:

            f.write(pdf.read())

        if st.button("Create Vector Database"):

            with st.spinner("Processing PDF..."):

                total = build_vector_database(
                    pdf_path
                )

            st.success(
                f"{total} chunks indexed."
            )

        question = st.text_input(
            "Ask Question"
        )

        if st.button("Get Answer"):

            with st.spinner("Searching..."):

                answer = ask_pdf(question)

            st.write(answer)

# ====================================================
# Footer
# ====================================================

st.markdown("---")

st.caption(
    "AI Studio | Gemini + Vision + Image Generation + RAG"
)