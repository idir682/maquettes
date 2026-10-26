# Tournée du mardi 27/10 : 10 prospects des alentours (Brunstatt, Riedisheim, Rixheim).
import json
C=[]
NOTE_C='Exemples de plats. Sur le vrai site : votre carte complète et à jour.'
def R(id,slug,name,word,ville,cp,addr,tel,kicker,cap,mani,carte_h2,plats,band,salle_h2,google,note=NOTE_C,mark=None):
    C.append(dict(kind='resto',id=id,slug=slug,name=name,title=f'{name} · Restaurant à {ville}',tel=tel,mark=mark or name,status='Réservation en ligne',word=word,
     kicker=kicker,cap=cap,mani=mani,carte_h2=carte_h2,plats=plats,carte_note=note,band=band,
     salle_h2=salle_h2,salle_p=f"{addr}, à {ville}. Sur le vrai site : vos photos, votre carte et vos horaires à jour.",
     infos=[('Adresse',f'{addr}, {ville}'),('Téléphone',tel),('Sur Google',google)],addr=addr,google=google,ville=ville,cp=cp))
SOINS_NOTE='Exemples de soins. Sur le vrai site : votre carte, vos durées et vos tarifs exacts.'
def I(id,slug,name,logo,ville,cp,addr,tel,h1,kicker,hero_p,univ_h2,univers,soins,panes,gift_soin,ft_big,avis,hours='À confirmer',note=SOINS_NOTE,gift='Au choix',verre_h2='Prenez le temps, <em>on s\'occupe du reste.</em>',univ_p='Chaque soin est expliqué simplement, pour choisir le bon avant de réserver.'):
    C.append(dict(kind='inst',id=id,slug=slug,name=name,logo=logo,title=f'{logo} · Institut de beauté à {ville}',tel=tel,h1=h1,h1_label=' '.join(h1),kicker=kicker,hero_p=hero_p,
     univ_h2=univ_h2,univ_p=univ_p,univers=univers,soins=soins,note=note,verre_h2=verre_h2,panes=panes,
     slots=['9 h 30','11 h 00','14 h 00','15 h 30','17 h 00'],gift=gift,gift_soin=gift_soin,ft_big=ft_big,addr=addr,hours=hours,avis=avis,ville=ville,cp=cp))

