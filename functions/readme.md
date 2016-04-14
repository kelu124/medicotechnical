# [FCT-sensing]()
![](viewme.jpg)

## Title
Sensing

## Description
Émission, réception de l’onde acoustique & gestion des tirs (dirac).
Conversion d’une pression p en une tension V.


---


# [FCT-sensing_emitting]()
![](viewme.jpg)

## Title
Emitting

## Description
Envoi du pulse de pression + initialisation (t0) (pour synchro) après réception d’un pulse de tension (envoie dirac qui indique t0 ie le début soit le plus proche + angle) +Alimentation energétique

## Main function
[FCT-sensing](../FCT-sensing)

---


# [FCT-sensing_receiving]()
![](viewme.jpg)

## Title
Receiving

## Description
Capter le signal de pression puis le convertir en tension + (TR switch?)

## Main function
[FCT-sensing](../FCT-sensing)

---


# [FCT-sensing_sweeping]()
![](viewme.jpg)

## Title
Sweeping

## Description
Réglage du pulse selon le bon angle

## Main function
[FCT-sensing](../FCT-sensing)

---

# [FCT-signal_processing]()
![](viewme.jpg)

## Title
Signal processing

## Description
Amplification(TGC), filtrage passe bas pour enlever le bruit (analogique) haute fréquence, conversion numérique, détection d’enveloppe, calcul des pixels

---

# [FCT-signal_processing_amplifying_time_gain_compensation]()
![](viewme.jpg)

## Title
Amplifying time gain compensation

## Description
amplification inversement exponentielle à la pronfondeur

## Main function
[FCT-signal_processing](../FCT-signal_processing)

---

# [FCT-signal_processing_filtering]()
![](viewme.jpg)

## Title
Filtering

## Description
Filtrage passe bas pour améliorer le ratio signal/bruit grace à une rampe fonction de la distance + eviter les trucs abérents

## Main function
[FCT-signal_processing](../FCT-signal_processing)

---

# [FCT-signal_processing_envelop_detecting]()
![](viewme.jpg)

## Title
Detecting

## Description
Obtenir l’energie du signal (sa forme)

## Main function
[FCT-signal_processing](../FCT-signal_processing)

---

# [FCT-signal_processing_calculating_pixels]()
![](viewme.jpg)

## Title
Calculating pixels

## Description
Obtenir une liste de pixels

## Main function
[FCT-signal_processing](../FCT-signal_processing)

---

# [FCT-user_interfacing]()
![](viewme.jpg)

## Title
User interface

## Description
Affichage de l’image en temps réel, et interface utilisateur (GUI) 

---

# [FCT-user_interfacing_displaying]()
![](viewme.jpg)

## Title
Displaying

## Description
Afficher l’image.

## Main function
[FCT-user_interfacing](../FCT-user_interfacing)

---

# [FCT-user_interfacing_setting]()
![](viewme.jpg)

## Title
Setting

## Description
L’opérateur règle les paramètres.

## Main function
[FCT-user_interfacing](../FCT-user_interfacing)

---

# [FCT-user_interfacing_image_processing]()
![](viewme.jpg)

## Title
Image processing

## Description
Formation de l’image en 2D à partir d’une suite de pixels 1D et traitement sur l’image : compensation
de perte saturation , zoom, selction et calcul de distance sur une image fixe , données image
(enregistrement + export), tir TM (affiche une ligne au cours du temps ).

## Main function
[FCT-user_interfacing](../FCT-user_interfacing)

---
