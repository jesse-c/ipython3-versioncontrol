# Make IPython 3 (Jupyter, nbformat 4) easy to keep under version control

An alternative approach to [ipython3-versioncontrol](https://github.com/balabit/ipython3-versioncontrol). Instead of creating new files in a different format, simply overwrite some trivial (in our opinion e.g. execution count) values from the notebook files.

**Key-values that are reset**

*Cell type: code*

- Execution count: null
- Outputs: []
- Metadata: {}

*Cell type: markdown*

- Metadata: {}

## Usage

```
python notebook_cleaner.py -o <notebook>
python notebook_cleaner.py -f <output> <notebook>
python notebook_cleaner.py -v | --version
python notebook_cleaner.py -h | --help
```

__Flags__

`-o`: Make changes in place

`-f`: Write the changes to a new a file
