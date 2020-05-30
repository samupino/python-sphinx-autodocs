# Python and Sphinx: auto-documentation of nested packages

A basic example of how to set and run Sphinx to auto-generate the
documentation for a Python code having a nested structure.

Result here: [beautiful HTML documentation](docs/build/html/index.html)

## Installation

```
pip install sphynx
pip install sphinx-autopackagesummary
```

## Initialization

From the main directory type in the terminal

```
sphinx-quickstart ./docs
```

Choosing

```
> Separate source and build directories (y/n) [n]: y
> Project name: DocExample
> Author name(s): Samuele
> Project release []: 0.1
```

Edit `docs/conf.py` by uncommenting the following line and replacing the
`'.'` with `'../..'` to insert the main directory among the paths for
packages search.

```
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

Add to the extension:
- "autodoc" to automatically generate module pages
- "coverage" (?)
- "autosummary" to automatically generate summary tables
- "autopackagesummary" to recursively generate sub-module summaries
- "Napoleon" to enable Sphinx to understand docstrings written in two
other popular formats: NumPy and Google.
- the last line enables autosummary to work

```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
    'sphinx_autopackagesummary',
    'sphinx.ext.napoleon',
    ]

autosummary_generate = True
```

### Edit the index page

Remove the useless comments at the beginning of in `index.rst`.

Also add pages that will be put in the `toctree`. Every page must have
a corresponding `.rst` file.

An example of index

```
Welcome to DocExample's documentation!
======================================

This example demonstrates how to generate documentation from your Python
code using **Sphinx**.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   page
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

### Edit the package page

The file `samplepackage.rst` should be the root of the API documentation
tree.

```
Sample package
===============

This page contains the list of project's modules.

.. autopackagesummary:: samplepackage
   :toctree: _autosummary
   :template: package.rst
```

We use `autopackagesummary` to make it build all the package tree.

The `template` argument specifies a template for the module pages that
are generated as the package tree is visited. This file must be created
in the directory `_templates/package.rst`.

This is an example of a template that behaves as an intermediate tree
node if the module is a package and as a module if it is a file `.py`.

```
{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}
   :members:

   .. autopackagesummary:: {{ fullname }}
      :toctree: .
      :template: package.rst
```

The `automodule` directive parses the docstrings in the python file and
generates a page listing the module classes, functions and methods.

## Generate docs

Make sure you are in the `./docs` directory and execute

```
make html
```

The documentation index file will be in `docs/build/html/index.html`.

### Cleaning the old documentation

After changing the package code structure it may happen to encounter an
error when making the updated html. In this case a clean may be needed

```
make clean
rm -rf source/_autosummary
```