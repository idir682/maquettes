import json
C=[]
C.append(dict(kind='resto',id='457048254688',slug='brasserie-le-parvis',name='Brasserie Le Parvis',title='Brasserie Le Parvis · Mulhouse',tel='03 89 56 60 33',mark='Le Parvis',status='Réservation en ligne',word='Parvis',
 kicker='Brasserie · avenue du Général Leclerc, Mulhouse',cap="Une brasserie chaleureuse, des assiettes généreuses cuisinées à la minute. Réservez votre table en deux gestes.",
 mani='Des assiettes <em>généreuses</em>, cuisinées à la minute, dans un cadre chaleureux.',carte_h2='À la <em>brasserie</em>',
 plats=[('Choucroute','Plat'),('Le plat du jour','Plat'),('Options sans lactose','Sur demande')],
 carte_note='Plats cités par vos clients en ligne. Sur le vrai site : votre carte complète et à jour.',band=['Brasserie','Cuisiné à la minute','Avenue du Général Leclerc','Mulhouse'],
 salle_h2='Un cadre <em>chaleureux.</em>',salle_p="Une salle agréable, un service attentif. Sur le vrai site : vos photos, votre carte et vos horaires à jour.",
 infos=[('Adresse','40 av. du Général Leclerc'),('Téléphone','03 89 56 60 33'),('Sur Google','4,0 / 5 · 201 avis')],addr='40 avenue du Général Leclerc',google='4,0 / 5 · 201 avis'))
C.append(dict(kind='resto',id='457149479098',slug='auberge-lefebvre',name='Auberge Lefebvre',title='Auberge Lefebvre · Restaurant à Mulhouse',tel='03 89 56 48 64',mark='Auberge Lefebvre',status='Réservation en ligne',word='Lefebvre',
 kicker='Restaurant · rue Lefebvre, Mulhouse',cap="Une cuisine traditionnelle, française et orientale, au cœur de Mulhouse. Réservez votre table en deux gestes.",
 mani='La cuisine de <em>tradition</em>, française et orientale, à la même table.',carte_h2='Quelques <em>spécialités</em>',
 plats=[('Couscous royal','Plat'),('Filet de bœuf aux morilles','Plat'),('Magret de canard','Plat'),('Cordon bleu','Plat')],
 carte_note='Plats cités en ligne. Sur le vrai site : votre carte complète et à jour.',band=['Cuisine traditionnelle','Française et orientale','Rue Lefebvre','Mulhouse'],
 salle_h2='Une table <em>de quartier.</em>',salle_p="Rue Lefebvre, à Mulhouse. Sur le vrai site : vos photos, votre carte et vos horaires à jour.",
 infos=[('Adresse','82 rue Lefebvre, Mulhouse'),('Téléphone','03 89 56 48 64'),('Sur Google','4,4 / 5 · 298 avis')],addr='82 rue Lefebvre',google='4,4 / 5 · 298 avis'))
