// menu toggle, scroll reveal, publication filters
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
