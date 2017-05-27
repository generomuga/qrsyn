from distutils.core import setup
import py2exe

setup(
    console=['qrsyn.py'],
    options = {
        'py2exe': {
            'packages': ['reportlab']
        }
    }
)	