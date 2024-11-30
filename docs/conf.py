import os
import sys

# sys.path.insert(0, os.path.abspath("."))

sys.path.insert(0, os.path.abspath(os.path.join("..", "project")))
sys.path.insert(
    0, os.path.abspath(os.path.join("..", "project", "something_module", "classes"))
)


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "something"
# copyright = "2024, Somebody"
copyright = "2024, Somebody"
author = "Somebody"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
# html_theme_options = {"rightsidebar": "true", "relbarbgcolor": "black"}
html_theme_options = {"show_relbar_top": "true", "show_relbar_bottom": "true"}
html_show_sphinx = False
#
#  add in the extension names to the empty list variable 'extensions'
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autodocsumm",
    "sphinx.ext.coverage",
]

# add in this line for the autosummary functionality
auto_doc_default_options = {"autosummary": True}
