from dexy.template import Template

class Cowsay(Template):
    """
    Run the cowsay filter with various options.
    """
    ALIASES = ['cowsay']
    FILTERS_USED = ['cowsay', 'jinja']
