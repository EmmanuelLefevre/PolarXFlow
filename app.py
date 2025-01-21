import sys
from dotenv import load_dotenv



################
##### Load #####
################
# Charger variables d'environnement
load_dotenv()



###################################################
##### Fonction pour choisir l'URL à scrapper' #####
###################################################



################
##### Main #####
################
def main():
  # Demander à l'utilisateur de choisir un fichier CSV



#####################
##### Execution #####
#####################
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("💥 Opération interrompue par l'utilisateur. Programme terminé.")
  finally:
    sys.exit(0)
