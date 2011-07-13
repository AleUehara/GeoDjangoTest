#!/usr/bin/env python
from django.core.management import execute_manager
#from waypoints.models import Waypoint
#Waypoint(name='New York', geometry='POINT(-73.9869510 40.7560540)').save()
#Waypoint(name='Buenos Aires', geometry='POINT(-58.4173090 -34.6117810)').save()
#Waypoint(name='Moscow', geometry='POINT(37.6176330 55.7557860)').save()
#Waypoint(name='Atlanta', geometry='POINT(-84.3896630 33.7544870)').save()
#print Waypoint.objects.all()

import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
