from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# Import system modules
import simplejson
# Import custom modules
from waypoints.models import Waypoint


def index(request):
    'Display map'
    waypoints = Waypoint.objects.order_by('name')
    return render_to_response('waypoints/index.html', {
        'waypoints': waypoints,
        'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints}),
    })

def save(request):
    'Save waypoints'
    for waypointString in request.POST.get('waypointsPayload', '').splitlines():
        waypointID, waypointX, waypointY = waypointString.split()
        waypoint = Waypoint.objects.get(id=int(waypointID))
        waypoint.geometry.set_x(float(waypointX))
        waypoint.geometry.set_y(float(waypointY))
        waypoint.save()
    return HttpResponse(simplejson.dumps(dict(isOk=1)), mimetype='application/json')
