
# Import load_dotenv to load environment variables
# from the .env file into the application.
from dotenv import load_dotenv


# Load all variables from the .env file.
# This is where the Hugging Face API token is usually stored.
load_dotenv()


# Import HuggingFaceEndpoint:
# Connects to a model hosted on Hugging Face Inference API.
#
# Import ChatHuggingFace:
# Provides a chat-model interface similar to ChatOpenAI,
# ChatGroq, etc.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


# Create a Hugging Face endpoint object.
#
# repo_id specifies which model should be used.
#
# DeepSeek-V4-Pro is the model repository hosted on
# Hugging Face.
#
# This object is responsible for communicating with
# Hugging Face servers.
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
)


# Wrap the endpoint inside ChatHuggingFace.
#
# ChatHuggingFace converts the endpoint into a chat model
# compatible with LangChain's standard chat interface.
model = ChatHuggingFace(llm=llm)


# Send a prompt to the model.
#
# invoke() sends the request to the Hugging Face model
# and returns an AIMessage object containing the response.
response = model.invoke(
    "Write a short poem about Python programming."
)


# Print only the generated text.
#
# response is an AIMessage object.
# response.content contains the actual generated answer.
print(response.content)
