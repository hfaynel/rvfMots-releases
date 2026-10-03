# Dictionnaire de rvfMots : la part tirée de Morphalou

Le dictionnaire du jeu réunit le lexique Grammalecte et une part de
Morphalou 3.1, lexique morphologique ouvert du français maintenu par
l'ATILF (CNRS, Université de Lorraine), distribué sous la licence LGPL-LR
(Lesser General Public License For Linguistic Resources).

Comme cette licence le demande, voici la liste tirée de Morphalou que le jeu
utilise, et de quoi la refaire :

- `morphalou.txt` : les formes fléchies retenues, une par ligne ;
- `import_morphalou.py` : le script qui la produit à partir du fichier
  `Morphalou3.1_formatCSV_toutEnUn.zip`, à télécharger sur ORTOLANG :
  https://repository.ortolang.fr/api/content/morphalou/latest/ ;
- `LICENCE-morphalou.txt` : les modifications faites, et le texte de la
  licence LGPL-LR.

Ce qui est retenu : la part Morphalou 2 (vérifiée par les lexicographes de
l'ATILF), noms communs, adjectifs, verbes, adverbes, interjections et mots
grammaticaux, sans locutions, sans formes à majuscule ni mots sans voyelle.
Le jeu écrit ensuite les mots sans accents ni traits d'union.