C.append(dict(kind='inst',id='457122479315',slug='beauty-smile',name='Institut Beauty Smile',logo='Beauty Smile',title='Beauty Smile · Institut de beauté à Mulhouse',tel='03 89 60 19 31',
 h1=['Le sourire,','le regard, la peau.'],h1_label='Le sourire, le regard, la peau.',kicker='Institut de beauté · boulevard de l\'Europe',
 hero_p='Blanchiment dentaire, cils, sourcils, Hydrafacial et head spa coréen. Ouvert du lundi au samedi, jusqu\'à 20 h en semaine.',
 univ_h2='Trois expertises, <em>une adresse.</em>',univ_p='Des soins précis, expliqués simplement, pour choisir le bon avant de réserver.',
 univers=[('Le sourire','Blanchiment dentaire.','Une séance d\'une heure pour un sourire plus lumineux.'),('Le regard','Cils et sourcils.','Rehaussement de cils avec teinture et soin, browlift. Tarif réduit à deux.'),('Visage et cuir chevelu','Hydrafacial et head spa.','Soin Hydrafacial, head spa coréen et hairneedling.')],
 soins=[('Blanchiment dentaire','1 h','90 €','Une séance de blanchiment.',['Sourire']),('Rehaussement de cils','1 h 30','30 €','Rehaussement, teinture et soin.',['Regard']),('Soin Hydrafacial','1 h','60 €','Le nettoyage profond du visage.',['Visage']),('Head spa découverte','35 min','70 €','Le head spa coréen, pour découvrir.',['Cuir chevelu'])],
 note='Tarifs relevés sur votre page Planity le 26/10/2026.',verre_h2='Des soins ciblés, <em>sans attendre.</em>',
 panes=[('Ouvert le lundi','Du lundi au jeudi de 10 h à 20 h, samedi jusqu\'à 17 h.'),('5,0 sur Planity','Accueil, propreté et qualité notés 5 sur 5 (168 avis).'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
 slots=['10 h 00','11 h 30','14 h 00','15 h 30','17 h 00','18 h 30'],gift='70 €',gift_soin='Head spa',ft_big='Prenez soin de vous, <em>avec le sourire.</em>',
 addr='16 boulevard de l\'Europe',hours='Lun – jeu, 10 h – 20 h<br>Ven, 10 h – 12 h, 14 h – 20 h<br>Sam, 10 h – 17 h',avis='5,0 / 5 sur Planity'))
C.append(dict(kind='inst',id='457003889909',slug='paolina-beaute',name='Paolina beauté',logo='Paolina beauté',title='Paolina beauté · Ongles et cils à Mulhouse',tel='06 71 63 66 95',
 h1=['Ongles, cils,','tout en rose.'],h1_label='Ongles, cils, tout en rose.',kicker='Salon de beauté · rue de Bâle, Mulhouse',
 hero_p='Un salon girly et chaleureux, une équipe de trois : Perrine et Camille pour les ongles, Kaoutar pour les cils. Ouvert dès 8 h 30.',
 univ_h2='Trois spécialistes, <em>un salon.</em>',univ_p='Chaque prestation est faite par la spécialiste du domaine.',
 univers=[('Les ongles','Gel, capsules, semi-permanent.','Pose sur ongles naturels, rallongement Gel X ou demi-capsule, semi-permanent mains et pieds.'),('Les cils','Le regard.','Kaoutar s\'occupe des cils.'),('Visage et épilation','Soins et épilations.','Soin hydratant, soin anti-âge et épilations.')],
 soins=[('Première pose de gel','1 h 15','43 €','Pose de gel sur ongles naturels.',['Ongles']),('Manucure simple','40 min','25 €','La manucure classique.',['Mains']),('Soin anti-âge visage','1 h','69 €','Un soin complet du visage.',['Visage']),('Épilation des sourcils','15 min','8 €','La ligne des sourcils.',['Épilation'])],
 note='Tarifs relevés sur votre page Planity le 26/10/2026.',verre_h2='Un salon <em>où l\'on se sent bien.</em>',
 panes=[('Ouvert dès 8 h 30','Du lundi au vendredi jusqu\'à 19 h, le samedi matin.'),('Une équipe de trois','Deux prothésistes ongulaires et une spécialiste des cils.'),('4,9 sur Planity','Sur 169 avis.')],
 slots=['8 h 30','10 h 00','11 h 30','14 h 00','15 h 30','17 h 00'],gift='43 €',gift_soin='Pose de gel',ft_big='Prenez soin de vous, <em>tout en douceur.</em>',
 addr='111 rue de Bâle',hours='Lun – ven, 8 h 30 – 19 h<br>Samedi, 9 h – 13 h',avis='4,9 / 5 sur Planity'))
for c in C: json.dump(c,open(c['slug']+'.json','w'),ensure_ascii=False)
