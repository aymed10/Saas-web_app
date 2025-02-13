from openai import OpenAI
import os
import pickle
from google.cloud import secretmanager
import argparse
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def get_secret(secret_name):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    client = secretmanager.SecretManagerServiceClient()
    secret_path = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(request={"name": secret_path})
    return response.payload.data.decode("UTF-8")

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def load_embeddings(embeddings_file="/home/aymed/Saas-web_app/Backend/faiss_index.bin", sentences_file="/home/aymed/Saas-web_app/Backend/sentences.pkl"):
    # Load FAISS index
    index = faiss.read_index(embeddings_file)

    # Load sentences
    with open(sentences_file, "rb") as f:
        sentences = pickle.load(f)

    return index, sentences

# Initialize once
INDEX, SENTENCES = load_embeddings()

def get_relevant_context(query):
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    query_embedding = model.encode([query])[0].astype('float32')

    # Retrieve more context to capture all possible matches
    _, indices = INDEX.search(np.array([query_embedding]), k=15)
    relevant_sentences = [SENTENCES[i] for i in indices[0]]

    return " ".join(relevant_sentences)



def generate_response(prompt : str):
    context = get_relevant_context(prompt)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Vous êtes un chatbot spécialisé dans l'association Ingénieure au Féminin (IAF). "
                    "Les données proviennent d'un fichier hiérarchique enrichi de synonymes pour mieux comprendre les demandes. "
                    "Si une information semble manquante, cherchez des termes proches (ex: 'bureau' pour 'équipe', 'cheffe' pour 'présidente').\n\n"
                    f"Contexte :\n{context}"
                )
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    response = completion.choices[0].message.content
    print(response)
    return response
