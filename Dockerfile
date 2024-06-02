# Utiliser une image de base officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]
