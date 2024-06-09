# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Gihyojp Sphinx Sample'
copyright = '2024, takanory'
author = 'takanory'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/logo.png"

# https://pradyunsg.me/furo/customisation/top-of-page-buttons/
html_theme_options = {
    "source_repository": "https://github.com/takanory/gihyojp-sphinx-sample/",
    "source_branch": "main",
    "source_directory": "source",
}

# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
todo_include_todos = True

# https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
]
