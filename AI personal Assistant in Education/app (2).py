##IMPORTING:
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplates import bot_template, user_template, css
from langchain.llms import HuggingFaceHub
import os


##FUNCTIONS TO HANDLE PROCESSES:
class AI_Educational_Assistant:
    
    def __init__(self, huggingface_hub_api_key):
        self.huggingface_hub_api_key = huggingface_hub_api_key
        st.set_page_config(page_title='Chat with Your own PDFs', page_icon=':books:')
        self._initialize_session_state()
        

    def _initialize_session_state(self):
        st.write(css, unsafe_allow_html=True)
        if "conversation" not in st.session_state:
            st.session_state.conversation = None

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None

    def extractPDFs(self, pdf_files):
        txt = ""
        for f in pdf_files:
            reader = PdfReader(f)
            for p in reader.pages:
                txt += p.extract_text()
        return txt

    def get_chunkies(self, text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text)
        return chunks

    def vector_transformation(self, text_chunks):     
        embeds = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeds)
        print(type(vectorstore))
        return vectorstore
        


    def convo_holder(self, vector_store):
        print("Creating ConversationRetrievalChain...")
        llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(),
            memory=memory
        )
        print("ConversationRetrievalChain created successfully.")
        return conversation_chain


        

    def input_handler(self, question):
        response = st.session_state.conversation({'question': question})
        st.session_state.chat_history = response['chat_history']

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

    def main(self):
        st.header("I'm your educational assistant. Let's learn!")
        question = st.text_input("What knowledge are you seeking?")

        if question:
            self.input_handler(question)

        with st.sidebar:
            st.subheader("Help me learn by dropping your files here")
            pdf_files = st.file_uploader("Help me learn!", type=['pdf'], accept_multiple_files=True)

            if st.button("OK"):
                with st.info("Processing your PDFs..."):
                    raw_text = self.extractPDFs(pdf_files)
                    text_chunks = self.get_chunkies(raw_text)
                    vector_store = self.vector_transformation(text_chunks)
                    st.write("I know it all")
                    st.session_state.conversation = self.convo_holder(vector_store)



##CALLING MAIN FUNCTION AND USING THE API KEYS:
if __name__ == '__main__':
    os.environ["HUGGINGFACEHUB_API_TOKEN"]= "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"
    HUGGINGFACEHUB_API_TOKEN= os.getenv("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")
    assistant= AI_Educational_Assistant(HUGGINGFACEHUB_API_TOKEN)
    assistant.main()


