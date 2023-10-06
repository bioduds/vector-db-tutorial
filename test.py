# import os
# import openai

# # Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")


import openai

# Set your OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Call the `davinci` engine to generate embeddings
response = openai.Embedding.create(
    input="I might be a cat outside the multiverse trying to communicate with myself",
    model="text-embedding-ada-002"
)

# Extract the embeddings from the response
embeddings = response['data'][0]['embedding']

# Print the embeddings
print(embeddings)