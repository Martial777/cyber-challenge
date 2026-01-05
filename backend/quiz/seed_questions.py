from quiz.models import Question

QUESTIONS = [
    {"text": "Que signifie le mot « cyber » dans le domaine informatique ?", "keywords": "informatique,securite,technologie"},
    {"text": "À quoi sert principalement un mot de passe ?", "keywords": "securite,acces,protection"},
    {"text": "Quel système d’exploitation est le plus utilisé sur les serveurs ?", "keywords": "linux,serveur"},
    {"text": "Kali Linux est principalement utilisé pour quoi ?", "keywords": "securite,test,intrusion"},
    {"text": "Que signifie le mot « hacker » à l’origine ?", "keywords": "passionne,programmation"},
    {"text": "Quelle commande Linux permet d’afficher le contenu d’un dossier ?", "keywords": "ls,linux"},
    {"text": "Quelle commande Linux permet de connaître le dossier courant ?", "keywords": "pwd,linux"},
    {"text": "Que signifie le sigle IP en réseau ?", "keywords": "internet,protocole"},
    {"text": "À quoi sert une adresse IP ?", "keywords": "identification,reseau"},
    {"text": "Qu’est-ce qu’un réseau informatique ?", "keywords": "ordinateurs,connexion"},
    {"text": "Qu’appelle-t-on une attaque par phishing ?", "keywords": "fraude,email"},
    {"text": "Quel est le but principal d’un antivirus ?", "keywords": "protection,malware"},
    {"text": "Que signifie le terme « malware » ?", "keywords": "logiciel,malveillant"},
    {"text": "Qu’est-ce qu’un pare-feu (firewall) ?", "keywords": "protection,reseau"},
    {"text": "Pourquoi utilise-t-on HTTPS au lieu de HTTP ?", "keywords": "securite,cryptage"},
    {"text": "À quoi sert la commande ping ?", "keywords": "reseau,test"},
    {"text": "Qu’est-ce qu’un mot de passe fort ?", "keywords": "long,complexe"},
    {"text": "Quelle est la différence entre Internet et le Wi-Fi ?", "keywords": "reseau,connexion"},
    {"text": "Citer un type d’attaque informatique connu.", "keywords": "attaque,cyber"},
    {"text": "Pourquoi la cybersécurité est-elle importante aujourd’hui ?", "keywords": "protection,donnees"},
]

added = 0
skipped = 0

for q in QUESTIONS:
    obj, created = Question.objects.get_or_create(
        text=q["text"],
        defaults={"keywords": q["keywords"]}
    )
    if created:
        added += 1
    else:
        skipped += 1

print(f"✔ Import terminé : {added} ajoutées / {skipped} déjà existantes")
