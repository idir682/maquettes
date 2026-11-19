# 19/11/2026 : niche couvreur, 1 prospect avec e-mail public (Patrick Hirtzlin, Spechbach). Style Lattis Couverture validé.
import json
from mk3 import TM,TP,ZN,ROOF,STEPS,LOGO,NAV
from mk import HOUSE
hz=dict(id='471017194709',slug='hirtzlin',name='Patrick HIRTZLIN, Couverture Zinguerie Bardage',short='Hirtzlin',title='Patrick Hirtzlin · Couvreur zingueur à Spechbach depuis 1985',tel='03 89 06 13 22',
 acc='#a8642c',acc_hi='#c27a3c',acc_rgb='168,100,44',hero_img='toit',logo_svg=LOGO,nav=NAV,cta_head='Demander un devis',
 kicker='Couverture · Zinguerie · Bardage · Depuis 1985',h1=['Couvreur','zingueur','<em>depuis 1985.</em>'],h1_label='Couvreur zingueur depuis 1985.',
 hero_p="Patrick Hirtzlin et ses compagnons couvreurs-zingueurs rénovent votre toiture dans le Haut-Rhin, depuis Spechbach. Noté 4,9 sur 5 par 84 clients sur Google.",
 cta1='Demander un devis',cta2='Une fuite ?',band=['Couverture','Zinguerie cuivre','Isolation sur-toiture','Bardage','Fenêtres de toit','Depuis 1985','4,9/5 sur Google'],
 anat_k='Le toit',anat_h2='Un toit, <em>cinq couches.</em>',anat_label="Coupe d'une toiture : charpente, isolant, écran, liteaux et tuiles",anat_svg=ROOF,steps=STEPS,
 sv_h2='Du faîtage <em>à la façade.</em>',sv_p='Rénovation complète ou partielle de la couverture : un seul artisan pour tout le toit, même à faible pente.',
 cards=[dict(img='toit',alt='Toiture en tuiles terre cuite',t='Couverture',p='Tuile en terre cuite de fabrication française, posée selon les normes du DTU.',li=['Rénovation complète','Rénovation partielle','Faible pente']),
  dict(img='gouttiere',alt='Gouttière',t='Zinguerie',p='Gouttières et habillage de cheminée en cuivre, réalisés sur mesure dans nos ateliers.',li=['Gouttières','Cheminée','Cuivre']),
  dict(img='liteaux',alt='Liteaux et tuiles',t='Isolation',p='Isolation par sur-toiture (Efisarking) et tous types d\'isolants selon les normes énergétiques.',li=['Sur-toiture','Combles']),
  dict(img='palette',alt='Matériaux sur un chantier de toiture',t='Bardage et fenêtres de toit',p='Bardage de façade, lambris métalliques pour façades et corniches, pose de fenêtres de toit Velux ou Roto.',li=['Bardage','Corniches','Velux, Roto'])],
 storm_k='Urgence',storm_h2='Une fuite <span class="fl">après l\'orage&nbsp;?</span>',storm_p='Appelez directement. On vous dit quoi faire tout de suite, puis on organise l\'intervention.',storm_cta2='Décrire le problème',
 devis_p='Répondez depuis votre téléphone, on vous rappelle pour fixer un rendez-vous.',q1='Votre toit',t1='Toit',
 opts=[('Tuile mécanique',TM),('Tuile plate',TP),('Zinc, bac acier',ZN),('Je ne sais pas',HOUSE)],q3='Votre projet',chips=['Fuite, tuiles cassées','Réfection complète','Zinguerie, gouttières','Isolation, bardage'],
 towns=['Spechbach','Altkirch','Illfurth','Burnhaupt','Bernwiller','Dannemarie','Zillisheim','Brunstatt-Didenheim','Mulhouse','Waldighoffen'],
 faq=[('Refaites-vous toute la toiture ?','Oui, la rénovation complète comme partielle de la couverture, y compris les toits à faible pente.'),('Faites-vous la zinguerie ?','Oui : gouttières et habillage de cheminée en cuivre, réalisés sur mesure dans nos ateliers.'),('Posez-vous des fenêtres de toit ?','Oui, des fenêtres de toit Velux ou Roto.'),('Comment vous joindre ?','Par téléphone au 03 89 06 13 22, du lundi au vendredi de 9 h à 18 h sur rendez-vous, ou avec le formulaire : on vous rappelle.')],
 ft_about='Couverture, zinguerie, isolation et bardage dans le Haut-Rhin, depuis 1985.',addr=['29 rue d\'Illfurth, ZA','68720 Spechbach'],big='Hirtzlin',css='.ft .big{font-size:clamp(56px,14vw,240px)}')
json.dump(hz,open('hirtzlin.json','w'),ensure_ascii=False,indent=1)
