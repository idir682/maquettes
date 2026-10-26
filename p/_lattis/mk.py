import json
FLAME='<path d="M23 28c-7 0-10-5-8-10 2-4 5-5 5-12 5 3 9 8 9 13 0 5-3 9-6 9z"/>'
BATH='<path d="M3 14h40v5a8 8 0 0 1-8 8H11a8 8 0 0 1-8-8z"/><path d="M10 14V6a3 3 0 0 1 6 0"/>'
PIPE='<path d="M3 9h16v12H3zM19 12h24M19 18h24M31 6v18"/>'
HOUSE='<path d="M5 27V13L23 3l18 10v14zM18 27v-8h10v8"/>'
CLIM='<path d="M6 4h34v13H6zM10 11h26M13 21l-2 6M23 21v6M33 21l2 6"/>'
PAC='<path d="M5 3h36v24H5z"/><circle cx="20" cy="15" r="7"/><path d="M33 8v14"/>'
DROP='<path d="M23 3c6 8 9 12 9 17a9 9 0 0 1-18 0c0-5 3-9 9-17z"/>'
BOLT='<path d="M26 2 12 17h10l-4 11 16-16H24z"/>'
WOOD='<path d="M4 24h38M8 17h30M12 10h22"/><circle cx="23" cy="6" r="3"/>'
TOOL='<path d="M30 4a8 8 0 0 0-8 10L6 26l4 4 12-16a8 8 0 0 0 10-8l-5 3-4-4z"/>'
L='<g class="ly l{n}" stroke="{c}" stroke-width="{w}"{x}>{p}</g>'
def ly(n,c,w,p,x=''): return L.format(n=n,c=c,w=w,p=p,x=x)

conti=dict(id='457124141244',slug='conti-david',name='Conti David',short='Conti David',title='Conti David · Chauffagiste et plombier à Mulhouse',tel='03 89 64 44 96',
 acc='#c8742f',acc_hi='#dd8a43',acc_rgb='200,116,47',hero_img='ac2',
 logo_svg='<path d="M20 4c7 9 10 14 10 19a10 10 0 0 1-20 0c0-5 3-10 10-19z" fill="none" stroke="ACC" stroke-width="3.5"/><path d="M15 24a5 5 0 0 0 5 5" fill="none" stroke="#eeebe5" stroke-width="3"/>',
 nav=[('anatomie','Le chantier'),('services','Prestations'),('orage','Dépannage'),('devis','Devis'),('zone','Secteur')],cta_head='Devis gratuit',
 kicker='Chauffage · Sanitaire · Mulhouse',h1=['Chauffage.','Sanitaire.','<em>Bien fait.</em>'],h1_label='Chauffage. Sanitaire. Bien fait.',
 hero_p="Depuis 14 ans, Conti David installe votre chauffage, refait vos sanitaires et rénove votre logement. Un travail propre, sérieux, de qualité et dans le respect des délais.",
 cta1='Demander un devis',cta2='Une fuite ?',band=['Chauffage','Sanitaire','Plomberie','Rénovation','Devis gratuit','14 ans de métier'],
 anat_k='Le chantier',anat_h2='Un chantier, <em>cinq étapes.</em>',anat_label="Coupe d'une salle de bain : murs, arrivées d'eau, évacuation, radiateur et sanitaires",
 anat_svg=ly(1,'#8b939c',8,'<path d="M60 360H580M90 360V70M550 360V70M90 70H550"/>')+ly(2,'#5f7fa6',6,'<path d="M110 340H300V190H340M110 320H280V210H340"/>')+ly(3,'#c9cfd4',10,'<path d="M200 360V320M380 360V300H420"/>')+ly(4,'#b08a5a',60,'<path d="M440 200H530"/>',' stroke-dasharray="5 9"')+ly(5,'ACC',8,'<path d="M120 320H280V280H120zM330 230H420L408 262H342zM375 230V196H392"/>'),
 steps=[('Visite et devis','On passe voir votre logement et on vous remet un devis gratuit, écrit et détaillé.'),('Dépose','Ancien équipement retiré proprement, pièces protégées.'),('Plomberie','Arrivées d\'eau et évacuations refaites ou adaptées.'),('Chauffage','Installation ou remplacement de votre système de chauffage.'),('Sanitaires et finitions','Pose, réglages, nettoyage du chantier. Dans le respect des délais annoncés.')],
 sv_h2='Quatre métiers, <em>un artisan.</em>',sv_p='Chauffage, sanitaire, plomberie et rénovation : vous gardez le même interlocuteur du devis à la fin du chantier.',
 cards=[dict(img='ac3',alt='Ballon d\'eau chaude et vasque',t='Chauffage',p='Vente et installation de votre chauffage, choisi selon votre logement.',li=['Vente','Installation','Remplacement']),
  dict(img='bm1',alt='Salle de bain rénovée',t='Sanitaires',p='Salle de bain, WC, lavabos, robinetterie : une pose soignée.',li=['Salle de bain','WC','Robinetterie']),
  dict(img='ac1',alt='Raccord en cuivre serré dans un étau',t='Plomberie',p='Alimentation, évacuation, fuites : on remet tout en ordre.',li=['Fuites','Évacuations','Raccordements']),
  dict(img='bm2',alt='Salle de bain moderne',t='Rénovation',p='Rénovation de votre logement, plomberie et chauffage compris.',li=['Rénovation','Coordination','Finitions'])],
 storm_k='Dépannage',storm_h2='Une fuite <span class="fl">sous l\'évier&nbsp;?</span>',storm_p='Appelez directement. On vous dit quoi faire tout de suite pour limiter les dégâts, puis on organise l\'intervention.',storm_cta2='Décrire le problème',
 devis_p='Répondez depuis votre téléphone, on vous rappelle pour fixer une visite. Le devis est gratuit.',q1='Votre projet',t1='Projet',
 opts=[('Chauffage',FLAME),('Salle de bain',BATH),('Plomberie',PIPE),('Rénovation',HOUSE)],q3='Votre situation',chips=['Installation neuve','Remplacement','Fuite ou panne','Rénovation complète'],
 towns=['Mulhouse','Riedisheim','Rixheim','Illzach','Kingersheim','Wittenheim','Pfastatt','Brunstatt-Didenheim','Sausheim','Lutterbach'],
 faq=[('Le devis est-il gratuit ?','Oui, le devis est gratuit et sans engagement.'),('Pouvez-vous tout regrouper dans un seul chantier ?','Oui : chauffage, sanitaires et plomberie peuvent être faits par la même entreprise.'),('Depuis quand existe l\'entreprise ?','Conti David exerce depuis 14 ans à Mulhouse.'),('Comment vous joindre ?','Par téléphone au 03 89 64 44 96, ou avec le formulaire de devis : on vous rappelle.')],
 ft_about='Chauffage, sanitaire, plomberie et rénovation à Mulhouse. « L\'énergie est notre avenir, économisons-la ! »',addr=['34 avenue de Riedisheim','68100 Mulhouse'],big='Conti',css='')

