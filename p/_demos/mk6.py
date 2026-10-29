# Jeudi 29/10 : niche institut de beauté (e-mail).
import json
from mk3 import I, C
C.clear()
T='Sur demande'
I('459092137184','secret-beaute-thann','Institut Secret Beauté','Secret Beauté','Thann','68800','116 rue de la 1ère Armée','06 22 23 88 50',
  ['Votre moment','beauté.'],'Institut de beauté · Thann',
  'Onglerie, regard, massages et épilations, dans un institut noté 5 sur 5 par ses clientes. Réservez votre soin en ligne, à toute heure.',
  'Votre institut, <em>à Thann.</em>',
  [('Les ongles','L\'onglerie.','Pose et soin des ongles, pour des mains impeccables.'),('Le regard','Cils et sourcils.','Teinture des cils et sourcils, réhaussement de cils.'),('Le corps','Massages et épilations.','Un massage pour souffler, des épilations pour toutes les zones.')],
  [('Onglerie','—',T,'Pose et soin des ongles.',['Ongles']),('Réhaussement de cils','—',T,'Vos cils courbés, sans extension.',['Regard']),('Teinture cils et sourcils','—',T,'Un regard plus intense.',['Regard']),('Massage','—',T,'Un moment de détente.',['Corps']),('Épilations','—',T,'Toutes les zones.',['Corps'])],
  [('Noté 5 sur 5','29 avis sur Google.'),('À Thann','Rue de la 1ère Armée.'),('Réservation 24 h/24','Vos clientes réservent même le soir.')],
  'Massage','Prenez soin de vous, <em>tout simplement.</em>','5 / 5 sur Google')
for c in C: json.dump(c,open(c['slug']+'.json','w'),ensure_ascii=False)
print(' '.join(c['slug']+'.json' for c in C))
