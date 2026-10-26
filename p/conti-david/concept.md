# Conti David : fiche concept (26/10/2026)

- Prospect : Conti David, sanitaire, chauffage et plomberie, 34 avenue de Riedisheim, 68100 Mulhouse. Téléphone 03 89 64 44 96. HubSpot 457124141244.
- Faits publics utilisés :
  - « Créée depuis 14 ans » ;
  - services : chauffage (vente et installation), installation de sanitaires, plomberie, rénovation immobilière ;
  - slogan « L'énergie est notre avenir, économisons-la ! » ;
  - phrase « Un travail propre, sérieux, de qualité et dans le respect des délais ».
- Constat sur le site actuel : copyright « @2019 » (Solocal), et la section « Notre entreprise » contient encore « Lorem ipsum ».

## Direction artistique : « le plan d'installation »
Le site se présente comme un plan technique. Il montre un artisan précis, qui réfléchit avant de percer.

- Palette :
  - bleu plan #0f2a44 ;
  - papier calque #eef1f0 ;
  - trait cyan #6fd3ff ;
  - cuivre #c8743c (rappel des tuyaux) ;
  - blanc.
- Polices : Barlow Condensed (titres, très techniques), IBM Plex Mono (annotations, cotes, cartouche).

## Structure
1. Héros : grille de plan et schéma isométrique SVG d'une installation (chaudière, radiateur, douche, lavabo). Le schéma se trace au chargement, puis des gouttes circulent dans les tuyaux. Les repères A, B, C et D apparaissent.
2. Cartouche : bloc de titre façon plan d'architecte, avec entreprise, ancienneté et adresse.
3. Quatre « planches » de services. Chaque pictogramme se dessine quand la planche entre à l'écran.
4. Le slogan : les mots s'allument pendant qu'un tuyau se remplit au défilement.
5. L'atelier : photo virée au bleu plan, avec des cotes autour.
6. Engagements : quatre tampons « OK » qui s'impriment.
7. Devis en bon de commande, en 3 étapes, avec un ticket récapitulatif.
8. Zone : cercles concentriques autour de Mulhouse.
9. Pied de page avec le cartouche complet.

## Motion
- Tracés `stroke-dashoffset` animés avec GSAP.
- Gouttes qui suivent les tuyaux grâce à `getPointAtLength`.
- ScrollTrigger pour les déclenchements, Lenis pour le défilement doux.
- Tampons animés avec un écrasement en scale et rotation.
- Bascule des chiffres de la cote.
- Avec les animations réduites : tout est déjà dessiné et rien ne circule.

## Différences avec les 5 dernières maquettes
Pas de photo en héros, c'est un schéma. Aucune police déjà utilisée. Palette bleu plan et cuivre. L'ordre des sections est nouveau : cartouche, puis planches, puis tampons.
