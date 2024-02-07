# LoveLetters

## Description : 

Nous avons essayé de recréer ici le on ne peut plus fameux jeu "Love Letter", qui se joue entre 2 et 6 joueurs.
L'interface graphique fournie utilise des images de cartes différentes de celle du jeu original car ces dernières étaient introuvables en bonne qualité.

## Règles du jeu : 

Dans ce jeu, les cartes comprennent un rôle et une valeur allant de 1 à 9.
Les joueurs ont tous un rôle qu'ils gardent secret.

### Comment gagner :

Être le dernier joueur non éliminé OU Avoir la carte de plus haute valeur lorsque la pioche est vide. 

### Déroulé : 

Chaque joueur se voit distribuer une carte. Le moins bon programmeur peut alors commencer et prendre une carte dans la pioche.
Il doit alors choisir quelle carte jouer : c'est à dire quelle carte révéler et quel pouvoir associé activer. 
Après avoir effectué les actions du pouvoir activé, les joueurs suivant réitèrent les mêmes actions jusqu'à ce qu'une des conditions de victoire soit remplie.

Les valeurs et pouvoirs sont associés aux rôles comme suit : 

- (1) Garde  : Nommez une carte non-Garde et choisissez un joueur. Si ce joueur a la carte nommée, il est éliminé.
- (2) Prêtre : Consultez la main d'un autre joueur.
- (3) Baron : Vous et un autre joueur comparez secrètement votre main. Le joueur avec la valeur la plus faible est éliminé.
- (4) Servante : Jusqu'à votre prochain tour, ignorez tous les effets des cartes jouées par les autres joueurs.
- (5) Prince : Choisissez un joueur (ce peut être vous). Il défausse sa main et pioche une nouvelle carte.
- (6) Roi : Echanger votre main avec celle du joueur de votre choix.
- (7) Comtesse : Si vous avez cette carte-ci et le Roi ou un Prince, vous devez défausser la Comtesse.
- (8) Princesse : Si vous défausser cette carte, vous êtes éliminé.


## Comment jouer à la version numérique : 

On précise que cette version n'est malheuresment disponible que pour exactement 4 joueurs.
Une fois la partie lancée et que les clients sont présents, l'état de la table s'affiche pour chaque client :  



Ils ont donc accès à leur(s) cartes mais pas à celles des autres. Lorsqu'un joueur joue une carte avec un pouvoir faisant intervenir les autres joueurs et (éventuellement) les rôles de ces derniers, il doit cliquer (sans ordre précis) sur le joueur ciblé et (si nécessaire) sur le rôle qu'il choisit parmis les rôles affichés en bas de l'écran.
Une fois un joueur éliminé, une carte spéciale s'affiche sur son emplacement  : 


Non n'avons malheuresement pas réussi à incorporer les conditions de victoires, et c'est aux participants de constater que la partie est finie lorsqu'un joueur seulement n'a pas la carte ci-dessus affichée sur son emplacement.









Après avoir choisi à combien de joueurs jouer, un écran récapitulatif s'affiche afin de garder le fil de qui est éliminé et avec quelle carte  : 

#A METTRE A JOUR
![image](https://github.com/Ninoyncrea/LoveLetters/assets/136315916/3831ccaa-73c8-474b-97a0-5ef8e7096409)


Pour qu'un joueur joue, il faut cliquer sur le bouton bleu, ici "à J3 de jouer".
La main (rôle + pioche) du joueur en question s'affiche alors : il lui suffit alors de cliquer sur la carte qu'il veut jouer.
Selon le pouvoir activé, différentes fenêtres peuvent apparaître (choix du joueur visé puis du rôle à deviner pour le garde, choix du joueur dont on veut connaître la carte pour le prêtre ect) : pour agir sur ces fenêtres (c'est à dire celles qui ne sont pas un choix de carte à jouer ou "à Ji de jouer") il faut utiliser les flèches du clavier pour naviguer entre les différents choix et les confirmer avec ENTER.
Comme pour la version physique, le jeu continue ainsi tant qu'une des conditions de victoire n'aura pas été remplie. Une fenêtre spécifique s'affichera alors.


