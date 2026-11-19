// menu toggle, scroll reveal, photo lightbox, publication filters
(function(){
  var d=document,b=d.querySelector('.burger'),m=d.querySelector('.menu'),n=d.querySelector('.nav');
  if(b&&m&&n){
    var set=function(o){m.classList.toggle('open',o);b.setAttribute('aria-expanded',o)};
    b.addEventListener('click',function(){set(!m.classList.contains('open'))});
    d.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){set(false);b.focus()}});
    n.addEventListener('focusout',function(e){if(e.relatedTarget&&!n.contains(e.relatedTarget))set(false)});
    d.addEventListener('click',function(e){if(!n.contains(e.target))set(false)});
  }
  var y=d.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
  // reveal: hide only what is below the fold, and only once this script is running
  var els=d.querySelectorAll('.reveal');
  if('IntersectionObserver' in window&&els.length){
    var h=window.innerHeight;
    els.forEach(function(e){if(e.getBoundingClientRect().top<h)e.classList.add('in')});
    d.documentElement.classList.add('js');
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(e){if(!e.classList.contains('in'))io.observe(e)});
  }
  // photo lightbox: links with class "lb" open the larger photo in a dialog; arrows step through the page's photos
  var lbs=[].slice.call(d.querySelectorAll('a.lb'));
  if(lbs.length&&window.HTMLDialogElement){
    var dl=d.createElement('dialog');dl.className='lightbox';dl.setAttribute('aria-label','Photo viewer');
    dl.innerHTML='<button type="button" class="lb-x" aria-label="Close">&times;</button><button type="button" class="lb-p" aria-label="Previous photo">&#8249;</button><figure><img alt=""></figure><button type="button" class="lb-n" aria-label="Next photo">&#8250;</button>';
    d.body.appendChild(dl);
    var im=dl.querySelector('img'),cur=0;
    var show=function(i){cur=(i+lbs.length)%lbs.length;var a=lbs[cur];im.src=a.getAttribute('href');im.alt=a.querySelector('img').alt};
    lbs.forEach(function(a,i){a.addEventListener('click',function(e){e.preventDefault();show(i);dl.showModal()})});
    dl.querySelector('.lb-x').addEventListener('click',function(){dl.close()});
    dl.querySelector('.lb-p').addEventListener('click',function(){show(cur-1)});
    dl.querySelector('.lb-n').addEventListener('click',function(){show(cur+1)});
    dl.addEventListener('click',function(e){if(e.target===dl)dl.close()});
    dl.addEventListener('keydown',function(e){if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1)});
  }
  // publication filters: publications.html#nitrogen opens with that filter on
  var fb=d.querySelectorAll('.filters button'),out=d.getElementById('pubcount');
  if(!fb.length)return;
  var apply=function(t){
    var shown=0,label='';
    fb.forEach(function(x){var on=x.dataset.f===t;x.classList.toggle('on',on);x.setAttribute('aria-pressed',on);if(on)label=x.textContent});
    d.querySelectorAll('.pgroup').forEach(function(g){
      var c=0;
      g.querySelectorAll('.pub').forEach(function(p){
        var ok=t==='all'||(' '+p.dataset.tags+' ').indexOf(' '+t+' ')>-1;
        p.hidden=!ok;if(ok)c++});
      g.hidden=!c;shown+=c});
    if(out)out.textContent=shown+(shown===1?' publication':' publications')+(t==='all'?'':' on '+label.toLowerCase());
  };
  fb.forEach(function(x){x.addEventListener('click',function(){
    apply(x.dataset.f);
    try{history.replaceState(null,'',x.dataset.f==='all'?location.pathname:'#'+x.dataset.f)}catch(e){}
  })});
  var k=location.hash.slice(1);
  apply(/^[a-z]+$/.test(k)&&d.querySelector('.filters [data-f="'+k+'"]')?k:'all');
})();
