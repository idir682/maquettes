
(function(){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine=matchMedia('(pointer: fine)').matches;
  var d=document,$=function(s,c){return (c||d).querySelector(s)},$$=function(s,c){return [].slice.call((c||d).querySelectorAll(s))};

  /* ---- grille de tuiles du héros ---- */
  var tiles=$('#tiles'),C=innerWidth<700?5:10,R=innerWidth<700?8:6;
  tiles.style.setProperty('--c',C);tiles.style.setProperty('--r',R);
  for(var y=0;y<R;y++)for(var x=0;x<C;x++){var i=d.createElement('i');i.style.backgroundPosition=(x/(C-1)*100)+'% '+(y/(R-1)*100)+'%';i.dataset.x=x;i.dataset.y=y;tiles.appendChild(i);}

  /* ---- interactions du devis (toujours actives) ---- */
  function group(g,cb){$$('[data-g='+g+'] button').forEach(function(b){b.addEventListener('click',function(){$$('[data-g='+g+'] button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});cb(b.dataset.v);});});}
  function bump(el){el.textContent=el.textContent;if(!reduce&&window.gsap)gsap.fromTo(el,{y:10,opacity:0},{y:0,opacity:1,duration:.5,ease:'power3.out'});}
  group('type',function(v){var e=$('#tType');e.textContent=v;bump(e);});
  group('sit',function(v){var e=$('#tSit');e.textContent=v;bump(e);});
  var surf=$('#surf');function sv(){var p=(surf.value-surf.min)/(surf.max-surf.min)*100;surf.style.setProperty('--p',p+'%');$('#surfO').innerHTML=surf.value+'<small>m²</small>';$('#tSurf').textContent=surf.value+' m²';}
  surf.addEventListener('input',sv);sv();
  $('#send').addEventListener('click',function(){$('#done').hidden=false;bump($('#done'));});
  $$('details').forEach(function(dt){dt.addEventListener('toggle',function(){if(dt.open&&!reduce&&window.gsap)gsap.from($('.a',dt),{height:0,duration:.6,ease:'power3.out'});});});

  /* ---- en-tête et encart Agence Turbo ---- */
  var hd=$('#hd'),tb=$('#turbo');
  function onS(){hd.classList.toggle('solid',scrollY>60);if(scrollY>innerHeight*2&&tb&&!tb._s){tb._s=1;tb.classList.add('on');if(innerWidth<981)setTimeout(function(){tb.classList.remove('on')},6000);}}
  addEventListener('scroll',onS,{passive:true});onS();

  if(reduce||!window.gsap){$$('.step').forEach(function(s){s.classList.add('on')});$$('#towns span').forEach(function(s){s.classList.add('on')});staticRain();return;}

  gsap.registerPlugin(ScrollTrigger);

  /* défilement doux */
  var lenis=new Lenis({lerp:.1,smoothWheel:true});
  lenis.on('scroll',ScrollTrigger.update);
  gsap.ticker.add(function(t){lenis.raf(t*1000)});gsap.ticker.lagSmoothing(0);
  $$('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){var t=a.getAttribute('href');if(t.length>1&&$(t)){e.preventDefault();lenis.scrollTo(t,{offset:-70,duration:1.4});}});});

  /* entrée : les tuiles se posent du faîtage vers le bas, puis le titre monte ligne à ligne */
  var tl=gsap.timeline({defaults:{ease:'expo.out'}});
  tl.from('#tiles i',{rotateX:-92,opacity:0,duration:1.1,stagger:{grid:[R,C],from:'start',axis:'y',amount:.9}})
    .from('#h1 .ln>span',{yPercent:110,duration:1.2,stagger:.09},'-=.55')
    .from('[data-in]',{y:24,opacity:0,duration:1,stagger:.08},'-=.8')
    .from('#hd .w',{y:-30,opacity:0,duration:1},'-=1');
  /* parallaxe du héros à la sortie */
  gsap.to('#tiles',{yPercent:18,scale:1.06,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  gsap.to('#h1',{yPercent:-30,opacity:.2,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});

  /* anatomie : chaque couche se dessine au défilement */
  var layers=$$('#cut .ly'),steps=$$('.step');
  layers.forEach(function(g){$$('path',g).forEach(function(p){var L=p.getTotalLength()||1;if(!p.getAttribute('stroke-dasharray')){p.style.strokeDasharray=L;p.style.strokeDashoffset=L;}else{p.style.opacity=0;}});});
  function draw(i,on){var g=layers[i];$$('path',g).forEach(function(p){if(p.getAttribute('stroke-dasharray'))gsap.to(p,{opacity:on?1:0,duration:.6});else gsap.to(p,{strokeDashoffset:on?0:p.getTotalLength(),duration:1.1,ease:'power2.inOut'});});steps[i].classList.toggle('on',on||i===0);}
  var mm=gsap.matchMedia();
  mm.add('(min-width: 981px)',function(){
    var st=ScrollTrigger.create({trigger:'.anat',start:'top top',end:'+=220%',pin:true,scrub:true,onUpdate:function(s){var n=Math.min(4,Math.floor(s.progress*5.2));layers.forEach(function(_,i){var on=i<=n;if(layers[i]._on!==on){layers[i]._on=on;draw(i,on);}});}});
    /* services : rail horizontal épinglé */
    var rail=$('#rail');
    var tw=gsap.to(rail,{x:function(){return -(rail.scrollWidth-innerWidth)},ease:'none',scrollTrigger:{trigger:'.sv',start:'top top',end:function(){return '+='+(rail.scrollWidth-innerWidth)},pin:true,scrub:1,invalidateOnRefresh:true}});
    $$('.card').forEach(function(c){gsap.to($('img',c),{scale:1,ease:'none',scrollTrigger:{trigger:c,containerAnimation:tw,start:'left right',end:'right left',scrub:true}});});
    return function(){st.kill();};
  });
  mm.add('(max-width: 980px)',function(){
    steps.forEach(function(s,i){ScrollTrigger.create({trigger:s,start:'top 75%',onEnter:function(){layers.slice(0,i+1).forEach(function(_,k){if(!layers[k]._on){layers[k]._on=true;draw(k,true);}});}});});
    $('#rail').style.cssText='flex-direction:column;width:auto;padding-inline:var(--gut)';
    $$('.card').forEach(function(c){c.style.width='100%';gsap.fromTo($('img',c),{scale:1.25},{scale:1,ease:'none',scrollTrigger:{trigger:c,start:'top bottom',end:'bottom top',scrub:true}});});
  });

  /* titres de section : montée mot à mot */
  $$('.anat h2,.sv h2,.devis h2,.faq h2').forEach(function(h){
    var html=h.innerHTML.replace(/(<em>)?([^<\s]+)(<\/em>)?/g,function(m,a,w,b){return '<span style="display:inline-block;overflow:hidden;vertical-align:top"><span style="display:inline-block">'+(a||'')+w+(b||'')+'</span></span>';});
    h.innerHTML=html;
    gsap.from($$(':scope>span>span',h),{yPercent:105,duration:1.1,ease:'expo.out',stagger:.06,scrollTrigger:{trigger:h,start:'top 85%'}});
  });
  gsap.from('.q,.ticket',{y:40,opacity:0,duration:1,ease:'expo.out',stagger:.1,scrollTrigger:{trigger:'#form',start:'top 80%'}});

  /* orage : éclair à l'entrée de la section */
  ScrollTrigger.create({trigger:'.storm',start:'top 60%',onEnter:function(){gsap.timeline().to('#flash',{opacity:.9,duration:.06}).to('#flash',{opacity:0,duration:.12}).to('#flash',{opacity:.6,duration:.05,delay:.08}).to('#flash',{opacity:0,duration:.6});}});
  gsap.from('#stormT',{y:60,opacity:0,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:'.storm',start:'top 70%'}});

  /* communes allumées une à une */
  gsap.to({},{scrollTrigger:{trigger:'.zone',start:'top 70%',end:'bottom 60%',scrub:true,onUpdate:function(s){var t=$$('#towns span'),n=Math.round(s.progress*t.length);t.forEach(function(e,i){e.classList.toggle('on',i<n)});}}});

  /* signature géante du pied de page */
  gsap.from('#big span',{yPercent:100,duration:1.2,ease:'expo.out',stagger:.06,scrollTrigger:{trigger:'#big',start:'top 95%'}});

  /* boutons aimantés */
  if(fine)$$('[data-mag]').forEach(function(b){b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect();gsap.to(b,{x:(e.clientX-r.left-r.width/2)*.25,y:(e.clientY-r.top-r.height/2)*.35,duration:.4,ease:'power3.out'});});b.addEventListener('mouseleave',function(){gsap.to(b,{x:0,y:0,duration:.8,ease:'elastic.out(1,.4)'});});});

  /* pluie en canvas, seulement quand la section est visible */
  var cv=$('#rain'),cx=cv.getContext('2d'),drops=[],run=false,W,H;
  function size(){W=cv.width=cv.offsetWidth*devicePixelRatio;H=cv.height=cv.offsetHeight*devicePixelRatio;drops=[];var n=Math.round(W*H/9000);for(var k=0;k<n;k++)drops.push({x:Math.random()*W,y:Math.random()*H,l:10+Math.random()*26,v:9+Math.random()*12,o:.08+Math.random()*.3});}
  function frame(){if(!run)return;cx.clearRect(0,0,W,H);cx.lineWidth=devicePixelRatio;for(var k=0;k<drops.length;k++){var p=drops[k];cx.strokeStyle='rgba(201,207,212,'+p.o+')';cx.beginPath();cx.moveTo(p.x,p.y);cx.lineTo(p.x-p.l*.18,p.y+p.l);cx.stroke();p.y+=p.v*devicePixelRatio;p.x-=p.v*.18;if(p.y>H){p.y=-p.l;p.x=Math.random()*W*1.1;}}requestAnimationFrame(frame);}
  size();addEventListener('resize',size);
  ScrollTrigger.create({trigger:'.storm',start:'top bottom',end:'bottom top',onToggle:function(s){run=s.isActive;if(run)frame();}});
  function staticRain(){}
})();
