// menu toggle, scroll reveal, publication filters
(function(){
  var b=document.querySelector('.burger'),m=document.querySelector('.menu');
  if(b&&m)b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(e){io.observe(e)});
  } else els.forEach(function(e){e.classList.add('in')});
  var fb=document.querySelectorAll('.filters button');
  fb.forEach(function(btn){btn.addEventListener('click',function(){
    fb.forEach(function(x){x.classList.remove('on')});btn.classList.add('on');
    var t=btn.dataset.f;
    document.querySelectorAll('.pub').forEach(function(p){p.style.display=(t==='all'||p.dataset.tags.indexOf(t)>-1)?'':'none'});
  })});
})();