T='Sur demande'
# 1 The Beauty Room (Planity 26/10)
I('457055205594','the-beauty-room','The Beauty Room','The Beauty Room','Brunstatt-Didenheim','68350','7 rue de France','06 72 98 20 49',
  ['Le regard,','sublimé.'],'Institut spécialiste du regard · Brunstatt-Didenheim',
  'Extensions de cils cil à cil, volume hybride, réhaussement et sourcils au fil. Un salon soigné, dédié au regard.',
  'Un seul sujet : <em>votre regard.</em>',
  [('Extensions','Cil à cil ou volume.','Pose classique, effet Dolly, eye liner ou volume hybride, selon le regard voulu.'),('Réhaussement','Le naturel, en mieux.','Le réhaussement de cils courbe vos propres cils, sans extension.'),('Sourcils','Au fil.','Épilation au fil et teinture pour une ligne nette.')],
  [('Pose cil à cil classique','1 h 45','105 €','Le cil à cil pour un regard naturel.',['Extensions']),('Pose cil à cil Dolly','1 h 45','115 €','Un effet poupée, plus ouvert.',['Extensions']),('Volume hybride','1 h 45','120 €','Le mélange cil à cil et volume.',['Extensions']),('Réhaussement de cils','1 h','65 €','Vos cils courbés, sans extension.',['Regard']),('Épilation des sourcils au fil','30 min','15 €','La ligne des sourcils, au fil.',['Sourcils'])],
  [('Spécialiste du regard','Cils et sourcils, rien d\'autre : chaque geste est maîtrisé.'),('5,0 sur Planity','61 avis clients.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Réhaussement','Un regard qui <em>s\'ouvre.</em>','5,0 / 5 sur Planity',
  hours='Lun, 11 h – 18 h<br>Mar, 9 h – 16 h<br>Jeu – ven, 9 h 30 – 18 h<br>Sam, 9 h – 14 h',note='Tarifs relevés sur votre page Planity le 26/10/2026.',gift='65 €')
# 2 Ozalie
I('457118868726','ozalie','Ozalie','Ozalie','Brunstatt-Didenheim','68350','7 rue de France','03 69 76 50 38',
  ['Le visage,','enfin détendu.'],'Massage facialiste · Brunstatt-Didenheim',
  'Des massages du visage pour relâcher les tensions et retrouver un teint reposé. Réservez votre moment en ligne.',
  'Le soin <em>par les mains.</em>',
  [('Le massage du visage','Le cœur du métier.','Un massage précis du visage pour détendre les traits.'),('Le moment pour soi','Prendre le temps.','Une pause au calme, à Brunstatt-Didenheim.'),('Offrir','La carte cadeau.','Un massage à offrir, en quelques clics.')],
  [('Massage du visage','—',T,'Le massage facial, adapté à votre peau.',['Visage']),('Massage visage et nuque','—',T,'Le visage, la nuque et les épaules.',['Détente']),('Carte cadeau','—',T,'Un massage à offrir.',['Offrir'])],
  [('Un savoir-faire précis','Le massage du visage comme spécialité.'),('4,9 sur Google','Sur 67 avis.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Massage du visage','Un visage <em>reposé.</em>','4,9 / 5 sur Google')
R('456996875472','la-taverne','La Taverne','Taverne','Riedisheim','68400','365 rue de Bâle','03 89 44 63 76','Restaurant · rue de Bâle, Riedisheim',
  "Une adresse appréciée à Riedisheim, notée 4,7 sur 5 par plus de 200 clients sur Google. Réservez votre table en deux gestes.",
  'Une table de quartier, <em>notée 4,7</em> par ses clients.','À la <em>carte</em>',[('Le plat du jour','Midi'),('Les plats de la carte','Plats'),('Les desserts','Dessert')],
  ['Restaurant','Rue de Bâle','Riedisheim','Réservez en ligne'],'Une table <em>à Riedisheim.</em>','4,7 / 5 · 207 avis')
R('457140444363','chez-yaki','Chez Yaki','Yaki','Riedisheim','68400','250 rue de Bâle','03 89 64 97 20','Cuisine marocaine · rue de Bâle, Riedisheim',
  "La cuisine marocaine et méditerranéenne à Riedisheim, notée 4,4 sur 5 par plus de 600 clients sur Google. Réservez votre table en deux gestes.",
  'Le couscous, <em>généreux</em>, comme on l\'aime.','Les <em>spécialités</em>',[('Couscous royal','Plat'),('Grillades','Plat'),('Mezze','Entrée')],
  ['Cuisine marocaine','Méditerranée','Riedisheim','Réservez en ligne'],'Une table <em>généreuse.</em>','4,4 / 5 · 611 avis',note='Plats cités par vos clients en ligne. Sur le vrai site : votre carte complète et à jour.')
I('457055205595','armance-beaute','Armance Beauté','Armance Beauté','Riedisheim','68400','11 rue de Mulhouse (entrée 2 rue de Habsheim)','03 89 56 18 66',
  ['Prendre soin','de vous.'],'Institut de beauté · Riedisheim',
  'Un institut noté 5 sur 5 par ses clientes sur Google. Réservez votre soin en ligne, à toute heure.',
  'Votre institut, <em>à Riedisheim.</em>',
  [('Le visage','Les soins.','Des soins adaptés à votre peau.'),('Le corps','Les épilations.','Les épilations, pour toutes les zones.'),('Les mains','La beauté des mains.','Manucure et soin des mains.')],
  [('Soin du visage','—',T,'Un soin adapté à votre peau.',['Visage']),('Épilations','—',T,'Toutes les zones.',['Corps']),('Beauté des mains','—',T,'Manucure et soin.',['Mains'])],
  [('Noté 5 sur 5','35 avis sur Google.'),('Accès facile','Entrée par le 2 rue de Habsheim.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Soin du visage','Prenez soin de vous, <em>tout simplement.</em>','5 / 5 sur Google')
R('457151201473','le-schetzahus','Restaurant Le Schetzahus','Schetzahus','Riedisheim','68400','160 rue de Habsheim','09 81 51 55 54','Restaurant · rue de Habsheim, Riedisheim',
  "Une cuisine française généreuse, notée 4,5 sur 5 par plus de 450 clients sur Google. Réservez votre table en deux gestes.",
  'Des burgers, des ribs, <em>et des assiettes de chef.</em>','Quelques <em>classiques</em>',[('Ribs','Plat'),('Le Schetz\'burger XL','Plat'),('Risotto aux noix de Saint-Jacques','Plat'),('Tartare de bœuf','Plat'),('Café gourmand','Dessert')],
  ['Cuisine française','Rue de Habsheim','Riedisheim','Réservez en ligne'],'Une table <em>à Riedisheim.</em>','4,5 / 5 · 459 avis',note='Plats cités en ligne. Sur le vrai site : votre carte complète et à jour.',mark='Le Schetzahus')
R('457077517512','niji-ristorante','NIJI ristorante italiano','NIJI','Rixheim','68170','65 rue de Mulhouse','06 14 68 06 16','Ristorante italiano · Rixheim',
  "La cuisine italienne à Rixheim, notée 4,4 sur 5 par plus de 600 clients sur Google. Réservez votre table en deux gestes.",
  'La cuisine <em>italienne</em>, à Rixheim.','La <em>carta</em>',[('Antipasti','Entrée'),('Pâtes','Plat'),('Dolci','Dessert')],
  ['Ristorante italiano','Rue de Mulhouse','Rixheim','Réservez en ligne'],'Une table <em>italienne.</em>','4,4 / 5 · 640 avis',mark='NIJI')
R('457147728068','chez-celine','Chez Céline','Céline','Rixheim','68170','59 rue de Mulhouse','09 52 93 73 64','Kebab, grillades, pizzas au feu de bois · Rixheim',
  "Kebab, grillades et pizzas cuites au feu de bois, à Rixheim. Commandez ou réservez en deux gestes.",
  'Les pizzas <em>au feu de bois</em>, et les grillades.','Au <em>menu</em>',[('Pizzas au feu de bois','Pizza'),('Grillades','Plat'),('Kebab','Plat')],
  ['Pizza au feu de bois','Grillades','Kebab','Rixheim'],'Une adresse <em>à Rixheim.</em>','4,4 / 5 · 93 avis',note='Sur le vrai site : votre carte complète, vos prix et vos horaires.')
R('457106723012','la-brochette','Restaurant la brochette','Brochette','Rixheim','68170','116 Grand Rue Pierre Braun','03 89 42 05 46','Restaurant · Grand Rue, Rixheim',
  "Une adresse notée 4,8 sur 5 par plus de 200 clients sur Google, au cœur de Rixheim. Réservez votre table en deux gestes.",
  'Une table <em>notée 4,8</em> par ses clients.','À la <em>carte</em>',[('Les brochettes','Plat'),('Le plat du jour','Midi'),('Les desserts','Dessert')],
  ['Restaurant','Grand Rue','Rixheim','Réservez en ligne'],'Au cœur <em>de Rixheim.</em>','4,8 / 5 · 218 avis',mark='La Brochette')
I('457037732086','institut-frimousse','Institut Frimousse','Frimousse','Rixheim','68170',"1a rue de l'Étang",'03 89 54 47 33',
  ['Votre beauté,','sans attendre.'],'Institut de beauté · Rixheim',
  'Votre institut à Rixheim. Choisissez votre soin et réservez en ligne, à toute heure.',
  'Votre institut, <em>à Rixheim.</em>',
  [('Le visage','Les soins.','Des soins adaptés à votre peau.'),('Le corps','Les épilations.','Les épilations, pour toutes les zones.'),('Les mains','La beauté des mains.','Manucure et soin des mains.')],
  [('Soin du visage','—',T,'Un soin adapté à votre peau.',['Visage']),('Épilations','—',T,'Toutes les zones.',['Corps']),('Beauté des mains','—',T,'Manucure et soin.',['Mains'])],
  [('À Rixheim','Rue de l\'Étang.'),('77 avis sur Google','Note de 4,2 sur 5.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Soin du visage','Prenez soin de vous, <em>tout simplement.</em>','4,2 / 5 sur Google')
for c in C: json.dump(c,open(c['slug']+'.json','w'),ensure_ascii=False)
print(' '.join(c['slug']+'.json' for c in C))
