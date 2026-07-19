# -*- coding: utf-8 -*-
import glob

files = glob.glob('c:/Users/Asus/Downloads/gic/ui-design/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('padding: 48px 0 80px;', 'padding-top: 48px; padding-bottom: 80px;')
    
    if content != new_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
