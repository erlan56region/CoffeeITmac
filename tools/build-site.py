#!/usr/bin/env python3
"""Собирает index.html (сайт) из исходной статьи macos-history.html.

Что добавляет:
  * мета-описание, Open Graph, favicon;
  * лайтбокс — клик по скриншоту открывает его в полном размере;
  * кнопку «наверх»;
  * строку с источниками изображений в футере.
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "macos-history.html"
dst = root / "index.html"
html = src.read_text(encoding="utf-8")

FAVICON = (
    '<link rel="icon" href="data:image/svg+xml,'
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
    "%3Crect width='100' height='100' rx='22' fill='%231d1d1f'/%3E"
    "%3Ccircle cx='50' cy='50' r='26' fill='%230071e3'/%3E"
    "%3C/svg%3E\">"
)

META = (
    '<meta name="description" content="История macOS по годам: System 1.0 (1984), System 6–7, Mac OS 8–9, '
    'Mac OS X Cheetah–Snow Leopard, OS X Lion–Mavericks, macOS Yosemite–Sequoia (2024). Со скриншотами каждой версии.">\n'
    '<meta property="og:type" content="article">\n'
    '<meta property="og:title" content="Версии macOS по годам: от System 1.0 (1984) до macOS Sequoia (2024)">\n'
    '<meta property="og:description" content="Весь путь операционной системы Apple — со скриншотами каждой эпохи.">\n'
    '<meta property="og:locale" content="ru_RU">\n'
    '<meta name="theme-color" content="#1d1d1f">\n'
    + FAVICON + "\n"
)

CSS = """
  /* ---------- ЛАЙТБОКС ---------- */
  .slider .slide img{cursor:zoom-in;}
  #lightbox{position:fixed;inset:0;z-index:200;display:none;align-items:center;justify-content:center;
            background:rgba(10,10,12,.93);padding:24px;}
  #lightbox.open{display:flex;}
  #lightbox figure{max-width:min(1200px,96vw);max-height:92vh;display:flex;flex-direction:column;
                   gap:12px;align-items:center;}
  #lightbox img{max-width:100%;max-height:80vh;border-radius:10px;background:#000;
                box-shadow:0 24px 70px rgba(0,0,0,.65);}
  #lightbox figcaption{color:#d6d6d8;font-size:14px;text-align:center;max-width:760px;}
  #lightbox .hint{position:absolute;top:18px;right:24px;color:#a1a1a6;font-size:12px;
                  letter-spacing:.12em;text-transform:uppercase;}
  #lightbox .close{position:absolute;top:14px;left:18px;width:40px;height:40px;border:none;
                   border-radius:50%;background:rgba(255,255,255,.14);color:#fff;font-size:22px;
                   line-height:1;cursor:pointer;}
  #lightbox .close:hover{background:rgba(255,255,255,.26);}

  /* ---------- КНОПКА «НАВЕРХ» ---------- */
  #toTop{position:fixed;right:22px;bottom:22px;z-index:150;width:46px;height:46px;border:none;
         border-radius:50%;background:rgba(255,255,255,.92);color:#1d1d1f;font-size:18px;
         cursor:pointer;box-shadow:0 6px 20px rgba(0,0,0,.18);backdrop-filter:blur(10px);
         opacity:0;pointer-events:none;transition:opacity .3s, transform .3s;}
  #toTop.show{opacity:1;pointer-events:auto;}
  #toTop:hover{transform:translateY(-2px);}

  footer .credits{max-width:680px;margin:10px auto 0;font-size:12.5px;color:#8e8e93;line-height:1.5;}

  @media print{ #toTop, #lightbox{display:none !important;} }
"""

LIGHTBOX_HTML = """
<div id="lightbox" role="dialog" aria-modal="true" aria-label="Просмотр скриншота">
  <button class="close" aria-label="Закрыть">×</button>
  <span class="hint">клик или Esc — закрыть</span>
  <figure>
    <img alt="">
    <figcaption></figcaption>
  </figure>
</div>

<button id="toTop" aria-label="Наверх" title="Наверх">↑</button>
"""

JS = """
<script>
/* Лайтбокс для скриншотов */
(function(){
  var box = document.getElementById('lightbox');
  if (!box) return;
  var big = box.querySelector('img');
  var cap = box.querySelector('figcaption');

  document.querySelectorAll('.slider .slide img').forEach(function(el){
    el.addEventListener('click', function(){
      big.src = el.currentSrc || el.src;
      big.alt = el.alt || '';
      cap.textContent = el.alt || '';
      box.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function close(){
    box.classList.remove('open');
    big.removeAttribute('src');
    document.body.style.overflow = '';
  }
  box.addEventListener('click', function(e){
    if (e.target === box || e.target.classList.contains('close')) close();
  });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape') close();
    if (!box.classList.contains('open')) return;
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft'){
      var all = Array.prototype.slice.call(document.querySelectorAll('.slider .slide img'));
      var i = all.indexOf(document.querySelector('.slider .slide img[src="' + big.getAttribute('src') + '"]'));
      if (i === -1) return;
      var next = all[(i + (e.key === 'ArrowRight' ? 1 : all.length - 1)) % all.length];
      big.src = next.currentSrc || next.src; big.alt = next.alt || ''; cap.textContent = next.alt || '';
    }
  });
})();

/* Кнопка «наверх» */
(function(){
  var btn = document.getElementById('toTop');
  window.addEventListener('scroll', function(){
    btn.classList.toggle('show', window.scrollY > 700);
  }, {passive:true});
  btn.addEventListener('click', function(){
    window.scrollTo({top:0, behavior:'smooth'});
  });
})();
</script>
"""

CREDITS = (
    '<div class="credits">Скриншоты и обои: Wikimedia Commons, 512 Pixels, OSXDaily, Ars Technica, '
    'Apple Newsroom, VersionMuseum, PCMag, iMore, Cult of Mac, blog.alexseifert.com — в учебных целях.</div>'
)

assert "<title>" in html
html = html.replace("</title>\n", "</title>\n" + META, 1)
assert "</style>" in html
html = html.replace("</style>", CSS + "</style>", 1)
assert "</footer>" in html
html = html.replace("</footer>", CREDITS + "\n</footer>", 1)
assert "</body>" in html
html = html.replace("</body>", LIGHTBOX_HTML + JS + "\n</body>", 1)

dst.write_text(html, encoding="utf-8")
print(f"готово: {dst.relative_to(root)} ({len(html.encode('utf-8'))/1024:.0f} КБ)")
