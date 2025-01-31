import os
import time
import requests
import duckdb
import pandas as pd
from dotenv import load_dotenv
from io import StringIO
from colorama import Fore, Style, init

########################
##### Configuration #####
########################

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Initialisation de Colorama
init()

# Configuration des chemins et de la base DuckDB
DATABASE_PATH = "file.duckdb"  # Chemin vers la base DuckDB
DATA_DIR = "./data_frame"      # Dossier où stocker les fichiers Parquet
os.makedirs(DATA_DIR, exist_ok=True)  # Créer le dossier s'il n'existe pas

###############################
##### Fonction pour quitter #####
###############################
def leave():
    print(f"{Style.BRIGHT}{Fore.BLUE}👋 Programme terminé.{Style.RESET_ALL}")
    exit(0)

##############################################
##### Fonction pour générer un nom unique #####
##############################################
def generate_unique_filename(base_name, extension="parquet"):
    """Génère un nom de fichier unique avec un timestamp."""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.{extension}"

##############################################
##### Fonction pour récupérer la clé API #####
##############################################
def get_secret_token():
    """Récupère la clé API depuis les variables d'environnement."""
    api_key = os.getenv("SECRET_TOKEN")
    if not api_key:
        print(f"{Style.BRIGHT}{Fore.RED}❌ Clé API manquante dans .env !{Style.RESET_ALL}")
        leave()
    return api_key

####################################################
##### Fonction pour sauvegarder un fichier #####
####################################################
def save_parquet(dataframe, source_name):
    """Enregistre le DataFrame au format Parquet avec un nom unique."""
    file_name = generate_unique_filename(source_name, "parquet")
    file_path = os.path.join(DATA_DIR, file_name)
    dataframe.to_parquet(file_path, engine="pyarrow", index=False)
    print(f"{Style.BRIGHT}{Fore.GREEN}✅ Fichier enregistré : {file_path}{Style.RESET_ALL}")
    return file_path

##############################################
##### Fonction pour convertir JSON en Parquet #####
##############################################
def convert_json_to_parquet(json_data, source_name):
    """Convertit des données JSON en Parquet et les sauvegarde."""
    try:
        df = pd.DataFrame(json_data)
        return save_parquet(df, source_name)
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}💥 Erreur JSON -> Parquet : {e}{Style.RESET_ALL}")

##############################################
##### Fonction pour convertir CSV en Parquet #####
##############################################
def convert_csv_to_parquet(csv_data, source_name):
    """Convertit des données CSV en Parquet et les sauvegarde."""
    try:
        df = pd.read_csv(StringIO(csv_data))
        return save_parquet(df, source_name)
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}💥 Erreur CSV -> Parquet : {e}{Style.RESET_ALL}")

################################################
##### Charger les fichiers Parquet dans DuckDB #####
################################################
def load_parquet_to_duckdb(parquet_path):
    """Charge un fichier Parquet dans DuckDB sous le schéma `raw`."""
    table_name = os.path.splitext(os.path.basename(parquet_path))[0]  # Nom sans extension
    conn = duckdb.connect(DATABASE_PATH)
    conn.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    query = f"""
    CREATE OR REPLACE TABLE raw.{table_name} AS
    SELECT * FROM read_parquet('{parquet_path}');
    """
    conn.execute(query)
    print(f"{Style.BRIGHT}{Fore.GREEN}✅ Table raw.{table_name} créée dans DuckDB.{Style.RESET_ALL}")
    conn.close()

###############################################################
##### Fonction pour détecter et traiter les formats de données #####
###############################################################
def process_data_format(response, source_name):
    """Détecte et traite les formats JSON ou CSV des données."""
    try:
        response.json()
        print(f"{Style.BRIGHT}{Fore.CYAN}📄 Format détecté : JSON{Style.RESET_ALL}")
        parquet_path = convert_json_to_parquet(response.json(), source_name)
        load_parquet_to_duckdb(parquet_path)
    except ValueError:
        try:
            if "," in response.text or ";" in response.text:
                print(f"{Style.BRIGHT}{Fore.CYAN}📄 Format détecté : CSV{Style.RESET_ALL}")
                parquet_path = convert_csv_to_parquet(response.text, source_name)
                load_parquet_to_duckdb(parquet_path)
        except Exception as e:
            print(f"{Style.BRIGHT}{Fore.RED}💣 Format inconnu ou erreur : {e}{Style.RESET_ALL}")

####################################
##### Appeler une API et traiter #####
####################################
def api_call(url=None):
    """Appelle une API et traite les données."""
    if not url:
        url = input("🏁 Entrez l'URL de l'API : ").strip()

    headers = {"Accept": "application/json, application/csv"}
    api_key = get_secret_token()
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            process_data_format(response, "api_data")
        elif response.status_code == 401:
            print(f"{Style.BRIGHT}{Fore.RED}💥 Non autorisé. Vérifiez votre clé API.{Style.RESET_ALL}")
        elif response.status_code == 404:
            print(f"{Style.BRIGHT}{Fore.RED}❌ Ressource introuvable (404).{Style.RESET_ALL}")
        else:
            print(f"{Style.BRIGHT}{Fore.RED}💣 Erreur HTTP {response.status_code}.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}💥 Erreur lors de l'appel à l'API : {e}{Style.RESET_ALL}")

###########################
##### Point d'entrée #####
###########################
def main():
    print(f"{Style.BRIGHT}{Fore.GREEN}🚀 Script démarré...{Style.RESET_ALL}")
    api_call()

#########################
##### Exécution #####
#########################
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Style.BRIGHT}{Fore.BLUE}👋 Interruption par l'utilisateur. Programme terminé.{Style.RESET_ALL}")