h2o=dict(id='456817924335',slug='h2o-plombier-mulhouse',name='H2O Plombier Chauffagiste Mulhouse',short='H2O',title='H2O · Plombier chauffagiste à Mulhouse',tel='03 89 43 37 98',
 acc='#19a7a3',acc_hi='#2cc2bd',acc_rgb='25,167,163',hero_img='bm2',
 base={'--ardoise:#15181c':'--ardoise:#0f1b22','--ardoise2:#1d2127':'--ardoise2:#16252e','21,24,28':'15,27,34'},
 logo_svg='<path d="M5 15c5-5 10-5 15 0s10 5 15 0M5 24c5-5 10-5 15 0s10 5 15 0" fill="none" stroke="ACC" stroke-width="3.5"/><path d="M5 33h30" stroke="#eeebe5" stroke-width="3"/>',
 nav=[('anatomie','L\'installation'),('services','Prestations'),('orage','Dépannage'),('devis','Devis'),('zone','Secteur')],cta_head='Demander un devis',
 kicker='Plombier chauffagiste · Plus de 20 ans à Mulhouse',h1=['L\'eau.','La chaleur.','<em>Le confort.</em>'],h1_label="L'eau. La chaleur. Le confort.",
 hero_p='Salle de bain, chaudière, pompe à chaleur, climatisation, dépannage et entretien. Qualibat RGE, Professionnel du gaz, station technique agréée Vaillant.',
 cta1='Demander un devis',cta2='Une panne ?',band=['Qualibat RGE','Professionnel du gaz','Station technique agréée Vaillant','Handibat','Silverbat','Plus de 20 ans'],
 anat_k='L\'installation',anat_h2='De la chaudière <em>au robinet.</em>',anat_label='Schéma d\'une maison : chaudière, circuit de chauffage, radiateurs et eau chaude',
 anat_svg=ly(1,'#8b939c',8,'<path d="M70 360H570M100 360V170L320 50 540 170V360"/>')+ly(2,'#c9cfd4',6,'<path d="M130 340V250H200V340"/>')+ly(3,'#d9643c',5,'<path d="M200 270H300V200H460M200 300H320V215H460"/>')+ly(4,'#b08a5a',50,'<path d="M300 320H420M440 180H520"/>',' stroke-dasharray="5 9"')+ly(5,'ACC',6,'<path d="M200 320H250V360M470 270H500V300M486 300V318"/>'),
 steps=[('Diagnostic','On regarde votre logement et votre installation actuelle avant de proposer quoi que ce soit.'),('Chaudière ou pompe à chaleur','Le cœur du chauffage, installé par une entreprise RGE.'),('Circuit de chauffage','Les tuyaux qui portent l\'eau chaude jusqu\'aux pièces.'),('Radiateurs','La chaleur diffusée pièce par pièce.'),('Eau chaude et robinetterie','Jusqu\'à la douche et au robinet, avec une salle de bain adaptée si besoin.')],
 sv_h2='Cinq services, <em>une équipe.</em>',sv_p='Du projet de salle de bain à l\'entretien de la chaudière, tout est fait par la même entreprise.',
 cards=[dict(img='douche',alt='Douche à l\'italienne',t='Salle de bain',p='Douches, baignoires, robinetterie, WC et meubles. Adaptations Handibat et Silverbat.',li=['Douche','Baignoire','Accessibilité']),
  dict(img='ac3',alt='Ballon d\'eau chaude',t='Chauffage',p='Chaudières et pompes à chaleur, par une entreprise Qualibat RGE.',li=['Chaudière','Pompe à chaleur','RGE']),
  dict(img='pac',alt='Unité extérieure',t='Climatisation',p='Mono-split, multi-split ou gainable selon votre logement.',li=['Mono-split','Multi-split','Gainable']),
  dict(img='ac2',alt='Plombier serrant un raccord',t='Dépannage',p='Panne de chauffage ou fuite d\'eau : un seul numéro à appeler.',li=['Plomberie','Chauffage']),
  dict(img='ac1',alt='Raccord en cuivre',t='Entretien',p='Entretien annuel et contrat pour votre chaudière gaz.',li=['Entretien annuel','Contrat'])],
 storm_k='Dépannage',storm_h2='Plus de chauffage <span class="fl">en plein hiver&nbsp;?</span>',storm_p='Appelez directement. Station technique agréée Vaillant, l\'équipe connaît votre matériel.',storm_cta2='Décrire la panne',
 devis_p='Répondez depuis votre téléphone, on vous rappelle pour en parler et fixer une visite.',q1='Votre projet',t1='Projet',
 opts=[('Salle de bain',BATH),('Chaudière',FLAME),('Pompe à chaleur',PAC),('Climatisation',CLIM)],q3='Votre besoin',chips=['Projet neuf','Remplacement','Dépannage','Contrat d\'entretien'],
 towns=['Mulhouse','Colmar','Saint-Louis','Rixheim','Kingersheim','Illzach','Wittenheim','Brunstatt-Didenheim','Riedisheim','Pfastatt','Lutterbach','Sausheim','Baldersheim','Morschwiller-le-Bas'],
 faq=[('Êtes-vous certifiés RGE ?','Oui, l\'entreprise est Qualibat RGE, ce qui compte pour certaines aides à la rénovation.'),('Proposez-vous un contrat d\'entretien ?','Oui : entretien annuel et contrat pour chaudière gaz.'),('Adaptez-vous les salles de bain pour les seniors ?','Oui, l\'entreprise a les labels Handibat et Silverbat.'),('Réparez-vous les chaudières Vaillant ?','Oui, H2O est station technique agréée Vaillant.')],
 ft_about='Plombier chauffagiste à Mulhouse depuis plus de 20 ans.',addr=['14 rue de Hirsingue','68200 Mulhouse'],big='H2O',css='')

