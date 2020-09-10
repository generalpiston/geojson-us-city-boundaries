import json
import sys
import os
import re

parens_regex = re.compile("\\(([^\\)]+)\\)")

def main():
  filenames = os.listdir("./states")

  for filename in filenames:
    extract("./states/{}".format(filename))

def get_names(fullname):
  names = [parens_regex.sub('', name).strip() for name in fullname.split('/')]

  return [name.split(',')[0].strip() for name in names if name]

def extract(filename):
  state = os.path.basename(filename).replace('.json','')
  output_dir = "./cities/{}".format(state)
  
  if not os.path.exists(output_dir):
    os.mkdir(output_dir)

  with open(filename, 'r') as f:
    gj = json.loads(f.read())
  
    output = { "type": "FeatureCollection", "features": [] }

    for feature in gj['features']:
      for name in get_names(feature['properties']['NAME']):
        new_name = '{}.json'.format(name.lower().replace(' ', '-'))
        output = { "type": "FeatureCollection", "features": [feature] }
        output_path = os.path.join(output_dir, new_name)

        with open(output_path, 'w') as f:
          print('Writing {}'.format(output_path))
          f.write(json.dumps(output))

main()