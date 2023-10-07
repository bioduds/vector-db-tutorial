# import os
# import openai

# # Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")

import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


# Call the `davinci` engine to generate embeddings
response = openai.Embedding.create(
    input="I might be a cat outside the multiverse trying to communicate with myself",
    model="text-embedding-ada-002"
)

# Extract the embeddings from the response
embeddings = response['data'][0]['embedding']

# Print the embeddings
print(embeddings)