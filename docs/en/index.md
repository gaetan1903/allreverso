# Documentation du module python `allreverso`
[<img src="../python_allreverso.png" width="50" alt="allreverso's logo">](https://petitpotiron.github.io/python-reverso/fr/)


[![discord server widget](https://discord.com/api/guilds/831480772455038996/embed.png)](https://discord.gg/v4yfnjWKvy)
[![allreverso's version](https://img.shields.io/pypi/v/allreverso.svg)](https://pypi.org/project/allreverso/)
[![supported python versions](https://img.shields.io/pypi/pyversions/allreverso.svg)](https://pypi.org/project/allreverso/)
## Installation
To access the services offered by this awesome package, you need to install it!

There are several ways to install this super module:
**Python 3.5 or upper is required**
 ```
 # Linux / macOS
 python3 -m pip install -U allreverso
 # Windows
 python -m pip install -U allreverso
 ```

# The beginning
Here is the base of the module, wich is necessary each time you use allreverso.
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
```

# Different functions
### Traduction
To translate a text, use the `translate()` method from the reverso client:
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> client.translate("en", "fr", "Hello!")
['bonjour !']
```
client.translate(source, cible, text)
- source : str, must be in [the supported languages](#langues-supportées)
- target : str, must be in [the supported languages](#langues-supportées)
- text : str
### Text correction
To translate a text, use the `correct()` method from the reverso client:


**⚠️ This method only works with `fr` and `en` values for the `language` parameter. ⚠️**
```python
>>> import allreverso
>>> client = allreverso.ReversoClient()
Reverso Client successfully created !
>>> c.correct("en", "Helo")
'Hello'
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
