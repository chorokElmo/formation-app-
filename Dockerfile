# ── Étape 1 : image de base légère
FROM python:3.12-slim

# Métadonnées
LABEL maintainer="FormationHub DevOps Team"
LABEL description="Application web Flask – Liste de formations"

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Répertoire de travail
WORKDIR /app

# Copier et installer les dépendances en premier (cache Docker optimisé)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 3000

# Lancer avec Gunicorn (serveur WSGI de production)
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "2", "--timeout", "60", "app:app"]
