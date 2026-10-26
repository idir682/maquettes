# Maquettes prospects dans le style des démos validées (24/10) : Table Ruelle (restaurant) et Atelier Nacre (institut).
# CSS et JS des démos repris tels quels ; seul le contenu (body) et quelques réglages changent.
import json, os, shutil, sys, html
e = html.escape
H = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(H); PREM = os.path.join(os.path.dirname(ROOT), 'premium')

def telh(t): return 'tel:+33' + t.replace(' ', '')[1:]
def rep(s, old, new):
    assert old in s, old[:80]
    return s.replace(old, new)

def head_tail(src, c):
    s = open(src).read()
    b0 = s.index('<body>'); b1 = s.index('<script src="../../lib/gsap')
    head, tail = s[:b0], s[b1:]
    head = head.replace(head[head.index('data-hubspot-id="'):head.index('"', head.index('data-hubspot-id="') + 17) + 1], f'data-hubspot-id="{c["id"]}"')
    head = head.replace(head[head.index('<title>'):head.index('</title>') + 8], f'<title>{e(c["title"])}</title>')
    i = head.index('<meta name="description"'); j = head.index('>', i)
    head = head[:i] + f'<meta name="description" content="Maquette proposée par Agence Turbo à {e(c["name"])}. Ce n\'est pas le site officiel de l\'entreprise.">' + head[j + 1:]
    head = head.replace('</style>', c.get('css', '') + '</style>')
    return head, tail

def banner(c): return f'<div class="demo">Maquette proposée par Agence Turbo à {e(c["name"])}. Ce n\'est pas le site officiel de l\'entreprise.</div>'
TURBO = '<div class="turbo" id="turbo"><div><b>Ce site peut être le vôtre</b>Maquette Agence Turbo. <a href="mailto:contact@agenceturbo.fr">contact@agenceturbo.fr</a></div><button aria-label="Fermer" onclick="this.parentNode.remove()">×</button></div>'

