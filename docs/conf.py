# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Інформаційні технології у лінгвістиці'
copyright = '2025, Володимир КОВДРИШ'
author = 'Володимир КОВДРИШ'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"
extensions = ["myst_parser",
              "sphinx.ext.autodoc"]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = []

language = 'uk'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_book_theme'
html_theme_options = {
     "repository_provider": "github",
    "repository_url": "https://volodymyr-kovdrysh.github.io/ITinLingvo",
    "repository_branch": "dev",
    "path_to_docs": "docs",
    "use_source_button": True,
    # "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": False,
    "show_navbar_depth": 2,
    "toc_title": "Зміст",
    "show_toc_level": 2
}
html_static_path = ['_static']

myst_enable_extensions = [
  "deflist",
  "dollarmath", 
  "amsmath", 
  "colon_fence", 
  "attrs_block", 
  "attrs_inline",
  "fieldlist"]