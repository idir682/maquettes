# 30/10/2026 : niche couvreur, 2 prospects avec e-mail public (envoi auto 9h). Style Lattis Couverture validé.
import json
from mk import HOUSE,TOOL,DROP,ly
TM='<path d="M2 26c5-10 9-10 14 0 5-10 9-10 14 0 5-10 9-10 14 0M2 14c5-10 9-10 14 0 5-10 9-10 14 0 5-10 9-10 14 0"/>'
TP='<path d="M3 6h12v10H3zM17 6h12v10H17zM31 6h12v10H31zM10 16h12v10H10zM24 16h12v10H24z"/>'
ZN='<path d="M2 26V6M11 26V6M20 26V6M29 26V6M38 26V6M2 26h42"/>'
ROOF=(ly(1,'#8b939c',10,'<path d="M40 360 320 90 600 360"/><path d="M110 360V294M530 360V294M190 360V218M450 360V218"/><path d="M30 360h580"/>')
 +ly(2,'#d9c58f',16,'<path d="M66 340 320 96 574 340"/>',' opacity=".9"')+ly(3,'#5f7fa6',4,'<path d="M56 330 320 78 584 330"/>')
 +ly(4,'#b08a5a',7,'<path d="M60 318 320 66 580 318" stroke-dasharray="2 26"/>')+ly(5,'ACC',14,'<path d="M44 322 320 54 596 322"/>'))
STEPS=[('Charpente','On vérifie chevrons et pannes avant tout. Une pièce abîmée se remplace, elle ne se cache pas sous des tuiles neuves.'),('Isolant','Le moment idéal pour isoler par le toit, quand la couverture est déjà déposée.'),('Écran sous-toiture','Il protège des infiltrations, tout en laissant respirer la charpente.'),('Liteaux','Leur écartement suit le modèle de tuile. C\'est lui qui fait un toit droit et étanche.'),('Tuiles et faîtage','Tuile mécanique, plate ou ardoise, posée et fixée selon l\'exposition du bâtiment.')]
LOGO='<path d="M4 30 20 8l16 22" fill="none" stroke="ACC" stroke-width="3.5"/><path d="M12 30h16" stroke="#eeebe5" stroke-width="3"/>'
NAV=[('anatomie','Le toit'),('services','Prestations'),('orage','Urgence'),('devis','Devis'),('zone','Secteur')]
mk=dict(id='459635349746',slug='mk-toiture',name='MK Toiture',short='MK Toiture',title='MK Toiture · Couvreur et zingueur à Mulhouse',tel='07 60 05 56 75',
 acc='#c4532f',acc_hi='#d9643c',acc_rgb='196,83,47',hero_img='toit',logo_svg=LOGO,nav=NAV,cta_head='Devis gratuit',
 kicker='Couverture · Zinguerie · Mulhouse',h1=['Un toit','qui tient','<em>la saison.</em>'],h1_label='Un toit qui tient la saison.',
 hero_p="MK Toiture refait votre toiture, votre zinguerie et votre charpente à Mulhouse et autour. Noté 4,9 sur 5 par 62 clients sur Google.",
 cta1='Demander un devis',cta2='Une fuite ?',band=['Couverture','Zinguerie','Charpente','Isolation','Chien assis','Nettoyage de toiture','4,9/5 sur Google'],
 anat_k='Le toit',anat_h2='Un toit, <em>cinq couches.</em>',anat_label="Coupe d'une toiture : charpente, isolant, écran, liteaux et tuiles",anat_svg=ROOF,steps=STEPS,
 sv_h2='Du faîtage <em>à la gouttière.</em>',sv_p='Couverture, zinguerie, charpente et isolation : un seul interlocuteur pour tout le toit.',
 cards=[dict(img='toit',alt='Toiture en tuiles terre cuite',t='Couverture',p='Réfection et pose de toiture, contrôle de la charpente avant les tuiles.',li=['Réfection','Tuiles']),
  dict(img='liteaux',alt='Liteaux et tuiles plates',t='Charpente, lucarnes, chiens assis',p='Charpente, habillage de lucarne et création de chien assis.',li=['Charpente','Lucarne','Chien assis']),
  dict(img='gouttiere',alt='Gouttière en zinc',t='Zinguerie',p='Gouttières, habillage de cheminée et finitions en zinc.',li=['Gouttières','Cheminée']),
  dict(img='palette',alt='Tuiles terre cuite sur un chantier',t='Isolation et nettoyage',p='Isolation intérieure et extérieure, nettoyage de toiture.',li=['Isolation','Nettoyage'])],
 storm_k='Urgence',storm_h2='Une fuite <span class="fl">après l\'orage&nbsp;?</span>',storm_p='Appelez directement. On vous dit quoi faire tout de suite, puis on organise l\'intervention.',storm_cta2='Décrire le problème',
 devis_p='Répondez depuis votre téléphone, on vous rappelle pour fixer une visite. Le devis est gratuit.',q1='Votre toit',t1='Toit',
 opts=[('Tuile mécanique',TM),('Tuile plate',TP),('Zinc, bac acier',ZN),('Je ne sais pas',HOUSE)],q3='Votre situation',chips=['Fuite, tuiles cassées','Réfection complète','Gouttières, zinguerie','Isolation'],
 towns=['Mulhouse','Riedisheim','Illzach','Kingersheim','Wittenheim','Rixheim','Brunstatt-Didenheim','Lutterbach','Pfastatt','Sausheim'],
 faq=[('Le devis est-il gratuit ?','Oui, le devis est gratuit et sans engagement.'),('Faites-vous la zinguerie ?','Oui : gouttières, habillage de cheminée et de lucarne.'),('Créez-vous des chiens assis ?','Oui, MK Toiture crée des chiens assis et habille les lucarnes.'),('Comment vous joindre ?','Par téléphone au 07 60 05 56 75, ou avec le formulaire de devis : on vous rappelle.')],
 ft_about='Couvreur et zingueur à Mulhouse : couverture, zinguerie, charpente, isolation.',addr=['6 rue du Cèdre','68200 Mulhouse'],big='MK Toiture',css='.ft .big{font-size:clamp(56px,14vw,240px)}')