def resto(c):
    head, tail = head_tail(PREM + '/table-ruelle/index.html', c)
    n = len(c['word'].replace(' ', ''))
    head = head.replace('</style>', f'.word{{font-size:clamp(40px,{round(138/max(n,6),1)}vw,{int(380*6/max(n,6))}px)}}.word .sp{{width:.25em}}</style>')
    t = telh(c['tel'])
    word = ''.join('<span class="sp"> </span>' if ch == ' ' else f'<span>{e(ch)}</span>' for ch in c['word'])
    plats = ''.join(f'<div class="plat" data-img="{i%3}"><span class="n">{["i.","ii.","iii.","iv.","v."][i]}</span><h3>{e(p)}</h3><span class="pr"></span><p>{e(d)}</p></div>' for i, (p, d) in enumerate(c['plats']))
    band = ''.join(f'<span>{e(x)}</span>' for x in c['band'] * 2)
    infos = ''.join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in c['infos'])
    body = f'''<body>
{banner(c)}
<div class="top"><div class="bar w">
  <nav aria-label="Navigation"><a href="#ardoise">La carte</a><a href="#salle">Le lieu</a><a href="#resa">Réserver</a></nav>
  <a class="mark" href="#">{e(c['mark'])}</a>
  <div class="status"><span class="open"><i></i>{e(c['status'])}</span><a class="pill" href="#resa" data-mag>Réserver</a></div>
</div></div>
<main>
<section class="hero" aria-label="Accueil">
  <div class="stage">
    <h1 class="word" id="word" aria-label="{e(c['name'])}, restaurant à Mulhouse">{word}</h1>
    <div class="oval" aria-hidden="true"><div class="img" id="ovl"><img src="img/plat.webp" alt="" width="1100" height="1400"></div></div>
    <div class="cap" id="cap"><div><p class="k">{e(c['kicker'])}</p></div><p>{e(c['cap'])}</p></div>
  </div>
</section>
<section class="mani w" aria-label="Notre cuisine"><p id="mani">{c['mani']}</p></section>
<section class="ardoise" id="ardoise" data-bg="olive">
  <div class="w">
    <div class="hd"><h2>{c['carte_h2']}</h2><p class="date" id="today">Aujourd'hui</p></div>
    <div class="plats" id="plats">{plats}</div>
    <p style="margin-top:28px;font-size:13px;opacity:.65">{e(c['carte_note'])}</p>
  </div>
  <div class="prod" aria-hidden="true"><div class="tr">{band}</div></div>
</section>
<section class="salle" id="salle" data-bg="nuit">
  <div class="w">
    <div class="grid">
      <div><p class="k" style="color:rgba(243,236,224,.6);margin-bottom:22px">Le lieu</p><h2>{c['salle_h2']}</h2><p>{e(c['salle_p'])}</p></div>
      <div class="slats" id="slats"><img src="img/salle.webp" alt="Salle de restaurant (photo d'illustration)" width="1600" height="1000" loading="lazy"></div>
    </div>
    <div class="infos">{infos}</div>
  </div>
</section>
<section class="resa" id="resa" data-bg="creme">
  <div class="w grid">
    <div><p class="k" style="color:var(--mut);margin-bottom:22px">Réservation</p><h2>Une table <em>pour ce soir&nbsp;?</em></h2><p class="lead">Choisissez le jour, l'heure et le nombre de couverts. La demande arrive directement au restaurant, sans passer par une plateforme.</p></div>
    <div class="flip" id="flip"><div class="in">
      <div class="face front">
        <div><p class="lbl">Le jour</p><div class="days" id="days"></div></div>
        <div><p class="lbl">L'heure</p><div class="times" id="times"></div></div>
        <div><p class="lbl">Couverts</p><div class="cov"><button type="button" id="minus" aria-label="Un couvert de moins">−</button><div class="num" aria-live="polite"><span id="n">2</span></div><button type="button" id="plus" aria-label="Un couvert de plus">+</button></div></div>
        <div class="recap"><p id="recap">Table pour 2</p><button class="pill" type="button" id="ok" data-mag>Réserver</button></div>
      </div>
      <div class="face back" aria-live="polite"><h3>À très vite.</h3><p id="conf">Démonstration : sur le vrai site, la réservation arriverait au restaurant.</p><button class="pill out" type="button" id="again" style="justify-self:center">Modifier</button></div>
    </div></div>
  </div>
</section>
</main>
<footer class="ft" data-bg="nuit">
  <div class="w">
    <p class="bye" id="bye">À très vite.</p>
    <div class="cols">
      <div><h4>Réserver</h4><a href="{t}">{c['tel']}</a><a href="#resa">En ligne</a></div>
      <div><h4>Venir</h4><p>{e(c['addr'])}</p><p>68100 Mulhouse</p></div>
      <div><h4>Sur Google</h4><p>{e(c['google'])}</p></div>
      <div><h4>Horaires</h4><p>Vos horaires à jour, ici</p></div>
    </div>
    <div class="cp"><span>{e(c['name'])} · maquette de démonstration non officielle</span><span>Conçu par <a href="https://agenceturbo.fr" style="text-decoration:underline">Agence Turbo</a></span></div>
  </div>
</footer>
<div class="peek" id="peek" aria-hidden="true"><img src="img/plat.webp" alt=""><img src="img/poisson.webp" alt=""><img src="img/salle.webp" alt=""></div>
<div class="cursor" id="cur" aria-hidden="true"><span>Goûter</span></div>
<div class="dock"><a class="pill out" href="{t}">Appeler</a><a class="pill" href="#resa">Réserver</a></div>
{TURBO}
'''
    tail = rep(tail, "var closed=t.getDay()===0||t.getDay()===1;", "var closed=false;")
    tail = rep(tail, "if(scrollY>innerHeight*1.4&&tb)tb.classList.add('on');", "if(scrollY>innerHeight*2&&tb&&!tb._s){tb._s=1;tb.classList.add('on');if(innerWidth<901)setTimeout(function(){tb.classList.remove('on')},6000);}")
    tail = tail.replace("'ellipse(8% 20% at 50% 52%)'", "'ellipse('+OS+' at '+OV+')'").replace("'ellipse(0% 0% at 50% 52%)'", "'ellipse(0% 0% at '+OV+')'")
    tail = rep(tail, ".to('#cap',{className:'cap light',duration:.01},.45);", ".to('#cap',{className:'cap light',duration:.01},innerWidth<901?.12:.45);")
    tail = "<script>var OV=innerWidth<901?'50% 30%':'50% 52%',OS=innerWidth<901?'8% 16%':'8% 20%';</script>\n" + tail
    head = head.replace('</style>', '@media (max-width:900px){.oval .img{clip-path:ellipse(8% 16% at 50% 30%)}.word{position:absolute;top:calc(30% - .4em);left:0;right:0;justify-content:center}}</style>')
    tail = rep(tail, "Sur le vrai site, la demande arriverait au restaurant et vous recevriez un SMS.", "Sur le vrai site, la demande arriverait directement au restaurant.")
    return head + body + tail, 'table-ruelle'

