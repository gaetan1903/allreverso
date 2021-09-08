# Documentation du module python `allreverso`
[<img src="../python_allreverso.png" width="50" alt="logo de allreverso">](https://petitpotiron.github.io/python-reverso/fr/)


[![widget du serveur discord](https://discord.com/api/guilds/831480772455038996/embed.png)](https://discord.gg/v4yfnjWKvy)
[![version de allreverso](https://img.shields.io/pypi/v/allreverso.svg)](https://pypi.org/project/allreverso/)
[![versions de python supportées](https://img.shields.io/pypi/pyversions/allreverso.svg)](https://pypi.org/project/allreverso/)
## Installation
Pour accéder aux services qu'offre ce magnifique package, il faut tout d'abord l'installer !

Vous avez le choix entre plusieurs façons pour installer ce super module:
**Python 3.5 ou supérieur est requis**
 ```
 # Linux / macOS
 python3 -m pip install -U allreverso
 # Windows
 py -3 -m pip install -U allreverso
 ```

# Le commencement
Voici la base du module, qui est nécessaire à tout travail avec ce dernier.
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
```

# Différentes fonctions
### Traduction
Pour traduire un texte, il suffit d'utiliser la fonction `translate()` du client reverso:
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> client.translate("fr", "en", "Bonjour !")
['hello!']
```
client.translate(source, cible, text)
- source : str, doit être dans [les langues supportées](#langues-supportées)
- target : str, doit être dans [les langues supportées](#langues-supportées)
- text : str
### Correction de texte
Pour corriger un texte, on peut utiliser la fonction  `correct()` du client reverso :


**⚠️Cette fonction ne marche que pour les langues `français`et `anglais`. ⚠️**
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> client.correct("fr", "Bonjoure !").text
['bonjour']
>>> res = client.correct("fr", "Bonjoure !")
>>> print(res)
['Bonjour']
>>> print(res.description)
'''
Erreur de grammaire: Bonjoure --> Bonjour
Dans ce contexte, le mot #!Bonjoure#$ pourrait être confondu avec son homophone #!bonjour#$.

'''
```
client.correct(languague, text)
- languague : str doit être dans [les langues supportées](#langues-supportées) et doit être différent de `tu` ou `ch`
- text : str
### Obtenir les synonymes d'un mot
Pour obtenir les synonymes d'un mot, on peut utiliser la fonction `synonymize()`du client reverso :


**⚠️Cette fonction ne marche pas pour les langues `Turc` et `Chinois`. ⚠️**
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> client.synonymize("fr", "bateau")
['embarcation', 'barque', 'navire', 'canot', 'paquebot', 'voile', 'vaisseau', 'chaloupe', 'vapeur', 'bâtiment', 'radeau', 'submersible', 'barge', 'péniche', 'yacht', 'sous-marin', 'bord', 'cargo', 'vedette', 'voilier', 'engin', 'bac', 'chaland', 'transporteur', 'fusée', 'flacon', 'dirigeable', 'navigation', 'transbordeur', 'récipient', 'steamer', 'buée', 'tanker', 'navigation de plaisance', 'cliché', 'rafiot', 'fumée', 'banal', 'commun', 'vulgaire', 'ringard', 'bébête']
```
### Obtenir la définition d'un mot
On utilise la fonction `define()`


**⚠️Cette fonction ne marche pas bien, si vous savez comment la faire marcher, merci d'[ouvrir une pull request sur github](https://github.com/PetitPotiron/python-reverso/pulls). ⚠️**

### Obtenir la prononciation d'un mot
Pour obtenir la prononciation d'un mot, on a la fonction `speak_to_mp3()` du client reverso :
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> client.speak_to_mp3("fr", "Ceci est un texte de démonstration.")
```
client.speak_to_mp3(language, text)
- languague : str, doit être dans [les langues supportées](#langues-supportées)
- text : str


Ce qui donne [ce type de prononciation](voice.mp3)


### Langues supportées
**Pour utiliser ces langues, il faut utiliser leurs abréviations :**
- Allemand = "de"
- Anglais = "en"
- Arabe = "ar"
- Chinois = "ch"
- Espagnol = "es"
- Français = "fr"
- Hébreu = "hb"
- Italien = "it"
- Japonais = "jp"
- Néerlandais = "nl"
- Polonais = "pl"
- Portuguais = "pr"
- Roumain = "ro"
- Russe = "ru"
- Turc = "tu"
