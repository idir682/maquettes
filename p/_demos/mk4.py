# Tournée du jeudi 29/10 : 10 prospects (nord de Mulhouse, Kingersheim, Wittenheim).
import json, io, contextlib
with contextlib.redirect_stdout(io.StringIO()): import mk3 as m
m.C.clear(); R, I, C, T = m.R, m.I, m.C, m.T
R('456805033152','la-riziere-doree','La Rizière Dorée','Rizière','Mulhouse','68200','85 rue de Soultz','03 89 55 29 78','Cuisine thaï · rue de Soultz, Mulhouse',
  "La cuisine thaï à Mulhouse, notée 4,8 sur 5 par près de 400 clients sur Google. Réservez votre table en deux gestes.",
  'Les saveurs <em>de Thaïlande</em>, rue de Soultz.','La <em>carte</em>',[('Les entrées','Entrée'),('Les currys et les woks','Plat'),('Les desserts','Dessert')],
  ['Cuisine thaï','Rue de Soultz','Mulhouse','Réservez en ligne'],'Une table <em>thaï.</em>','4,8 / 5 · 390 avis',mark='La Rizière Dorée')
R('457135121606','la-roseraie','La Roseraie','Roseraie','Kingersheim','68260','36 rue de Guebwiller','03 89 52 92 77','Restaurant · rue de Guebwiller, Kingersheim',
  "Une adresse incontournable de Kingersheim : plus de 1 300 avis sur Google, notée 4,4 sur 5. Réservez votre table en deux gestes.",
  'Plus de <em>1 300 avis</em>, une table connue de tous.','À la <em>carte</em>',[('Le plat du jour','Midi'),('Les plats de la carte','Plats'),('Les desserts','Dessert')],
  ['Restaurant','Rue de Guebwiller','Kingersheim','Réservez en ligne'],'Une table <em>à Kingersheim.</em>','4,4 / 5 · 1 369 avis')
R('457084682433','restaurant-vanny','Restaurant Vanny','Vanny','Kingersheim','68260','34 rue de Hirschau','03 89 48 63 87','Cuisine vietnamienne · Kingersheim',
  "La cuisine vietnamienne à Kingersheim, notée 4,9 sur 5 par près de 300 clients sur Google. Réservez votre table en deux gestes.",
  'La cuisine <em>vietnamienne</em>, notée 4,9.','La <em>carte</em>',[('Les entrées','Entrée'),('Les plats','Plat'),('Les desserts','Dessert')],
  ['Cuisine vietnamienne','Rue de Hirschau','Kingersheim','Réservez en ligne'],'Une table <em>vietnamienne.</em>','4,9 / 5 · 285 avis',mark='Vanny')
R('456818125037','chez-aydin','Restaurant grill chez Aydin','Aydin','Wittenheim','68270','1 rue de Kingersheim','09 54 41 74 82','Restaurant grill · Wittenheim',
  "Le grill de Wittenheim, noté 4,3 sur 5 par plus de 500 clients sur Google. Réservez votre table en deux gestes.",
  'Les grillades, <em>servies généreusement.</em>','Au <em>grill</em>',[('Les grillades','Plat'),('Le plat du jour','Midi'),('Les desserts','Dessert')],
  ['Grill','Rue de Kingersheim','Wittenheim','Réservez en ligne'],'Une table <em>à Wittenheim.</em>','4,3 / 5 · 503 avis',mark='Chez Aydin')
