import streamlit as st
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

# -- load env --
import os
from dotenv import load_dotenv
load_dotenv()

# --- Default structured dataset (firmware CVEs) ---
default_firmware_cves = [
    {"component": "PCIe Controller", "cve": "CVE-2026-1234", 
     "description": "Buffer overflow in DMA engine"},
    {"component": "BIOS Firmware", "cve": "CVE-2026-5678", 
     "description": "Privilege escalation via SMM handler"},
    {"component": "Network Adapter Firmware", "cve": "CVE-2026-9012", 
     "description": "Remote code execution in packet parser"}
]

# --- Helper functions ---
def retriever(query: str, dataset):
    return [doc for doc in dataset if query.lower() in doc["component"].lower() 
            or query.lower() in doc["description"].lower()]

def format_docs(docs):
    return "\n\n".join(f"{d['component']} - {d['cve']} - {d['description']}" for d in docs)

# --- Prompt template ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a firmware security assistant. Use the context to answer clearly."),
    ("human", "Question: {input}\nContext: {context}")
])

# --- Initialize Groq LLM ---
llm = ChatGroq(model="openai/gpt-oss-120b")

# --- Streamlit UI ---
st.title("🔐 Firmware Component Security RAG (Vectorless)")

# File upload option
uploaded_file = st.file_uploader("Upload a JSON file with CVEs", type=["json"])

if uploaded_file is not None:
    try:
        dataset = json.load(uploaded_file)
        st.success("✅ Custom CVE dataset loaded.")
    except Exception as e:
        st.error(f"Error loading file: {e}")
        dataset = default_firmware_cves
else:
    dataset = default_firmware_cves
    st.info("Using default CVE dataset.")

# Build RAG chain dynamically with chosen dataset
rag_chain = (
    {"context": lambda q: format_docs(retriever(q, dataset)), "input": RunnablePassthrough()} 
    | prompt 
    | llm 
    | StrOutputParser()
)

query = st.text_input("Enter your security research question:", "Explain BIOS firmware risks")

if st.button("Run Query"):
    result = rag_chain.invoke(query)
    st.subheader("Answer")
    st.write(result)

    # Show retrieved context
    retrieved = retriever(query, dataset)
    if retrieved:
        st.subheader("Retrieved CVEs")
        for doc in retrieved:
            st.write(f"- {doc['component']} | {doc['cve']} | {doc['description']}")
