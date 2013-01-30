from dexy.template import Template

class Cowsay(Template):
    """
    Run the cowsay filter with various options.
    """
    ALIASES = ['cowsay']
    FILTERS_USED = ['cowsay', 'jinja']

class Pygments(Template):
    """
    Applies the pygments filter.
    """
    ALIASES = ['pygments']
    FILTERS_USED = ['pyg', 'shint', 'idio', 'l']

class PygmentsStylesheets(Template):
    """
    How to generate stylesheets for use with pygments.
    """
    ALIASES = ['pygments-stylesheets']
    FILTERS_USED = ['pyg', 'shint', 'idio']

class PygmentsImage(Template):
    """
    How to use the image output formats from pygments.
    """
    ALIASES = ['pygments-image']
    FILTERS_USED = ['pyg', 'gn', 'jn', 'pn']

    @classmethod
    def is_active(klass):
        try:
            import PIL
            return True
        except ImportError:
            return False

class Markdown(Template):
    """
    Convert markdown to HTML.
    """
    ALIASES = ['markdown']
    FILTERS_USED = ['markdown', 'jinja', 'pyg']

class Figlet(Template):
    """
    Makes a figlet out of text.
    """
    ALIASES = ['figlet']
    FILTERS_USED = ['figlet']

class Abc(Template):
    """
    Shows how to generate a .pdf from .abc music notation file.
    """
    ALIASES = ['abc']
    FILTERS_USED = ['abc', 'h']

class Regetron(Template):
    """
    Shows how to use regetron.
    """
    ALIASES = ['regetron']
    FILTERS_USED = ['regetron']

class ReStructuredText(Template):
    """
    Shows how to convert ReST using various filters.
    """
    ALIASES = ['rst']
    FILTERS_USED = ['rstdocparts', 'rst', 'rstbody', 'latex']
