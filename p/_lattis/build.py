# Maquettes prospects dans le style de la démo validée « Lattis Couverture » (24/10/2026).
# CSS et JS repris tels quels (base.css / base.js) ; seuls textes, photos et couleur d'accent changent.
import json, os, shutil, sys, html
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(H)
LATTIS = os.path.join(os.path.dirname(ROOT), 'premium', 'lattis-couverture')
e = html.escape

def build(c):
    out = f"{ROOT}/{c['id']}-{c['slug']}"
    os.makedirs(out + '/img', exist_ok=True)
    if os.path.isdir(out + '/fonts'): shutil.rmtree(out + '/fonts')
    shutil.copytree(LATTIS + '/fonts', out + '/fonts')
    imgs = {c['hero_img']} | {k['img'] for k in c['cards']}
    for k in imgs: shutil.copy(f'{ROOT}/_img/{k}.webp', f'{out}/img/{k}.webp')
    a, ahi, rgb = c['acc'], c['acc_hi'], c['acc_rgb']
    css = open(H + '/base.css').read()
    css = (css.replace('--tuile:#c4532f', f'--tuile:{a}').replace('--tuile-hi:#d9643c', f'--tuile-hi:{ahi}')
              .replace('196,83,47', rgb).replace('url(img/toit.webp)', f"url(img/{c['hero_img']}.webp)"))
    for old, new in c.get('base', {}).items(): css = css.replace(old, new)
    css += '.cut .l4{stroke-linecap:butt}.hero{height:auto;min-height:100svh}.hero .w{height:auto;min-height:100svh;padding-top:150px}@media (max-width:980px){.hero .w{padding-top:140px}.ft .cols>div:first-child{grid-column:1/-1}}' + c.get('css', '')
    js = open(H + '/base.js').read()
    tel = c['tel']; telh = 'tel:+33' + tel.replace(' ', '')[1:]
    logo_svg = c['logo_svg'].replace('ACC', a)
    logo = f'<svg viewBox="0 0 40 40" aria-hidden="true">{logo_svg}</svg>{e(c["short"])}'
    band = ''.join(f'<span>{e(w)}</span>' for w in c['band'] * 2)
    h1 = ''.join(f'<span class="ln"><span>{l}</span></span>' for l in c['h1'])
    h1_label = e(c['h1_label'])
    steps = ''.join(f'<div class="step{" on" if i == 0 else ""}"><b>{i+1}</b><h3>{e(t)}</h3><p>{e(p)}</p></div>' for i, (t, p) in enumerate(c['steps']))
    cards = ''.join(f'<article class="card"><div class="ph"><span class="n">{i+1:02d}</span><img src="img/{k["img"]}.webp" alt="{e(k["alt"])}" loading="lazy"></div><h3>{e(k["t"])}</h3><p>{e(k["p"])}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in k["li"])}</ul></article>' for i, k in enumerate(c['cards']))
    opts = ''.join(f'<button type="button" class="opt" aria-pressed="{"true" if i == 0 else "false"}" data-v="{e(v)}"><svg viewBox="0 0 46 30">{svg}</svg><span>{e(v)}</span></button>' for i, (v, svg) in enumerate(c['opts']))
    chips = ''.join(f'<button type="button" class="chip" aria-pressed="{"true" if i == 0 else "false"}" data-v="{e(v)}">{e(v)}</button>' for i, v in enumerate(c['chips']))
    towns = ''.join(f'<span>{e(t)}</span>' for t in c['towns'])
    faq = ''.join(f'<details><summary>{e(q)}</summary><div class="a"><p>{e(r)}</p></div></details>' for q, r in c['faq'])
    big = ''.join(f'<span>{e(ch)}</span>' for ch in c['big'])
    nav = ''.join(f'<a href="#{h}">{e(t)}</a>' for h, t in c['nav'])
    page = f'''<!doctype html>
<html lang="fr" data-hubspot-id="{c['id']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(c['title'])}</title>
<meta name="description" content="Maquette proposée par Agence Turbo à {e(c['name'])}. Ce n'est pas le site officiel de l'entreprise.">
<meta name="robots" content="noindex">
<link rel="preload" href="fonts/bigshoulders-normal-500-900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="fonts/bigshoulders.css">
<link rel="stylesheet" href="fonts/manrope.css">
<style>{css}</style>
</head>
<body>
<header class="hd" id="hd"><div class="demo">Maquette proposée par Agence Turbo à {e(c['name'])}. Ce n'est pas le site officiel de l'entreprise.</div><div class="w">
  <a class="logo" href="#top" aria-label="{e(c['name'])}, accueil">{logo}</a>
  <nav class="nav" aria-label="Navigation">{nav}</nav>
  <a class="urg" href="{telh}"><i></i>{tel}</a>
  <a class="btn go" href="#devis" data-mag><span>{e(c['cta_head'])}</span></a>
</div></header>

<main id="top">
<section class="hero" aria-label="Accueil">
  <div class="tiles" id="tiles" aria-hidden="true"></div>
  <div class="w">
    <p class="k" data-in><b>●</b>&nbsp; {e(c['kicker'])}</p>
    <h1 id="h1" aria-label="{h1_label}">{h1}</h1>
    <div class="row">
      <p data-in>{e(c['hero_p'])}</p>
      <div class="acts" data-in><a class="btn go" href="#devis" data-mag><span>{e(c['cta1'])}</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a><a class="btn ghost" href="#orage"><span>{e(c['cta2'])}</span></a></div>
    </div>
  </div>
  <div class="scroll" aria-hidden="true">Défiler</div>
</section>

<div class="band" aria-hidden="true"><div class="tr">{band}</div></div>

<section class="anat" id="anatomie">
  <div class="w">
    <div>
      <p class="k" style="margin-bottom:22px"><b>01</b>&nbsp; {e(c['anat_k'])}</p>
      <h2 style="margin-bottom:40px">{c['anat_h2']}</h2>
      <svg class="cut" id="cut" viewBox="0 0 640 400" role="img" aria-label="{e(c['anat_label'])}">{c['anat_svg'].replace('ACC', a)}</svg>
    </div>
    <div class="steps" id="steps">{steps}</div>
  </div>
</section>

<section class="sv" id="services">
  <div class="w head">
    <div><p class="k" style="margin-bottom:22px"><b>02</b>&nbsp; Prestations</p><h2>{c['sv_h2']}</h2></div>
    <p>{e(c['sv_p'])}</p>
  </div>
  <div class="rail" id="rail">{cards}</div>
</section>

<section class="storm" id="orage">
  <canvas id="rain" aria-hidden="true"></canvas>
  <div class="flash" id="flash" aria-hidden="true"></div>
  <div class="w">
    <p class="k"><b>03</b>&nbsp; {e(c['storm_k'])}</p>
    <h2 id="stormT">{c['storm_h2']}</h2>
    <p>{e(c['storm_p'])}</p>
    <div class="acts"><a class="btn go" href="{telh}" data-mag><span>Appeler le {tel}</span></a><a class="btn ghost" href="#devis"><span>{e(c['storm_cta2'])}</span></a></div>
  </div>
</section>

<section class="devis" id="devis">
  <div class="w">
    <div class="intro">
      <p class="k"><b>04</b>&nbsp; Devis</p>
      <h2>Trois questions, <em>un rappel.</em></h2>
      <p>{e(c['devis_p'])}</p>
    </div>
    <form id="form" novalidate onsubmit="return false">
      <div class="q"><h3><small>01</small>{e(c['q1'])}</h3><div class="opts" data-g="type">{opts}</div></div>
      <div class="q"><h3><small>02</small>Surface du logement</h3>
        <div class="range"><output id="surfO">120<small>m²</small></output><input id="surf" type="range" min="20" max="400" step="10" value="120" aria-label="Surface du logement en mètres carrés"></div>
      </div>
      <div class="q"><h3><small>03</small>{e(c['q3'])}</h3><div class="chips" data-g="sit">{chips}</div></div>
      <div class="ticket" aria-live="polite">
        <div class="tt"><b>Votre demande</b><span>Démonstration</span></div>
        <dl><dt>{e(c['t1'])}</dt><dd id="tType">{e(c['opts'][0][0])}</dd><dt>Surface</dt><dd id="tSurf">120 m²</dd><dt>Besoin</dt><dd id="tSit">{e(c['chips'][0])}</dd></dl>
        <button class="btn go" type="button" id="send"><span>Être rappelé</span></button>
        <p class="done" id="done" hidden>Démonstration : sur le vrai site, la demande arriverait chez {e(c['short'])} par e-mail.</p>
      </div>
    </form>
  </div>
</section>

<section class="zone" id="zone">
  <div class="w">
    <p class="k"><b>05</b>&nbsp; Secteur</p>
    <div class="towns" id="towns">{towns}</div>
  </div>
</section>

<section class="faq">
  <div class="w">
    <h2>Avant <em>d'appeler.</em></h2>
    <div>{faq}</div>
  </div>
</section>
</main>

<footer class="ft">
  <div class="w">
    <div class="cols">
      <div><a class="logo" href="#top">{logo}</a><p style="margin-top:14px;max-width:32ch;line-height:1.6">{e(c['ft_about'])}</p></div>
      <div><h4>Contact</h4><a href="{telh}">{tel}</a><a href="#devis">Demande de devis</a></div>
      <div><h4>Prestations</h4>{''.join(f'<a href="#services">{e(k["t"])}</a>' for k in c['cards'][:3])}</div>
      <div><h4>Adresse</h4>{''.join(f'<p>{e(l)}</p>' for l in c['addr'])}</div>
    </div>
  </div>
  <div class="big" id="big" aria-hidden="true">{big}</div>
  <div class="w"><div class="cp"><span>{e(c['name'])} · maquette de démonstration non officielle</span><span>Conçu par <a href="https://agenceturbo.fr">Agence Turbo</a></span></div></div>
</footer>

<div class="dock"><a class="btn ghost" href="{telh}"><span>Appeler</span></a><a class="btn go" href="#devis"><span>Devis</span></a></div>
<div class="turbo" id="turbo"><div><b>Ce site peut être le vôtre</b>Maquette Agence Turbo. <a href="mailto:contact@agenceturbo.fr">contact@agenceturbo.fr</a></div><button aria-label="Fermer" onclick="this.parentNode.remove()">×</button></div>

<script src="../../lib/gsap.min.js"></script>
<script src="../../lib/ScrollTrigger.min.js"></script>
<script src="../../lib/lenis.min.js"></script>
<script>{js}</script>
</body>
</html>
'''
    open(out + '/index.html', 'w').write(page)
    print(out)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        build(json.load(open(f)))
