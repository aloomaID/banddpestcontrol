import os
import shutil
from bs4 import BeautifulSoup
import random

def short_code_state(state_repl):
    search_categories = open("/var/www/html/howardskeyandlock/duplicatescript1/staticfile/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        short_code = credential[2].replace('ï»¿', '').upper()
        state_repl1= credential[3].replace('ï»¿', '').title()
        try:
            if state_repl.lower() == state_repl1.lower():
                break
        except:
            break
    return short_code

for d in os.listdir('pest-control'):
    try:
        for c in os.listdir(f'pest-control/{d}'):
            try:
                for b in os.listdir(f'pest-control/{d}/{c}'):
                    try:
                        search_categories = open(f'pest-control/{d}/{c}/{b}', "r", encoding="utf8").read()
                        op= search_categories.replace("", '')
                        soup = BeautifulSoup(op, "lxml")
                        state_repl= str(d).replace('ï»¿', '').replace('-', ' ').title()
                        abbr_state= short_code_state(state_repl)
                        city= str(c).replace('ï»¿', '').replace('-', ' ').title()
                       
                        op= op.replace('[State]', f'USA').replace('{BandD|B&amp;D}', random.choice(['B&D', 'BandD'])).replace('{‘bandd pest control’|BandD Pest Control|Band &amp; D Pest Control|B&amp;D Pest Control|bandd pest experts}', random.choice(['B&D Pest Control', 'BandD Pest Control', 'Band & D Pest Control', 'B&D Pest Control', 'bandd pest experts'])).replace('{and|&amp;|plus}', random.choice(['and', '&', 'plus'])).replace('{BandD Pest Control|B&amp;D Pest Control|B and D Pest Control}', random.choice(['BandD Pest Control', 'B&D Pest Control', 'B and D Pest Control']))
                        fp = open(f'pest-control/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except Exception as oops:
                        print('Error communicating:', oops)
            except:
                pass
    except:
        pass

for d in os.listdir('pest-control'):
    try:
        search_categories = open(f'pest-control/{d}/index.html', "r", encoding="utf8").read()
        if len(d.split('-')) >3:
            op= search_categories.replace("", '')
            soup = BeautifulSoup(op, "lxml")
            split_data= d.split('-')
            state_repl= f'{split_data[0]} {split_data[1]} {split_data[2]}'.replace('ï»¿', '').replace('-', ' ').title()

            
            op= op.replace('[State]', f'USA').replace('{BandD|B&amp;D}', random.choice(['B&D', 'BandD'])).replace('{‘bandd pest control’|BandD Pest Control|Band &amp; D Pest Control|B&amp;D Pest Control|bandd pest experts}', random.choice(['B&D Pest Control', 'BandD Pest Control', 'Band & D Pest Control', 'B&D Pest Control', 'bandd pest experts'])).replace('{and|&amp;|plus}', random.choice(['and', '&', 'plus'])).replace('{BandD Pest Control|B&amp;D Pest Control|B and D Pest Control}', random.choice(['BandD Pest Control', 'B&D Pest Control', 'B and D Pest Control']))

            fp = open(f'pest-control/{d}/index.html', "w", encoding='utf-8-sig')
            fp.writelines(op)
            fp.close()
        else:
            op= search_categories.replace("", '')
            soup = BeautifulSoup(op, "lxml")
            split_data= d.split('-')
            state_repl= d.replace('ï»¿', '').replace('-', ' ').title()

            op= op.replace('[State]', f'USA').replace('{BandD|B&amp;D}', random.choice(['B&D', 'BandD'])).replace('{‘bandd pest control’|BandD Pest Control|Band &amp; D Pest Control|B&amp;D Pest Control|bandd pest experts}', random.choice(['B&D Pest Control', 'BandD Pest Control', 'Band & D Pest Control', 'B&D Pest Control', 'bandd pest experts'])).replace('{and|&amp;|plus}', random.choice(['and', '&', 'plus'])).replace('{BandD Pest Control|B&amp;D Pest Control|B and D Pest Control}', random.choice(['BandD Pest Control', 'B&D Pest Control', 'B and D Pest Control']))

            fp = open(f'pest-control/{d}/index.html', "w", encoding='utf-8-sig')
            fp.writelines(op)
            fp.close()
    except:
        pass


try:
    search_categories = open(f'pest-control/index.html', "r", encoding="utf8").read()

    op= search_categories.replace("", '')
    soup = BeautifulSoup(op, "lxml")
    
    op= op.replace('[State]', f'USA').replace('{BandD|B&amp;D}', random.choice(['B&D', 'BandD'])).replace('{‘bandd pest control’|BandD Pest Control|Band &amp; D Pest Control|B&amp;D Pest Control|bandd pest experts}', random.choice(['B&D Pest Control', 'BandD Pest Control', 'Band & D Pest Control', 'B&D Pest Control', 'bandd pest experts'])).replace('{and|&amp;|plus}', random.choice(['and', '&', 'plus'])).replace('{BandD Pest Control|B&amp;D Pest Control|B and D Pest Control}', random.choice(['BandD Pest Control', 'B&D Pest Control', 'B and D Pest Control']))
    fp = open(f'pest-control/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
