from flask import Flask, request, jsonify
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  # CORS pour Flask

# Liste de mots sensibles
mots_sensibles = ["sexe", "décapitation", "pornographie"]

# Fonction pour vérifier si le texte contient des mots sensibles
def contient_mots_sensibles(texte):
    mots = texte.split()  # Divise le texte en mots
    for mot in mots:
        if mot.lower() in mots_sensibles:
            return True  # Le texte contient un mot sensible
    return False  # Aucun mot sensible  trouvé

@app.route('/verifier-texte', methods=['POST'])
def verifier_texte():
    data = request.get_json()
    texte_utilisateur = data.get('texte', '')

    if contient_mots_sensibles(texte_utilisateur):
        resultat = {'valide': False, 'message': 'Le texte contient des mots sensibles.'}
    else:
        resultat = {'valide': True, 'message': 'Le texte est valide.'}

    return jsonify(resultat)

if __name__ == '__main__':
    app.run(debug=True)
