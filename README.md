# Make IPython 3 (Jupter, nbformat 4) easy to keep under version control

An alternative approach to [ipython3-versioncontrol](https://github.com/balabit/ipython3-versioncontrol). Instead of creating new files, simply overwrite some trivial (in our opinion) values from the notebook files.

**Key-values that are reset**

*Cell type: code*

- Execution count: null
- Outputs: []
- Metadata: {}

*Cell type: markdown*

- Metadata: {}

## Usage

```
python notebooker_cleaner.py

Usage:
  notebook_cleaner.py -o <notebook>
  notebook_cleaner.py -f <output> <notebook>
  notebook_cleaner.py -v | --version
  notebook_cleaner.py -h | --help
```
