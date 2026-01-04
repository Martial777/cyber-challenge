from quiz.models import Question

questions = [
    {"text": "Quel port est utilisé par SSH par défaut ?", "keywords": "22"},
    {"text": "Quel protocole est sécurisé pour la navigation web ?", "keywords": "https,https://"},
    {"text": "Quelle commande Linux permet de lister les fichiers ?", "keywords": "ls"},
    {"text": "Que fait la commande 'chmod' ?", "keywords": "permissions,chmod"},
    {"text": "Que signifie 'stéganographie' ?", "keywords": "cacher,masquer"},
    {"text": "Quel outil Kali permet de scanner un réseau et ses ports ?", "keywords": "nmap"},
    {"text": "Que signifie 'phishing' ?", "keywords": "hameçonnage,vol,info"},
    {"text": "Quel outil Kali permet d'analyser les paquets réseau ?", "keywords": "wireshark"},
    {"text": "Quelle commande Linux affiche le répertoire courant ?", "keywords": "pwd"},
    {"text": "Quel algorithme symétrique est souvent utilisé pour chiffrer les données ?", "keywords": "aes"},
    {"text": "Quel protocole est utilisé pour envoyer des emails de manière sécurisée ?", "keywords": "smtp"},
    {"text": "Que fait la commande 'mkdir' en Linux ?", "keywords": "mkdir,dossier"},
    {"text": "Que fait la commande 'cat' en Linux ?", "keywords": "cat,afficher"},
    {"text": "Quel outil Kali permet de cracker des mots de passe ?", "keywords": "john,johntheripper"},
    {"text": "Que fait la commande 'grep' en Linux ?", "keywords": "grep,chercher"},
    {"text": "Que fait la commande 'ping' ?", "keywords": "ping,connectivité"},
    {"text": "Quel protocole permet le transfert de fichiers sécurisé ?", "keywords": "sftp"},
    {"text": "Que fait la commande 'whoami' ?", "keywords": "whoami,utilisateur"},
    {"text": "Que signifie 'MITM' ?", "keywords": "man in the middle"},
    {"text": "Que fait la commande 'scp' en Linux ?", "keywords": "scp,copier,ssh"}
]

for q in questions:
    Question.objects.create(text=q["text"], keywords=q["keywords"])

print("✅ 20 questions insérées dans la base.")
