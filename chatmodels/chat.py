
# Import ChatGroq from LangChain.
# ChatGroq provides an interface to interact with Groq-hosted LLMs.
from langchain_groq import ChatGroq


# Import load_dotenv to load environment variables
# from the .env file into the application.
from dotenv import load_dotenv


# Load all environment variables from the .env file.
# This allows us to access GROQ_API_KEY securely
# without hardcoding it in the source code.
load_dotenv()


# Create a ChatGroq model object.
# model      -> Specifies which LLM to use.
# temperature -> Controls creativity/randomness of responses.
# max_tokens -> Maximum number of tokens generated in the output.
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1.2,
    max_tokens=248,
)


# Send a prompt to the model using invoke().
# invoke() sends the request to the LLM and returns
# an AIMessage object containing the generated response.
response = model.invoke(
    "Write a short poem about Python programming."
)


# Print only the generated text.
# response is an AIMessage object and
# response.content contains the actual answer.
print(response.content)
