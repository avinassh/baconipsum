import os
import sys


BASE_DIR = os.path.abspath( os.path.dirname( __file__ ) )


activate_this = os.path.join( os.path.abspath( BASE_DIR ), "env/bin/activate_this.py" )
execfile( activate_this, dict( __file__ = activate_this ) )

sys.path.insert( 0, BASE_DIR )
from baconipsum import app as application
