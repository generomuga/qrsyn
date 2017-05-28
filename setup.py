from distutils.core import setup
import py2exe

setup(
    console=['qrrow.py'],
    options = {
        'py2exe': {
            'packages': ['reportlab']
        }
    }
)	