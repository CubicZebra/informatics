# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
show_authors = True
today = ''
today_fmt = '%B %d, %Y'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'informatics'
copyright = '2023, Chen Zhang'
author = 'Chen Zhang'
version = '0.0.4'
release = '0.0.4rc0'

numfig = True
numfig_format = {'figure': 'Figure %s', 'code-block': 'Code %s'}
math_number_all = False  # no numbered for unlabeled math domain
math_eqref_format = 'Equation {number}'
rst_prolog = """
.. |author| replace:: Chen Zhang
.. |date| date::
.. |time| date:: %H:%M
.. |create| replace:: Created on
.. |signature| replace:: Created by |author|; Last updated on |time|, |date|
.. |und dev| replace:: under developing...
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    # 'sphinx_inline_tabs',
]

root_doc = 'index'
templates_path = ['_templates']
exclude_patterns = []
add_function_parentheses = False
add_module_names = False
autodoc_typehints = 'none'
autodoc_class_signature = 'separated'
autodoc_default_options = {
    'exclude-members': '__init__, __new__',
    'ignore-module-all': True
}
locale_dirs = ['_locale']
gettext_compact = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']
html_sidebars = {
    '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html']
}
html_search_language = 'en'
html_favicon = './images/favicon.jpg'
html_last_updated_fmt = '%b %d, %Y'
pygments_style = 'dracula'

# -- Options for Python domain -------------------------------------------------
# https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-the-python-domain

python_display_short_literal_types = True
