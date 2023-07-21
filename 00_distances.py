
from pprint import pprint


stick = {
    'Cherkessk': (450, 340),
    'Stavropol': (290, 645),
    'Nalchik': (330, 443)
}

distances = dict()

cherkessk_stavropol = ((stick['Cherkessk'][0] - stick['Stavropol'][0]) ** 2 + (stick['Cherkessk'][1] - stick['Stavropol'][1]) **2 ) ** .5
cherkessk_nalchik = ((stick['Cherkessk'][0] - stick['Nalchik'][0]) ** 2 + (stick['Cherkessk'][1] - stick['Nalchik'][1]) **2 ) ** .5
stavropol_nalchik = ((stick['Stavropol'][0] - stick['Nalchik'][0]) ** 2 + (stick['Stavropol'][1] - stick['Nalchik'][1]) **2 ) ** .5

distances['Cherkessk'] = {}
distances['Cherkessk']['Stavropol'] = cherkessk_stavropol
distances['Cherkessk']['Nalchik'] = cherkessk_nalchik

distances['Stavropol'] = {}
distances['Stavropol']['Cherkessk'] = cherkessk_stavropol
distances['Stavropol']['Nalchik'] = stavropol_nalchik

distances['Nalchik'] = {}
distances['Nalchik']['Cherkessk'] = cherkessk_nalchik
distances['Nalchik']['Stavropol'] = stavropol_nalchik



pprint(distances)