L'objectif de ce TP est l'implémentation de [l'algorithme du jour du jugement dernier de John Conway](https://fr.wikipedia.org/wiki/Algorithme_du_jour_du_Jugement_dernier).

Seules les dates à partir de l'année 1583 (première année complète du calendrier grégorien) seront prises en charge.

## Saisie de la date

La première partie du projet consiste à demander une date au format `YYYY-MM-dd` et à définir si elle est valide ou non. La récupération de cet input se fera dans le fichier principal `doomsday.py`.

Puis vous devrez vérifier :

- Que l'input suit correctement le format "YYYY-MM-dd"
- Que la date est postérieure à 1583 et existe

Lorsque l'utilisateur commet une erreur de saisie, vous devez lui expliquer laquelle.

Pour simplifier les tests, votre fonction de validation devra se trouver dans le fichier `doomsday/date.py` et se nommer `is_valid_date()`.

Bien sûr, il est possible (et recommandé) d'utiliser des sous-fonctions.

### Comment tester ?

Pour être considéré comme valide, votre algorithme doit passer une série de tests.

Pour tester, exécutez le fichier `test-date.py`.

**Attention** : tous les cas de figure ne sont pas testés. Votre code peut passer le test, mais certains bugs peuvent rester cachés...

## Calcul du jour

Dans un second temps, utilisez l'algorithme du jour du jugement dernier pour déterminer le jour en fonction de la date.

Pour simplifier les tests, votre fonction de calcul devra se trouver dans le fichier `doomsday/algorithm.py` et se nommer `get_day_for_date()`

### Comment tester ?

Comme pour la date, mais avec le fichier `test-algorithm.py`

## Pour rendre ce TP

Merci de faire une Pull Request vers ce repository.

Le nom de la PR doit contenir votre nom et celui de votre collègue si vous êtes en binôme.

Vérifiez que votre code est conforme aux normes pep8 et aux autres critères de qualité dont nous avons parlé.
