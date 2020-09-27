
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
  * [Configuration](#Configuration)
* [Utilisation](#Utilisation)
* [Contribution](#contribution)
* [Licence](#Licence)
* [Contact](#contact)




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


### Configuration

Pour qu'on puisse utiliser le script avec le format natif de python, la premiere chose à faire est d'installer Python. En effet contrairement à Mac et Linux, il est necessaire d'installer python sous windows.

1) Rendez-vous sur le site de Python. En vous rendant à l'adresse python.org/downloads, vous allez pouvoir télécharger votre version de Python. Le site détectera que vous êtes sous Windows et la version que vous utilisez : il affichera alors l'installateur Windows approprié.
2) Exécutez l'installateur une fois le téléchargement terminé. Cliquez sur le bouton de la version voulue et le téléchargement de l'installateur commencera. 
3) Cochez la case Add Python 3.5 to PATH. Ainsi, vous pourrez exécuter Python directement depuis l'invite de commandes.

Vous etes à présent en mesure de lancer le script depuis l'interpreteur CMD de windows.


Le script est pratiquement délivré clé en main, vous devez simplement personnaliser les variables avec les de services que vous souhaitez, selon votre besoin.

Choissiez le service que vous voulez superviser prenons pour notre démonstration le gestionnaire audio de windows. 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/JmwMVKT/Capture.png" alt="Capture" border="0"></a>

Pour l'ajouter il vous suffit de déterminer son nom de service, dans notre cas il se nomme "Audiosrv".

<a href="https://ibb.co/Jr2HWKn"><img src="https://i.ibb.co/MPp7ysn/Services.png" alt="Services" border="0"></a>

Vous devez reneigner ce nom à la ligne 7 du script Script_vision.py <a href="https://imgbb.com/"><img src="https://i.ibb.co/m5bZY69/Ligne-7.png" alt="Ligne-7" border="0"></a>




<!-- USAGE EXAMPLES -->
## Utilisation

Vous pouvez utiliser le script de plusieurs manieres, la premiere l'executer comme script simple depuis l'invite de commande quand vous le souhaitez.
 <a href="https://ibb.co/Dt1P55F"><img src="https://i.ibb.co/mGRr66K/Commande.png" alt="Commande" border="0"></a>



Deuxieme utilisation possible celle qui nous motive à réaliser ce projet : l'automatisation de la tache.

Pour ce faire nous allons utiliser l'outil windows planificateur de tache, afin de lancer le script à intervalles réguliers.

Néanmoins, nous ne pouvons pas ajouter le script tel quel il est préferable de compiler un exectuable.

La première étape consiste à télécharger la dépendance python qui va convertir le script en exécutable :


<a href="https://ibb.co/yX5K4nm"><img src="https://i.ibb.co/JK283RW/Pip-pyinstaller.png" alt="Pip-pyinstaller" border="0"></a>

Tapez la commande pip install pyinstaller --onefile 

Le "one file" est utile quand vous voulez qu'un seul fichier à la sortie.

Une fois terminé, vous vous retrouvez avec votre executable.

<a href="https://ibb.co/PgXGYKS"><img src="https://i.ibb.co/zZ9V5pk/exe.png" alt="exe" border="0"></a>

L'avantage, c'est qu'il n'est pas necessaire d'avoir python installer ainsi sa compatibilité aux divers environnements est améoliré. 


Maintenant que nous avons un executable fraichement créer, nous pouvons créer une tache dans l'outil windows "planificateur de tache".
Je vous ai facilité la "tache" :) . Plutot que de créer une tache de maniere longue et fastidieuse, je vous ai mis à disposition dans le répertoire projet le fichier services visions reboot.xml. Ce fichier est le template de la tache que j'ai créer pour mon projet, les commentaires dans le fichier xml vous indiquent les balises à modifier afin de personnaliser votre tache.

Une fois que vous avez ajuster le XML selon votre besoin, nous pouvons le charger dans le planificateur.
Il vous suffit d'ouvrir une invite de commande en administrateur et de taper la commande suivante et appuyez sur Entrer:


schtasks /create /xml "%UserProfile%\CHEMIN-JUSQUAU-FICHIER\NOM-DE-VOTRE-FICHIER.xml" /tn "\NOM-DOSSIER-PLANIFICATEUR\NOM-TACHE-SUR-PLANIFICATEUR" /ru "NOM-PC\NOM-UTILISATEUR"


Dans la commande, n'oubliez pas de modifier ("%UserProfile%\CHEMIN-JUSQUAU-FICHIER\NOM-DE-VOTRE-FICHIER.xml"," "\NOM-DOSSIER-PLANIFICATEUR\NOM-TACHE-SUR-PLANIFICATEUR" "NOM-PC\NOM-UTILISATEUR") avec vos informations locales.

Petite astuce: Si la commande echoue ou vous ne voulez pas tapez le mot de passe manuellement (script auto), modifiez /rp COMPTE-MDP (remplacant "COMPTE-MDP" par votre mot de passe actuel).

Resultat

<a href="https://ibb.co/74k57Tx"><img src="https://i.ibb.co/rsdSnLK/Capture.png" alt="Capture" border="0"></a>

Allons voir dans le planificateur de tache  : 

<a href="https://ibb.co/1vJ07gs"><img src="https://i.ibb.co/4mgFKqs/Capture-2.png" alt="Capture-2" border="0"></a>


La tache est bien présente et elle s'excutera automatiquement toutes les 5 minutes et va démarrer à 20h.




<!-- CONTRIBUTING -->
## Contribution

Plusieurs axes d'amélioration sont possibles:
notamment l'ajoute d'une fonction qui envoie une notification par alerte mail quand le script n'est pas en mesure d'effectuer sa tâche. 
Possibilité d'exporter les logs automatiquement après un délai d'un mois sur des serveurs FTP.

Automatisation avec CRON pour linux


<!-- LICENCE -->
## Licence

Le projet régit de la licence MIT.



Version précédente Version 1.0
Voir changelog.md


<!-- CONTACT -->
## Contact

Noor khan noorkhan.95150@gmail.com

Project Link: [https://github.com/azura1003/Nkhan_P6_Python](https://github.com/azura1003/Nkhan_P6_Python)









