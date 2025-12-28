import streamlit as st
import subprocess
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')
# loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidfd = pickle.load(open('tfidf.pkl', 'rb'))

def clean_resume(resume_text):
            clean_text = re.sub('http\S+\s*', ' ', resume_text)
            clean_text = re.sub('RT|cc', ' ', clean_text)
            clean_text = re.sub('#\S+', '', clean_text)
            clean_text = re.sub('@\S+', '  ', clean_text)
            clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
            clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
            clean_text = re.sub('\s+', ' ', clean_text)
            return clean_text
def main():
    """ Login """
    st.sidebar.header("Welcome to CV Pro")
    menu = ["Home", "Resume Builder", "Resume Screeening"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":

        st.title("Echo")
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        if prompt := st.chat_input("Ask me"):
            # Display user message in chat message container
            st.chat_message("user").markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            if prompt == "hi":
                response = f"Echo: Hello :) "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})

            elif prompt == "super hero":
                response = f"Echo: Spider-man "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            elif prompt == "animation":
                response = f"Echo: Spirited Away "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            elif prompt == "comedy":
                response = f"Echo: Big Daddy "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            elif prompt == "action":
                response = f"Echo: Mission: Impossible "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                response = f"Echo: Sorry:( Try again "
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})

    elif choice == "Resume Builder":
        subprocess.run(["streamlit", "run", ""])



    elif choice == "Resume Screeening":
        subprocess.run(["streamlit", "run", "main.py"])



if __name__ == '__main__':
    main()
