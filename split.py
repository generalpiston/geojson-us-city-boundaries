import json
import sys

js = open(sys.argv[1], 'r').read()
gj = json.loads(js)

output = { "type": "FeatureCollection", "features": [] }

for feature in gj['features']:
  name = '{}.json'.format(feature['properties']['NAME'].lower().replace(' ', '-'))
  output = { "type": "FeatureCollection", "features": [feature] }

  with open(name, 'w') as f:
    print('Writing {}'.format(name))
    f.write(json.dumps(output))
