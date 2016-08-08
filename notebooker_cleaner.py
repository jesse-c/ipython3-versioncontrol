from docopt import docopt
import sys
import os.path
import json
from collections import OrderedDict

assert len(sys.argv) == 2,             \
  "Missing file path arg."
assert os.path.isfile(sys.argv[1]),    \
    "File path arg isn't a file."
assert sys.argv[1].endswith(".ipynb"), \
  "The file wasn't an IPython notebook (.ipynb)."

with open(sys.argv[1], 'r+') as f:
    # Read in the notebook and retain order
    j = json.loads(f.read(), object_pairs_hook=OrderedDict)

    # Reset trivial changes
    for i in range(len(j['cells'])):
        if j['cells'][i]['cell_type'] == 'code':
            j['cells'][i]['execution_count'] = None
            j['cells'][i]['outputs'] = []
            j['cells'][i]['metadata'] = {}
        elif j['cells'][i]['cell_type'] == 'markdown':
            j['cells'][i]['metadata'] = {}

    # Construct the filename for the clean version
    base = os.path.basename(sys.argv[1])
    base_split = os.path.splitext(base)
    clean = '{}.clean{}'.format(base_split[0], base_split[1])
    file_dir = os.path.dirname(sys.argv[1])
    if file_dir:
        clean = '{}/{}'.format(file_dir, clean)

    with open(clean, 'w+') as s:
        print('Writing clean version to {}'.format(clean))
        # Dump the JSON
        json.dump(j, s, indent=1, separators=(',', ': '))
        # Add a newline char to prevent a diff at EOF
        s.write('\n')
