from quiz.models import Question

QUESTIONS = [
    (
        "Tu es sur Kali. Tu veux vérifier si un fichier est lisible uniquement par son propriétaire. Quelle information cherches-tu et comment ?",
        "ls,-l,permissions"
    ),
    (
        "Un utilisateur se plaint qu’une commande fonctionne en root mais pas en user normal. Quelle piste vérifies-tu en premier ?",
        "sudo,permissions,path"
    ),
    (
        "Tu télécharges un script bash inconnu. Quelle est la première chose à faire avant de l’exécuter ?",
        "cat,less,chmod"
    ),
    (
        "Un fichier semble contenir du texte illisible. Quelle hypothèse fais-tu et que testes-tu ?",
        "file,strings,encoding"
    ),
    (
        "Tu suspectes qu’un mot de passe est caché dans un fichier texte. Quelle commande simple testes-tu ?",
        "grep,cat,less"
    ),
    (
        "Un service écoute sur un port inconnu. Comment identifies-tu ce service localement ?",
        "netstat,ss,lsof"
    ),
    (
        "Tu analyses une image PNG reçue dans un CTF. Quelle piste évidente testes-tu en premier ?",
        "strings,steghide,exif"
    ),
    (
        "Tu veux savoir si un fichier a été modifié récemment. Quelle information regardes-tu ?",
        "ls,stat,time"
    ),
    (
        "Un script ne s’exécute pas alors qu’il est correct. Quelle cause fréquente liée au système peux-tu vérifier ?",
        "chmod,permissions,shebang"
    ),
    (
        "Tu interceptes une chaîne encodée étrange. Quelle est la première vérification simple à faire ?",
        "base64,decode,echo"
    ),
    (
        "Un utilisateur est compromis. Quelle commande permet de voir ses dernières connexions ?",
        "last,w,who"
    ),
    (
        "Tu veux voir les processus lancés par un utilisateur précis. Quelle approche utilises-tu ?",
        "ps,grep,user"
    ),
    (
        "Tu dois comparer deux fichiers suspects rapidement. Quelle commande utilises-tu ?",
        "diff,cmp"
    ),
    (
        "Un fichier semble trop petit pour être normal. Quelle hypothèse fais-tu ?",
        "hidden,steganography"
    ),
    (
        "Un binaire ne se lance pas malgré les droits. Quelle cause système possible ?",
        "architecture,ldd,dependencies"
    ),
    (
        "Tu veux savoir si une machine est joignable avant un scan. Quelle commande simple ?",
        "ping,icmp"
    ),
    (
        "Tu analyses un log et vois beaucoup de tentatives échouées. Quelle attaque soupçonnes-tu ?",
        "bruteforce,password"
    ),
    (
        "Tu trouves un hash mais tu ignores l’algorithme. Quelle première étape ?",
        "identify,hashid"
    ),
    (
        "Un fichier zip est protégé par mot de passe. Quelle approche générale testes-tu ?",
        "dictionary,bruteforce"
    ),
    (
        "Tu veux vérifier si un script fait des actions réseau. Où regardes-tu ?",
        "curl,wget,requests"
    ),
]

def run():
    for q, k in QUESTIONS:
        Question.objects.create(text=q, keywords=k)
    print("Questions insérées")
