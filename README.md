
<!-- PROJECT LOGO -->

<a href="https://ibb.co/ZG6N78x"><img src="https://i.ibb.co/ydnV7yq/images.png" alt="images" border="0"></a>

  <h3 align="center">Script de stabilité</h3>

  <p align="center">
    Un script permetant de veiller sur vos programmeS
    <br />
    



<!-- Sommaire -->
## Sommaire du Readme

* [A propos du projet](#a-propos-du-projet)
  * [Conçu avec](#conçu-avec)
* [Pour commmencer](#Pour-commmencer)
  * [Prérequis](#Prérequis)
  * [Installation](#installation)
* [Utilisation](#Utilisation)
* [Roadmap](#roadmap)
* [Contribution](#contribution)
* [Licence](#Licence)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- A propos du projet -->
## A propos du projet


Ce projet est né de ma volonté de faciliter mon quotidien. Dans le cadre de maintenance d'automates qui encodent des carte magnétique/RFID, il m'arrive d'effectuer quotidiennement des tâches redondantes. Le parc d'automates que je maintiens avec mon équipe s'élève à 3000 machines basées chez nos divers clients, 20% de ces machines dispose d'un logiciel d'encodage nommé vision. Celui-ci est installé par la société Assabloy, dont il est elle est conceptrice.

<!-- capture ici de l'interface vision -->
Vision tourne comme un programme.Exe, mais dispose aussi de certaines dépendence qui tournent comme services Windows. Il arrive très fréquemment que ce programme et ses services arrêtent de fonctionner.
L'instabilité est liée à l'obsolescence du logiciel, en effet l'upgrade vers une version plus sable dépend de nos clients, car cette dernière a un coût.
<!-- capture ici de l'interface services -->

L'objectif de ce projet est d'automatiser la détection, et effectuer proprement le redémarrage de ces programmes afin que notre machine puisse continuer à fonctionner.
En effet, quand ce programme ne fonctionne plus, le client ne peut plus utiliser sa machine et perd de l'argent. Il en suit une maintenance par mon équipe.

Ce script pourra à terme nous apporter un gain de temps statistiquement un agent passe à peu pres, et les mainteneurs pourront se consacrer à d'autres tâches et cela augmentera également la satisfaction des clients, car meilleur stabilité de notre Automate.

Apres une estimation, la moyenne de temps passé par un technicien sur ce probleme est 15 minutes :

-la prise du ticket sur salesforce

-la comprension de la demande

-la prise de main sur le system

-l'exploitation des logs afin de dyagnostiquer le probleme

-la resolution

-la communication avec le client et la cloture 



### conçu avec
Le scrypt/programme a été concu dans le language Python avec l'aide de l'IDE Pycharm.
* [Python](https://www.python.org/)
* [Pycharm](https://www.jetbrains.com/fr-fr/pycharm/promo/?gclid=EAIaIQobChMIsY6M37_V6wIVBqp3Ch3DJA6XEAAYASAAEgIrwfD_BwE)




<!-- GETTING STARTED -->
## Pour commmencer 

Voici des instructions simples pour que vous puissiez vous aussi utiliser ce script et l'adapter à votre infrastucture.


### Prérequis

Voici une liste des prérequis afin d'utiliser ce scrypt et le programme en .exe .

Vous devez disposer d'un system sous windows
Disposer d'un compte administrateur 


Les scripts ont été développés et testés dans l'environnement ci-dessous :


Python version 3.8
Postes clients Windows 10
Postes clients Windows 7


### Installation





<!-- USAGE EXAMPLES -->
## Utilisation

Parler ici de windows planificateur de taches / CRON sous linux des opportunités.

Les variables énoncées ci-dessous seront à modifier dans le script selon votre system et besoin. Si une variable n'est pas dans la liste suivante, le script est ponctué par des commentaires afin d'en éclairer le fonctionnement et rappeler les contenus attendus pour les variables.




<!-- CONTRIBUTING -->
## Contribution

Plusieurs axes d'amélioration sont possibles:
Notamment l'ajoute d'une fonction qui envoie une notification par alerte mail quand le script est pas en mesure d'effectuer sa tache. 
Possibilité d'exporter les logs automatiquement apres un delai de un mois sur des serveurs FTP.





<!-- LICENCE -->
## Licence

Parler ici de la licence Github



<!-- CONTACT -->
## Contact

Noor khan nk@emailfactice.fr

Project Link: [https://github.com/azura1003/Nkhan_P6_Python](https://github.com/azura1003/Nkhan_P6_Python)









