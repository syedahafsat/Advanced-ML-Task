import streamlit as st
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
st.set_page_config(page_title="📄Chat with Your Document", page_icon="🤖")
st.title("🤖 Context-Aware Chatbot using LangChain")
st.markdown("Upload a '.txt' file and ask questions about it!")
uploaded_file = st.file_uploader("(TXT file)",type=["txt"])
loader= TextLoader("multilang.txt")
documents= loader.load()
TextSplitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
texts = TextSplitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(texts, embeddings)
st.success("Document processed! Ask questions below:")
query = st.text_input("Ask something based on the uploaded content:")
if query:
    results=vectorstore.similarity_search(query, k=2)
    answer=results[0].page_content
    st.markdown("### Answer:")
    st.write(answer)

