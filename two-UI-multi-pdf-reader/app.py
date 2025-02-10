import streamlit as st
from pdf_reader import extract_text_from_pdf
from text_chunker import chunk_text_by_newlines
from rag_search import retrieve_relevant_chunks
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the sidebar for page selection
page = st.sidebar.selectbox("Choose Page", ["Admin Setup", "Annotator Q&A"])

# Create session state to store chunks
if "all_chunks" not in st.session_state:
    st.session_state["all_chunks"] = []

if page == "Admin Setup":
    st.title("📄 Admin: Document Setup")

    # Step 1: PDF Upload
    uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Step 2: Extract text from PDF
            with st.spinner(f"Extracting text from {uploaded_file.name}..."):
                document_text = extract_text_from_pdf(uploaded_file)
                st.success(f"Text extracted from {uploaded_file.name} successfully!")

            # Step 3: Display document preview
            st.subheader(f"📃 Document Preview: {uploaded_file.name}")
            st.text_area(f"Preview of {uploaded_file.name} content", document_text[:1000], height=200)

            # Step 4: Chunk the text
            chunks = chunk_text_by_newlines(document_text, chunk_size=1000, overlap=200)
            st.session_state["all_chunks"].extend(chunks)  # Store chunks globally

        st.success("Document setup complete! Ready for Q&A on the annotator page.")

elif page == "Annotator Q&A":
    st.title("🤖 Annotator: Q&A Interface")

    # Step 1: Input question
    question = st.text_input("Ask a question about the uploaded PDFs")

    if st.button("Get Answer"):
        if not question.strip():
            st.warning("Please enter a question.")
        elif not st.session_state["all_chunks"]:
            st.error("No documents have been set up. Please ask the admin to upload and set up PDFs.")
        else:
            # Step 2: Retrieve relevant chunks using RAG
            with st.spinner("Retrieving relevant chunks from documents..."):
                relevant_context = retrieve_relevant_chunks(question, st.session_state["all_chunks"], top_k=5)

            # Step 3: Generate answer using OpenAI's ChatCompletion API
            with st.spinner("Generating answer..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant. Read the provided document context and answer the user's question accurately and concisely."},
                        {"role": "user", "content": f"Document Context: {relevant_context}\n\nQuestion: {question}"}
                    ],
                    max_tokens=500
                )
                answer = response['choices'][0]['message']['content'].strip()

                # Step 4: Display the answer
                st.subheader("🤖 Answer")
                st.write(answer)
