import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai
from langchain.memory import ConversationBufferMemory
from langchain.chains import conversational_retrieval
from htmlTemplate import css, bot_template , user_template



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text 

def get_text_chunks(text):

    text_splitter = CharacterTextSplitter(
    separator  ="\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function =len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts = text_chunks , embedding = embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = openai()
    memory = ConversationBufferMemory(memory_key='chat_history' , return_messages= True)
    converstion_chain = conversational_retrieval.from_llm(
        llm = llm,
        retrieval = vectorstore.as_retrieval(),
        memory = memory

    )

    return conversation_chain 


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.write(response)
    




   

print("Script is running...")  # This should appear in the terminal

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With Multiple PDF" , page_icon=":books:")

    st.write(css, unsafe_allow_html = True)

    if "converssation" not in  st.session_state:
        st.session_state.conversation = None

    st.header("Chat With Multiple PDF :books:")
    
    user_question = st.text_input("Ask a Qustion about your documents:")
    if user_question:
        handle_userinput(user_question)


    st.write(user_template.replace("{{MSG}}", "Hello Robot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs= st.file_uploader("Upload Your PDF here and click  on 'process'", accept_multiple_files=True)
        if  st.button("Process"):
            with st.spinner("Processing"):
            #get pdf text
             raw_text = get_pdf_text(pdf_docs)
            

            #get the text chunks
            text_chunks = get_text_chunks(raw_text)
            

            #create vector store 

            vectorstore = get_vectorstore(text_chunks)

            #create conversation  chain
        st.session_state.conversation = get_conversation_chain(vectorstore)

    st.session_state.conversation 




if __name__ == "__main__":
    main()  