# Configuration file for the Sphinx documentation builder.
project = 'Cloud'
copyright = '2023, robotdreams'
author = 'robotdreams'
release = '1'

extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton'
]

pygments_style = 'sphinx'

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

html_theme_options = {
    "navigation_depth": -1
}

html_logo = "_static/Logo.jpg"

html_css_files = ['max_width.css']
