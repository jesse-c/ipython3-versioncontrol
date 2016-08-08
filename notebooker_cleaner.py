"""Clean IPython3 (Jupter, nbformat 4) notebooks.

Usage:
  notebook_cleaner -o <notebook>
  notebook_cleaner -f <output> <notebook>
  notebook_cleaner -v | --version
  notebook_cleaner -h | --help

Options:
  -o            Overwrite file in place.
  -f <file>     Write to specified file.
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
import sys
import os.path
import json
from collections import OrderedDict


def clean(notebook, output):
    with open(notebook, 'r+') as f:
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

        with open(output, 'w+') as s:
            print('Writing clean version to {}'.format(output))
            # Dump the JSON
            json.dump(j, s, indent=1, separators=(',', ': '))
            # Add a newline char to prevent a diff at EOF
            s.write('\n')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='notebook_cleaner 0.0.1')

    notebook = arguments['<notebook>']
    output = arguments['-f']

    assert os.path.isfile(notebook),    \
        "Notebook path arg isn't a file."
    assert notebook.endswith(".ipynb"), \
        "The file wasn't an IPython notebook (.ipynb)."

    if arguments['-o']:
        clean(notebook, notebook)
    elif arguments['-f']:
        clean(notebook, output)
