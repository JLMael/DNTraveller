Le programme analyse le nom des fenêtres lancées afin de reconnaître le jeu. 
Lorsque le script détecte un nouveau message dans le presse-papiers (CTRL+C) contenant "/travel", 
il analyse les coordonnées qui suivent et réécrit le tout sur la fenêtre de jeu 
(ESPACE, /travel, coordonnées, ENTREE, ENTREE), en la mettant au premier plan.

* Il ne peut pas renvoyer les mêmes coordonnées 2 fois de suite.
* Les MAJUSCULES ne doivent pas être activées.
* Dofus doit être ouvert au démarrage.
* L'autopilotage doit être actif.


Installez les dépendances et utilisez Python 3.7 ou +

pip install -r requirements.txt
