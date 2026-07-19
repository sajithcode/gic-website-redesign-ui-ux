# -*- coding: utf-8 -*-
import glob

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

files = glob.glob('c:/Users/Asus/Downloads/gic/ui-design/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '.mobile-menu-btn { display: none;' not in content:
        # We need to insert the CSS right before </style>
        content = content.replace('</style>', css_addition + '\n</style>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