ro=dict(id='459511761103',slug='romani-et-fils',name='Romani & Fils',short='Romani & Fils',title='Romani & Fils · Couvreur à Brunstatt-Didenheim',tel='03 89 06 38 11',
 acc='#2f6f8c',acc_hi='#3f88a8',acc_rgb='47,111,140',hero_img='toit',logo_svg=LOGO,nav=NAV,cta_head='Devis gratuit',
 base={'--ardoise:#15181c':'--ardoise:#141a1e','--ardoise2:#1d2127':'--ardoise2:#1b2328'},
 kicker='Couverture · Gouttières · Brunstatt',h1=['Votre toit,','entre de','<em>bonnes</em>','<em>mains.</em>'],h1_label='Votre toit, entre de bonnes mains.',
 hero_p="Romani & Fils s'occupe de votre couverture, de vos gouttières et de l'étanchéité, à Brunstatt-Didenheim et autour de Mulhouse. Noté 4,7 sur 5 par ses clients sur Google.",
 cta1='Demander un devis',cta2='Une fuite ?',band=['Couverture','Gouttières','Étanchéité','Brunstatt-Didenheim','Devis gratuit','4,7/5 sur Google'],
 anat_k='Le toit',anat_h2='Un toit, <em>cinq couches.</em>',anat_label="Coupe d'une toiture : charpente, isolant, écran, liteaux et tuiles",anat_svg=ROOF,steps=STEPS,
 sv_h2='Trois métiers, <em>un seul toit.</em>',sv_p='Couverture, gouttières et étanchéité : une entreprise familiale pour tout le toit.',
 cards=[dict(img='toit',alt='Toiture en tuiles terre cuite',t='Couverture',p='Réfection et entretien de toiture, du contrôle de la charpente aux tuiles.',li=['Réfection','Entretien']),
  dict(img='gouttiere',alt='Gouttière en zinc',t='Gouttières',p='Pose et remplacement de gouttières et de descentes.',li=['Pose','Remplacement']),
  dict(img='liteaux',alt='Liteaux et tuiles plates',t='Étanchéité',p='Étanchéité de la toiture pour garder la maison au sec.',li=['Étanchéité','Réparation'])],
 storm_k='Urgence',storm_h2='Une fuite <span class="fl">après l\'orage&nbsp;?</span>',storm_p='Appelez directement. On vous dit quoi faire tout de suite, puis on organise l\'intervention.',storm_cta2='Décrire le problème',
 devis_p='Répondez depuis votre téléphone, on vous rappelle pour fixer une visite. Le devis est gratuit.',q1='Votre toit',t1='Toit',
 opts=[('Tuile mécanique',TM),('Tuile plate',TP),('Zinc, bac acier',ZN),('Je ne sais pas',HOUSE)],q3='Votre situation',chips=['Fuite, tuiles cassées','Réfection complète','Gouttières','Étanchéité'],
 towns=['Brunstatt-Didenheim','Mulhouse','Zillisheim','Flaxlanden','Morschwiller-le-Bas','Riedisheim','Illfurth','Hochstatt','Galfingue','Rixheim'],
 faq=[('Le devis est-il gratuit ?','Oui, le devis est gratuit et sans engagement.'),('Posez-vous des gouttières ?','Oui, Romani & Fils pose et remplace les gouttières.'),('Faites-vous l\'étanchéité ?','Oui, l\'étanchéité fait partie de nos métiers, avec la couverture.'),('Comment vous joindre ?','Par téléphone au 03 89 06 38 11, ou avec le formulaire de devis : on vous rappelle.')],
 ft_about='Couverture, gouttières et étanchéité à Brunstatt-Didenheim.',addr=['20 rue des Pyrénées','68350 Brunstatt-Didenheim'],big='Romani',css='.ft .big{font-size:clamp(56px,14vw,240px)}')
for n,c in [('mk-toiture',mk),('romani',ro)]: json.dump(c,open(n+'.json','w'),ensure_ascii=False,indent=1)
