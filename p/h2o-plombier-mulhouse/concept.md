# H2O Plombier Chauffagiste Mulhouse : fiche concept (26/10/2026)

- Prospect : H2O, 14 rue de Hirsingue, 68200 Mulhouse. Téléphone 03 89 43 37 98. HubSpot 456817924335.
- Faits publics, relevés sur l'accueil du site actuel :
  - « Plus de 20 ans au service de votre confort » ;
  - certifications et partenaires : Qualibat RGE, Professionnel du gaz, Handibat, Silverbat, Station Technique Agréée Vaillant ;
  - services : salle de bain, chauffage (chaudières, pompes à chaleur), climatisation (mono-split, multi-split, gainable), dépannage plomberie et chauffage, entretien annuel des chaudières gaz ;
  - zone : Mulhouse, Colmar, Saint-Louis, Rixheim, Kingersheim, Illzach, Wittenheim, Brunstatt-Didenheim, Riedisheim, Pfastatt, Lutterbach, Sausheim, Baldersheim, Morschwiller-le-Bas.
- Aucun défaut du site actuel n'est affirmé. Angle retenu : mettre en avant les certifications dès le premier écran.

## Direction artistique : « le niveau d'eau »
L'eau devient le motif d'interface : surfaces qui ondulent, niveaux qui montent, courant qui emporte les noms des communes.

- Palette :
  - bleu canard profond #06343a ;
  - eau #57d6cf ;
  - écume #e8f4f2 ;
  - sable #f3eee6 ;
  - laiton #d9a441 pour les labels.
- Polices : Unbounded (titres larges et ronds), Inter Tight (texte).

## Structure
1. Héros : surface d'eau simulée en canvas. Une vraie simulation d'ondes réagit au doigt et à la souris, avec des gouttes de temps en temps. « H2O » en très grand, rempli par une vague qui monte.
2. Bandeau de labels qui défile (RGE, Vaillant, gaz, Handibat, Silverbat).
3. Cinq services présentés en « colonnes d'eau » : le niveau monte au survol (ordinateur) ou au défilement (mobile).
4. Outil « prochain entretien » : on choisit le mois du dernier entretien et la page calcule l'échéance des 12 mois.
5. Urgence : bande de couleur avec une goutte qui tombe et le numéro.
6. Zone : deux rangées de communes qui défilent en sens contraire, comme un courant.
7. Contact et pied de page.

## Motion
- Simulation d'ondes en canvas 2D (deux tampons de hauteur, avec amortissement), mise en pause hors écran.
- Vague SVG animée dans le titre.
- GSAP ScrollTrigger et Lenis.
- Niveaux en `clip-path`.
- Avec les animations réduites : surface fixe, titre plein, défilants arrêtés.

## Différences avec les maquettes précédentes
Héros sans photo, interactif et physique, différent du shader nacre. Polices jamais utilisées. Palette bleu canard. Sections nouvelles : colonnes d'eau, calculateur d'entretien, courant des communes.
