Récupération de l'image
=======================
https://www.raspberrypi.org/downloads/raspbian/

Initialisation
==============
Copie de la clef SSH publique sur le raspberry
----------------------------------------------
    $ ssh-copy-id pi@10.27.0.242

Exécuter le playbook
--------------------
	$ ansible-playbook  -i inventory playbook.yml