I('456987581639','m-beauty','M BEAUTY','M Beauty','Wittenheim','68270','28 rue de Kingersheim','03 89 51 01 72',
  ['Visage, corps,','regard, ongles.'],'Institut de beauté · près de la place Tiers, Wittenheim',
  'Soins du visage et du corps, drainage lymphatique méthode Renata França, épilations, cils et sourcils, ongles. Ouvert du lundi au samedi.',
  'Tout votre institut, <em>à Wittenheim.</em>',
  [('Le visage','Les soins.','Le soin hydratant Destination Fjord et les soins du visage.'),('Le corps','Drainage et épilations.','Drainage lymphatique méthode Renata França, épilations à la cire.'),('Regard et ongles','Les finitions.','Teinture des sourcils, pose de capsules et gel.')],
  [('Soin Destination Fjord','1 h 15','75 €','Le soin hydratant du visage.',['Visage']),('Pose de capsules et gel','1 h 30','58 €','La pose complète.',['Ongles']),('Sourcils, création de ligne','20 min','16 €','À la cire.',['Sourcils']),('Teinture des sourcils','25 min','16 €','Un regard plus marqué.',['Regard']),('Sourcils, entretien','10 min','12 €','À la cire.',['Sourcils'])],
  [('Ouvert du lundi au samedi','Le lundi dès 13 h, du mardi au vendredi dès 9 h.'),('4,9 sur Planity','Sur 249 avis.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Soin Destination Fjord','Prenez soin de vous, <em>à deux pas.</em>','4,9 / 5 sur Planity',
  hours='Lun, 13 h – 19 h<br>Mar – ven, 9 h – 19 h<br>Sam, 9 h – 15 h',note='Tarifs relevés sur votre page Planity le 26/10/2026.',gift='75 €')
R('456771060958','enjoy-restaurant','Enjoy restaurant','Enjoy','Wittenheim','68270','47 rue de Kingersheim','09 88 58 64 24','Restaurant · rue de Kingersheim, Wittenheim',
  "Une adresse notée 4,9 sur 5 par ses clients sur Google, à Wittenheim. Réservez votre table en deux gestes.",
  'Une table <em>notée 4,9</em> par ses clients.','À la <em>carte</em>',[('Le plat du jour','Midi'),('Les plats de la carte','Plats'),('Les desserts','Dessert')],
  ['Restaurant','Rue de Kingersheim','Wittenheim','Réservez en ligne'],'Une table <em>à Wittenheim.</em>','4,9 / 5 · 97 avis',mark='Enjoy')
I('457055205593','institut-celeste','institut celeste','Céleste','Wittenheim','68270','4 rue de Guebwiller','03 89 57 43 31',
  ['Un moment','rien qu\'à vous.'],'Institut de beauté · Wittenheim',
  'Un institut noté 4,8 sur 5 par plus de 100 clientes sur Google. Choisissez votre soin et réservez en ligne, à toute heure.',
  'Votre institut, <em>à Wittenheim.</em>',
  [('Le visage','Les soins.','Des soins adaptés à votre peau.'),('Le corps','Les épilations.','Les épilations, pour toutes les zones.'),('Les mains','La beauté des mains.','Manucure et soin des mains.')],
  [('Soin du visage','—',T,'Un soin adapté à votre peau.',['Visage']),('Épilations','—',T,'Toutes les zones.',['Corps']),('Beauté des mains','—',T,'Manucure et soin.',['Mains'])],
  [('4,8 sur Google','Sur 117 avis.'),('Rue de Guebwiller','À Wittenheim.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Soin du visage','Prenez soin de vous, <em>tout simplement.</em>','4,8 / 5 sur Google')
R('456761901293','les-hirondelles','Les Hirondelles','Hirondelles','Wittenheim','68270','8 rue de Soultz','03 89 50 89 35','Restaurant · rue de Soultz, Wittenheim',
  "Côte de bœuf, steak frites, cordon bleu : une table généreuse, notée 4,4 sur 5 par près de 400 clients sur Google.",
  'Des viandes <em>généreuses</em>, à Wittenheim.','Quelques <em>classiques</em>',[('Côte de bœuf','Plat'),('Foie gras et confit d\'oignon','Entrée'),('Filet mignon de porc','Plat'),('Cordon bleu','Plat'),('Steak frites','Plat')],
  ['Restaurant','Rue de Soultz','Wittenheim','Réservez en ligne'],'Une table <em>à Wittenheim.</em>','4,4 / 5 · 395 avis',note='Plats cités en ligne. Sur le vrai site : votre carte complète et à jour.')
R('457129655497','le-boreal','Restaurant le Boréal','Boréal','Wittenheim','68270',"1 rue d'Ensisheim",'03 89 52 43 73','Cuisine française et alsacienne · Wittenheim',
  "Tarte flambée, choucroute, bouchée à la reine : la cuisine du terroir, notée 4,4 sur 5 par plus de 270 clients sur Google.",
  'La cuisine <em>du terroir</em>, faite maison.','Les <em>classiques</em>',[('Tarte flambée gratinée','Plat'),('Choucroute garnie','Plat'),('Bouchée à la reine','Plat'),('Escargots à l\'alsacienne','Entrée'),('Tarte aux myrtilles','Dessert')],
  ['Tarte flambée','Choucroute','Wittenheim','Réservez en ligne'],'Une table <em>alsacienne.</em>','4,4 / 5 · 271 avis',note='Plats cités en ligne. Sur le vrai site : votre carte complète et à jour.',mark='Le Boréal')
I('457133271287','l-instant-beaute','l\'Instant Beauté','L\'Instant Beauté','Wittenheim','68270','227 rue du Dr Albert Schweitzer','06 34 10 08 80',
  ['Un instant,','pour vous.'],'Institut de beauté · Wittenheim',
  'Un institut noté 5 sur 5 par ses clientes sur Google. Choisissez votre soin et réservez en ligne, à toute heure.',
  'Votre institut, <em>à Wittenheim.</em>',
  [('Le visage','Les soins.','Des soins adaptés à votre peau.'),('Le corps','Les épilations.','Les épilations, pour toutes les zones.'),('Les mains','La beauté des mains.','Manucure et soin des mains.')],
  [('Soin du visage','—',T,'Un soin adapté à votre peau.',['Visage']),('Épilations','—',T,'Toutes les zones.',['Corps']),('Beauté des mains','—',T,'Manucure et soin.',['Mains'])],
  [('Noté 5 sur 5','Sur Google.'),('Rue du Dr Schweitzer','À Wittenheim.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Soin du visage','Prenez soin de vous, <em>tout simplement.</em>','5 / 5 sur Google')
for c in C: json.dump(c,open(c['slug']+'.json','w'),ensure_ascii=False)
print(' '.join(c['slug']+'.json' for c in C))
