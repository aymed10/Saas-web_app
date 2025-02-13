import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import json

# Synonym dictionary to enrich text
SYNONYMS = {
"équipe": ["équipe", "groupe", "bureau", "staff", "collectif", "team"],
"présidente": ["présidente", "cheffe", "leader", "responsable", "dirigeante"],
"vice-présidente": ["vice-présidente", "adjointe", "collaboratrice", "assistante de direction"],
"secrétaire": ["secrétaire", "administratrice", "responsable des dossiers"],
"trésorière": ["trésorière", "responsable financière", "gestionnaire de fonds"],
"responsable_communication": ["responsable communication", "community manager", "gestionnaire des réseaux sociaux"],
"mandats": ["mandats", "périodes de service", "durée de fonction"],
"secteur": ["secteur", "domaine", "industrie"],
"taille": ["taille", "dimension", "effectif"],
"siège_social": ["siège social", "adresse principale", "quartier général"],
"fondation": ["fondation", "création", "origine"],
"événements": ["événements", "manifestations", "activités", "rencontres"],
"intervenants": ["intervenants", "conférenciers", "experts"],
"activités": ["activités", "ateliers", "séances pratiques"],
"témoignages": ["témoignages", "avis", "retours d'expérience"],
"réalisations": ["réalisations", "succès", "projets accomplis"],
"projets_futurs": ["projets futurs", "plans", "objectifs à venir"],
"statistiques": ["statistiques", "chiffres", "données"],
"spécialisations": ["spécialisations", "options", "domaines de spécialité"],
"questions_et_réponses": ["questions et réponses", "FAQ", "aide en ligne"],
"actions": ["actions", "initiatives", "projets en cours"]
}



def flatten_and_enrich_json(obj, parent_key=''):
    """Recursively flattens JSON and adds synonyms for better retrieval."""
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            enriched_keys = SYNONYMS.get(k, [k])
            for synonym in enriched_keys:
                items.append(f"{parent_key}.{synonym}: {v}" if parent_key else f"{synonym}: {v}")
            items.extend(flatten_and_enrich_json(v, new_key))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            items.extend(flatten_and_enrich_json(v, f"{parent_key}[{i}]"))
    else:
        items.append(f"{parent_key}: {obj}")
    return items


def generate_and_save_embeddings(file_path="/home/aymed/Saas-web_app/Backend/IAF.json", embeddings_file="/home/aymed/Saas-web_app/Backend/faiss_index.bin", sentences_file="/home/aymed/Saas-web_app/Backend/sentences.pkl"):
    # Load the structured JSON
    with open(file_path, "r", encoding="utf-8") as f:
        structured_data = json.load(f)

    # Flatten and enrich the JSON structure
    sentences = flatten_and_enrich_json(structured_data)
    sentences = list(set(filter(None, sentences)))

    # Generate embeddings
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    embeddings = model.encode(sentences)
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Cosine similarity
    index.add(np.array(embeddings).astype('float32'))

    # Save index and sentences
    faiss.write_index(index, embeddings_file)
    with open(sentences_file, "wb") as f:
        pickle.dump(sentences, f)

    print("✅ Embeddings generated with synonym-enrichment!")

if __name__ == "__main__":
    generate_and_save_embeddings()
