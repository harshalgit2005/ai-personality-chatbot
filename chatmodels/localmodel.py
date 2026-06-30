
# Import ChatHuggingFace:
# Provides a chat interface compatible with LangChain.
#
# Import HuggingFacePipeline:
# Allows us to load and run Hugging Face models locally
# using the transformers pipeline.
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


# Create a local Hugging Face model.
#
# from_model_id() downloads the specified model
# (if not already present) and creates a transformers
# pipeline behind the scenes.
#
# model_id:
# Name of the model available on Hugging Face Hub.
#
# task:
# Defines what task the model should perform.
# "text-generation" means generating text from prompts.
#
# pipeline_kwargs:
# Additional settings passed to the transformers pipeline.
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(

        # Maximum number of new tokens the model
        # can generate in its response.
        max_new_tokens=512,

        # False = deterministic output.
        # True = sampling/randomness enabled.
        do_sample=False,

        # Helps reduce repeated words or phrases.
        # Values slightly above 1 discourage repetition.
        repetition_penalty=1.03,
    ),
)


# Wrap the local model inside ChatHuggingFace.
#
# This gives us the standard LangChain chat interface,
# allowing us to use invoke(), stream(), batch(), etc.
chat_model = ChatHuggingFace(llm=llm)


# Send a prompt to the model.
#
# The prompt is processed by TinyLlama running locally.
#
# invoke() returns an AIMessage object.
result = chat_model.invoke(
    "What is locally running model?"
)


# Print only the generated text.
#
# result is an AIMessage object.
# result.content contains the actual response.
print(result.content)