def institut(c):
    head, tail = head_tail(PREM + '/atelier-nacre/index.html', c)
    t = telh(c['tel'])
    imgs = [('cabine', 900, 1200), ('masque', 800, 1000), ('soin', 800, 1000)]
    steps = ''.join(f'''<article class="step" data-i="{i}" data-l="{e(s[0])}">
        <div class="mob"><img src="img/{imgs[i][0]}.webp" alt="Photo d'illustration" width="{imgs[i][1]}" height="{imgs[i][2]}" loading="lazy"></div>
        <span class="n">{["i.","ii.","iii."][i]} {e(s[0])}</span><h3>{e(s[1])}</h3><p>{e(s[2])}</p></article>''' for i, s in enumerate(c['univers']))
    acc = ''.join(f'''<div class="it{" open" if i == 0 else ""}"><button aria-expanded="{"true" if i == 0 else "false"}"><span class="no">{i+1:02d}</span><span><span class="nm">{e(r[0])}</span><span class="meta">{e(r[1])} · {e(r[2])}</span></span><span class="du">{e(r[1])}</span><span class="pr">{e(r[2])}</span><span class="pl" aria-hidden="true"></span></button>
        <div class="body"><div><div class="cnt"><span></span><p>{e(r[3])}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in r[4])}</ul><button class="btn go" data-r="{e(r[0])}" data-hov>Réserver ce soin</button></div></div></div></div>''' for i, r in enumerate(c['soins']))
    icons = ['<circle cx="22" cy="22" r="19"/><path d="M22 10v12l8 5"/>', '<rect x="9" y="6" width="26" height="32" rx="3"/><path d="M15 15h14M15 21h14M15 27h8"/>', '<path d="M22 38s-14-8.5-14-19a8 8 0 0 1 14-5 8 8 0 0 1 14 5c0 10.5-14 19-14 19z"/>']
    panes = ''.join(f'<div class="pane" data-tilt><svg viewBox="0 0 44 44" aria-hidden="true">{icons[i]}</svg><h3>{e(p[0])}</h3><p>{e(p[1])}</p></div>' for i, p in enumerate(c['panes']))
    body = f'''<body>
<header class="hd" id="hd">
  {banner(c)}
  <div class="bar">
    <a class="logo" href="#"><i></i>{e(c['logo'])}</a>
    <nav aria-label="Navigation principale"><a href="#gestes">L'institut</a><a href="#rituels">Les soins</a><a href="#cadeau">Offrir</a></nav>
    <a class="btn" href="#rdv" data-hov>Prendre rendez-vous</a>
  </div>
</header>
<main>
<section class="hero" aria-label="Accueil">
  <div class="fallback" aria-hidden="true"></div>
  <canvas id="gl" aria-hidden="true"></canvas>
  <div class="veil" aria-hidden="true"></div>
  <div class="in">
    <h1 aria-label="{e(c['h1_label'])}"><span class="ln"><span>{c['h1'][0]}</span></span><span class="ln"><span><em>{c['h1'][1]}</em></span></span></h1>
    <div class="side">
      <p class="k">{e(c['kicker'])}</p>
      <p>{e(c['hero_p'])}</p>
      <div class="cta"><a class="btn" href="#rdv" data-hov>Réserver un soin</a><a class="btn ghost" href="#rituels" data-hov>Voir les soins</a></div>
    </div>
  </div>
</section>
<section class="gestes w" id="gestes" aria-label="L'institut">
  <div class="intro"><h2>{c['univ_h2']}</h2><p>{e(c['univ_p'])}</p></div>
  <div class="gst">
    <div class="frame" id="frame" aria-hidden="true"><div class="tilt" id="tilt">
      <div class="ph"><img src="img/cabine.webp" alt="" width="900" height="1200"></div>
      <div class="ph"><img src="img/masque.webp" alt="" width="800" height="1000"></div>
      <div class="ph"><img src="img/soin.webp" alt="" width="800" height="1000"></div>
      <span class="lbl" id="lbl">{e(c['univers'][0][0])}</span>
    </div></div>
    <div class="steps">{steps}</div>
  </div>
</section>
<section class="rituels" id="rituels" aria-label="Les soins">
  <div class="w">
    <div class="top"><div><p class="k">Carte des soins</p><h2>Les <em>soins</em></h2></div><p>Durée et prix affichés pour chaque soin. Ouvrez-en un pour le détail, puis réservez-le directement.</p></div>
    <div class="acc" id="acc">{acc}</div>
    <p class="note">{e(c['note'])}</p>
  </div>
</section>
<section class="verre" aria-label="Pourquoi venir">
  <div class="blob b1" aria-hidden="true"></div><div class="blob b2" aria-hidden="true"></div>
  <div class="w"><p class="k">Pourquoi venir ici</p><h2>{c['verre_h2']}</h2><div class="panes">{panes}</div></div>
</section>
<section class="rdv w" id="rdv" aria-label="Prendre rendez-vous">
  <div class="head"><h2>Votre <em>rendez-vous</em>, en trois choix.</h2><p>Choisissez un soin, un jour et une heure, directement sur votre site, sans passer par une plateforme.</p></div>
  <p class="lab">1 · Le soin</p><div class="chips" id="rit"></div>
  <p class="lab">2 · Le jour</p><div class="days" id="days" aria-label="Choisir un jour"></div>
  <p class="lab">3 · L'heure</p><div class="chips slots" id="slots"></div>
  <div class="sheet" id="sheet" aria-live="polite"><span class="sum" id="sum"></span><button class="btn" id="ok" data-hov>Confirmer le rendez-vous</button></div>
  <div class="done" id="done" aria-live="polite"><h3>C'est noté, <em>à bientôt.</em></h3><p id="doneTxt"></p><p style="margin-top:10px;font-size:13px">Démonstration : aucun rendez-vous n'est réellement enregistré.</p></div>
</section>
<section class="cadeau w" id="cadeau" aria-label="Carte cadeau">
  <div class="grid">
    <div class="stagec"><div class="card" id="card">
      <div class="f"><div class="t1">{e(c['logo'])}</div><div class="t2"><span>Carte cadeau</span><span class="v">{e(c['gift'])}</span></div></div>
      <div class="b"><div class="t1">Pour vous</div><div class="t2"><span>{e(c['gift_soin'])}</span><span>Mulhouse</span></div></div>
    </div></div>
    <div><p class="k">Offrir</p><h2>Un soin, <em>plutôt qu'un objet.</em></h2><p>Avec votre site, vos clientes pourraient offrir un soin en carte cadeau, achetée en ligne et envoyée par e-mail.</p><a class="btn" href="#rdv" data-hov>Offrir un soin</a></div>
  </div>
</section>
</main>
<footer class="ft">
  <div class="w">
    <p class="big">{c['ft_big']}</p>
    <div class="cols">
      <div><h4>Venir</h4>{e(c['addr'])}<br>68100 Mulhouse</div>
      <div><h4>Horaires</h4>{c['hours']}</div>
      <div><h4>Contact</h4><a href="{t}">{c['tel']}</a><br>Rendez-vous en ligne</div>
      <div><h4>Avis</h4>{e(c['avis'])}</div>
    </div>
    <div class="cp"><span>{e(c['name'])} · maquette de démonstration non officielle</span><span>Conçu par <a href="https://agenceturbo.fr" style="text-decoration:underline">Agence Turbo</a></span></div>
  </div>
</footer>
<div class="dock"><a class="btn ghost" href="{t}">Appeler</a><a class="btn" href="#rdv">Rendez-vous</a></div>
{TURBO}
<div class="ring" id="ring" aria-hidden="true"></div>
'''
    R = json.dumps([r[0] for r in c['soins']], ensure_ascii=False); S = json.dumps(c['slots'], ensure_ascii=False)
    tail = rep(tail, "var R=['Éclat express','Rituel nacre','Peau sensible','Dos et épaules'],S=['9 h 30','10 h 30','11 h 45','14 h 00','15 h 15','16 h 30','17 h 45'];", f"var R={R},S={S};")
    tail = rep(tail, "var st={r:R[1],", "var st={r:R[0],")
    tail = rep(tail, "if(scrollY>innerHeight*1.2&&tb)tb.classList.add('on');", "if(scrollY>innerHeight*2&&tb&&!tb._s){tb._s=1;tb.classList.add('on');if(innerWidth<981)setTimeout(function(){tb.classList.remove('on')},6000);}")
    tail = rep(tail, "if(w===0||w===1){b.disabled=true;", "if(w===0){b.disabled=true;")
    return head + body + tail, 'atelier-nacre'

def build(c):
    page, demo = (resto if c['kind'] == 'resto' else institut)(c)
    out = f"{ROOT}/{c['id']}-{c['slug']}"
    os.makedirs(out, exist_ok=True)
    for sub in ('img', 'fonts'):
        if os.path.isdir(f'{out}/{sub}'): shutil.rmtree(f'{out}/{sub}')
        shutil.copytree(f'{PREM}/{demo}/{sub}', f'{out}/{sub}')
    open(out + '/index.html', 'w').write(page)
    print(out)

if __name__ == '__main__':
    for f in sys.argv[1:]: build(json.load(open(f)))