rch=dict(id='455808504027',slug='r-chauffe',name="R'Chauffe",short="R'Chauffe",title="R'Chauffe · Pompe à chaleur à Mulhouse, RGE QualiPAC",tel='06 89 55 55 02',
 acc='#e8571e',acc_hi='#ff6e33',acc_rgb='232,87,30',hero_img='pac',
 logo_svg='<path d="M4 22 20 8l16 14" fill="none" stroke="ACC" stroke-width="3.5"/><path d="M13 30c3-4 6-4 9 0s6 4 9 0" fill="none" stroke="#eeebe5" stroke-width="3"/>',
 nav=[('anatomie','La PAC'),('services','Prestations'),('orage','L\'hiver'),('devis','Rappel'),('zone','Secteur')],cta_head='Être rappelé',
 kicker='Pompes à chaleur · Certifié RGE QualiPAC · Mulhouse',h1=['La chaleur','de l\'air,','<em>chez vous.</em>'],h1_label="La chaleur de l'air, chez vous.",
 hero_p="R'Chauffe installe pompes à chaleur et chauffe-eau thermodynamiques à Mulhouse. Entreprise certifiée RGE QualiPAC, valable jusqu'au 10/04/2027.",
 cta1='Parler de mon projet',cta2='Comment ça marche ?',band=['RGE QualiPAC','Pompe à chaleur','Chauffe-eau thermodynamique','Mulhouse','Étude sur place'],
 anat_k='Comment ça marche',anat_h2='L\'air dehors, <em>la chaleur dedans.</em>',anat_label='Schéma d\'une pompe à chaleur : unité extérieure, liaison, module intérieur et radiateurs',
 anat_svg=ly(1,'#8b939c',8,'<path d="M30 360H610M240 360V170L420 60 600 170V360"/>')+ly(2,'#c9cfd4',6,'<path d="M50 260H190V350H50z"/><circle cx="105" cy="305" r="30"/>')+ly(3,'#5f7fa6',5,'<path d="M190 280H280V230M190 300H300V230"/>')+ly(4,'#b08a5a',50,'<path d="M330 320H450M480 200H570"/>',' stroke-dasharray="5 9"')+ly(5,'ACC',6,'<path d="M270 190H330V250H270zM330 210H470M330 230H460V300"/>'),
 steps=[('Unité extérieure','Elle capte les calories présentes dans l\'air, même quand il fait froid.'),('Liaison','Un fluide transporte cette énergie jusqu\'à la maison.'),('Montée en température','Le compresseur élève la température pour chauffer l\'eau du circuit.'),('Module intérieur','Il transmet la chaleur au circuit de chauffage et à l\'eau chaude.'),('Radiateurs ou plancher','La chaleur arrive dans chaque pièce. L\'étude sur place vérifie que vos émetteurs conviennent.')],
 sv_h2='La pompe à chaleur, <em>notre métier.</em>',sv_p='Une installation qui se prépare : on vérifie votre logement avant de vous proposer un matériel.',
 cards=[dict(img='pac',alt='Unité extérieure de pompe à chaleur',t='Pompe à chaleur',p='Étude et installation d\'une pompe à chaleur pour chauffer votre logement.',li=['Étude','Installation','Mise en service']),
  dict(img='ac3',alt='Ballon d\'eau chaude',t='Chauffe-eau thermodynamique',p='L\'eau chaude produite avec l\'énergie de l\'air.',li=['Eau chaude','RGE QualiPAC']),
  dict(img='ac1',alt='Raccord en cuivre',t='Étude et conseil',p='Isolation, radiateurs, emplacement de l\'unité : on vérifie avant de vous engager.',li=['Visite','Conseil'])],
 storm_k='L\'hiver alsacien',storm_h2='Dehors, il pleut, <span class="fl">il fait froid.</span>',storm_p='La pompe à chaleur puise quand même son énergie dans l\'air extérieur. Encore faut-il qu\'elle soit bien choisie et bien posée.',storm_cta2='Parler de mon projet',
 devis_p='Trois réponses depuis votre téléphone, et on vous rappelle pour en parler. Sans engagement.',q1='Votre chauffage actuel',t1='Chauffage actuel',
 opts=[('Fioul',DROP),('Gaz',FLAME),('Électrique',BOLT),('Bois',WOOD)],q3='Votre projet',chips=['Pompe à chaleur','Chauffe-eau thermodynamique','Les deux','Je ne sais pas encore'],
 towns=['Mulhouse','Riedisheim','Illzach','Kingersheim','Wittenheim','Rixheim','Pfastatt','Brunstatt-Didenheim'],
 faq=[('Que veut dire RGE QualiPAC ?','C\'est une qualification pour installer des pompes à chaleur et des chauffe-eau thermodynamiques. Elle est souvent demandée pour bénéficier d\'aides à la rénovation.'),('Ma maison est-elle adaptée ?','Ça dépend de l\'isolation et des radiateurs. On le vérifie lors de la visite.'),('Installez-vous aussi des chauffe-eau thermodynamiques ?','Oui, la certification couvre aussi le chauffe-eau thermodynamique.')],
 ft_about="Pompes à chaleur et chauffe-eau thermodynamiques à Mulhouse. Certifié RGE QualiPAC.",addr=['27 rue Furstenberger','68200 Mulhouse'],big="R'Chauffe",css='.ft .big{font-size:clamp(60px,15vw,260px)}')
for n,c in [('conti',conti),('h2o',h2o),('rchauffe',rch)]: json.dump(c,open(n+'.json','w'),ensure_ascii=False,indent=1)
