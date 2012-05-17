activate_this = "/home/david/flask/env/bin/activate_this.py"
execfile( activate_this, dict( __file__ = activate_this ) )

import sys
sys.path.insert( 0, "/home/david/flask" )
from baconipsum import app as application
