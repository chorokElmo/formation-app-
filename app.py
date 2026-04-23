from flask import Flask, render_template

app = Flask(__name__)

formations = [
    {
        "id": 1,
        "titre": "DevOps & CI/CD",
        "description": "Maîtrisez Docker, Kubernetes, GitHub Actions et les pipelines d'intégration continue.",
        "duree": "12 semaines",
        "niveau": "Intermédiaire",
        "icon": "⚙️",
        "tag": "Infrastructure"
    },
    {
        "id": 2,
        "titre": "Développement Web Full Stack",
        "description": "De la conception à la mise en production : HTML, CSS, JavaScript, React et Node.js.",
        "duree": "16 semaines",
        "niveau": "Débutant",
        "icon": "🌐",
        "tag": "Web"
    },
    {
        "id": 3,
        "titre": "Python & Data Science",
        "description": "Analyse de données, machine learning et visualisation avec Python, Pandas et Scikit-learn.",
        "duree": "10 semaines",
        "niveau": "Intermédiaire",
        "icon": "🐍",
        "tag": "Data"
    },
    {
        "id": 4,
        "titre": "Cybersécurité Fondamentaux",
        "description": "Sécurité réseau, ethical hacking, cryptographie et protection des systèmes d'information.",
        "duree": "8 semaines",
        "niveau": "Avancé",
        "icon": "🔐",
        "tag": "Sécurité"
    },
    {
        "id": 5,
        "titre": "Cloud Computing AWS",
        "description": "Architecture cloud, services AWS, déploiement scalable et gestion des coûts.",
        "duree": "14 semaines",
        "niveau": "Intermédiaire",
        "icon": "☁️",
        "tag": "Cloud"
    },
    {
        "id": 6,
        "titre": "Intelligence Artificielle",
        "description": "Deep learning, NLP, computer vision et déploiement de modèles en production.",
        "duree": "20 semaines",
        "niveau": "Avancé",
        "icon": "🤖",
        "tag": "IA"
    },
]

@app.route("/")
def index():
    return render_template("index.html", formations=formations)

@app.route("/formations")
def liste_formations():
    return render_template("formations.html", formations=formations)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
