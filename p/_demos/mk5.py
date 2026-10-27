# Mardi 27/10 : niche restaurant, 7 prospects avec e-mail public (envoi auto 9h).
import json
from mk3 import R, C
C.clear()
R('457508547800','le-fer-rouge','Le Fer Rouge','Fer Rouge','Colmar','68000','52 Grand Rue','03 89 20 80 69','Restaurant · Grand Rue, Colmar',
  "Une table connue de Colmar, notée 4,2 sur 5 par près de 5 000 clients sur Google. Ouvert 7 jours sur 7. Réservez votre table en deux gestes.",
  'La cuisine alsacienne, <em>au cœur de Colmar.</em>','Quelques <em>spécialités</em>',[('Choucroute Fer Rouge','Plat'),('Suprême de poulet, sauce Colmar au foie gras','Plat'),('Entrecôte Black Angus','Plat')],
  ['Grand Rue','Colmar','7 jours sur 7','Réservez en ligne'],'Une table <em>à Colmar.</em>','4,2 / 5 · 4 953 avis',note='Plats relevés sur votre site actuel. Sur le vrai site : votre carte complète et à jour.')
R('457486949606','chez-madar-joon','Chez Madar Joon','Madar Joon','Saint-Louis','68300','5 rue des Jardins','03 89 67 10 88','Cuisine afghane · Saint-Louis',
  "La cuisine afghane à Saint-Louis, notée 4,6 sur 5 par plus de 500 clients sur Google. Réservez votre table en deux gestes.",
  'La cuisine <em>afghane</em>, faite maison.','Les <em>spécialités</em>',[('Mantow','Plat'),('Ashak','Plat'),('Baghali Palaw','Plat'),('Souris d\'agneau','Plat'),('Nans','Accompagnement')],
  ['Cuisine afghane','Rue des Jardins','Saint-Louis','Réservez en ligne'],'Une table <em>à Saint-Louis.</em>','4,6 / 5 · 533 avis',note='Plats relevés sur votre page actuelle. Sur le vrai site : votre carte complète et à jour.')
R('457476157627','le-bratzala','Le Bratzala','Bratzala','Guebwiller','68500',"32 rue de l'Église",'03 89 28 60 78',"Restaurant · rue de l'Église, Guebwiller",
  "Une adresse appréciée à Guebwiller, notée 4,4 sur 5 par près de 500 clients sur Google. Réservez votre table en deux gestes.",
  'Une table de Guebwiller, <em>notée 4,4</em> par ses clients.','À la <em>carte</em>',[('Le plat du jour','Midi'),('Les plats de la carte','Plats'),('Les desserts','Dessert')],
  ["Rue de l'Église",'Guebwiller','Restaurant','Réservez en ligne'],'Une table <em>à Guebwiller.</em>','4,4 / 5 · 489 avis')
R('458013708518','pazza-idea','Pazza Idea','Pazza Idea','Guebwiller','68500','18 rue du Maréchal Joffre','03 89 37 89 29','Ristorante italiano · Guebwiller',
  "La cuisine italienne à Guebwiller, notée 4,6 sur 5 par plus de 550 clients sur Google. Réservez votre table en deux gestes.",
  'La cuisine <em>italienne</em>, à Guebwiller.','La <em>carta</em>',[('Antipasti','Entrée'),('Pâtes','Plat'),('Dolci','Dessert')],
  ['Ristorante italiano','Rue du Maréchal Joffre','Guebwiller','Réservez en ligne'],'Une table <em>italienne.</em>','4,6 / 5 · 565 avis')
R('458011921616','le-poincare','Le Poincaré','Poincaré','Cernay','68700','44 rue Raymond Poincaré','09 84 04 05 96','Burgers, brunch, halal · Cernay',
  "Burgers, brunch et desserts à Cernay, notés 4,4 sur 5 par plus de 300 clients sur Google. Ouvert tous les jours. Réservez votre table en deux gestes.",
  'Les burgers <em>et le brunch</em>, à Cernay.','Au <em>menu</em>',[('Burgers','Plat'),('Brunch','Week-end'),('Desserts','Dessert')],
  ['Burgers','Brunch','Halal','Cernay'],'Une adresse <em>à Cernay.</em>','4,4 / 5 · 302 avis',note='Catégories relevées sur votre page actuelle. Sur le vrai site : votre carte complète et à jour.')
R('457465348297','la-piazzetta','La Piazzetta','Piazzetta','Huningue','68330','16 rue du Maréchal Foch','03 68 06 60 16','Pizzeria · Huningue',
  "Pizzas et cuisine italienne à Huningue, notées 4,3 sur 5 par plus de 400 clients sur Google. Réservez votre table en deux gestes.",
  'Les pizzas, <em>à Huningue.</em>','La <em>carta</em>',[('Pizzas','Pizza'),('Pâtes','Plat'),('Dolci','Dessert')],
  ['Pizzeria','Rue du Maréchal Foch','Huningue','Réservez en ligne'],'Une table <em>italienne.</em>','4,3 / 5 · 438 avis')
R('457669578992','le-meridien','Le Meridien','Meridien','Guebwiller','68500','140 rue de la République','03 89 26 18 95','Cuisine marocaine · Guebwiller',
  "La cuisine marocaine à Guebwiller, notée 4,8 sur 5 par plus de 450 clients sur Google. Réservez votre table en deux gestes.",
  'Les tajines <em>et le couscous</em>, comme là-bas.','Les <em>spécialités</em>',[("Tajine d'agneau aux pruneaux et amandes",'Plat'),('Tajine de poulet aux olives et citrons','Plat'),('Couscous','Plat'),('Grillades','Plat')],
  ['Cuisine marocaine','Rue de la République','Guebwiller','Réservez en ligne'],'Une table <em>à Guebwiller.</em>','4,8 / 5 · 463 avis',note='Plats relevés sur votre page actuelle. Sur le vrai site : votre carte complète et à jour.')
for c in C: json.dump(c,open(c['slug']+'.json','w'),ensure_ascii=False)
print(' '.join(c['slug']+'.json' for c in C))
