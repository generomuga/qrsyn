from distutils.core import setup
import py2exe

setup(
    console=['printPDF.py'],
    options = {
        'py2exe': {
            'packages': ['reportlab']
        }
    }
)	