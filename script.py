# -*- coding: utf-8 -*-
import os, glob, re

css_addition = '''
/* --- Mobile Nav --- */
.mobile-menu-btn { display: none; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,.3); padding: 6px 12px; border-radius: 4px; font-size: 1rem; cursor: pointer; }
@media (max-width: 768px) {
  .main-nav .container { justify-content: space-between; align-items: center; padding: 10px 24px; flex-wrap: wrap; }
  .mobile-menu-btn { display: block; }
  .main-nav > .container > ul { display: none; width: 100%; flex-direction: column; padding-top: 10px; }
  .main-nav > .container > ul.mobile-open { display: flex; }
  .nav-dropdown { position: static; box-shadow: none; min-width: 100%; padding: 0 10px; display: none; background: rgba(0,0,0,0.1); border-radius: 0; }
  .main-nav > .container > ul > li > a { justify-content: space-between; }
}
'''

js_addition = '''
  // Mobile Nav Toggle
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const mainNavUl = document.querySelector('.main-nav > .container > ul');
  if (mobileBtn && mainNavUl) {
    mobileBtn.addEventListener('click', () => {
      mainNavUl.classList.toggle('mobile-open');
    });
  }
'''

files = glob.glob('c:/Users/Asus/Downloads/gic/ui-design/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '.mobile-menu-btn' not in content:
        # Add CSS
        content = re.sub(r'/\* ---------- Hero ---------- \*/', css_addition + r'\n/* ---------- Hero ---------- */', content)
        # Add HTML
        content = re.sub(r'<nav class="main-nav" aria-label="Primary">\s*<div class="container">\s*<ul>', '<nav class="main-nav" aria-label="Primary">\n    <div class="container">\n      <button class="mobile-menu-btn" aria-label="Toggle navigation">☰ Menu</button>\n      <ul>', content)
        # Add JS
        content = re.sub(r'  // No JS needed for dropdown — pure CSS :hover handles it', js_addition + r'\n  // No JS needed for dropdown — pure CSS :hover handles it', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
