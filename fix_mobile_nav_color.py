# -*- coding: utf-8 -*-
import glob

files = glob.glob('c:/Users/Asus/Downloads/gic/ui-design/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_css = ".nav-dropdown { position: static; box-shadow: none; min-width: 100%; padding: 0 10px; display: none; background: rgba(0,0,0,0.1); border-radius: 0; }"
    new_css = ".nav-dropdown { position: static; box-shadow: none; min-width: 100%; padding: 0 10px; display: none; background: rgba(0,0,0,0.1); border-radius: 0; }\n  .nav-dropdown li a { color: #fff; }\n  .nav-dropdown li a:hover { background: rgba(255,255,255,0.1); color: #fff; }"
    
    new_content = content.replace(old_css, new_css)
    
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
