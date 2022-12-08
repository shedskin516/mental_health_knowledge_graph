from flask import Blueprint, current_app, request, jsonify

from api.dao.therapist import TherapistDAO

from geopy.geocoders import Nominatim
import geopy.distance
geolocator = Nominatim(user_agent="my_user_agent")

therapist_routes = Blueprint("therapist", __name__, url_prefix="/api/therapist")


def getGeo(address):
    try:
        loc = geolocator.geocode(address)
        return (loc.latitude, loc.longitude)
    except:
        return None
        
        
def calDistance(therapists, geo_user):
    for t in therapists:
        geo_t = (t['geo'].split(',')[0], t['geo'].split(',')[1])
        distance = geopy.distance.geodesic(geo_user, geo_t).km
        t['distance'] = distance


# get disease detail by disease name
@therapist_routes.route('/', methods = ['POST', 'GET'])
def get_therapist():
    data = request.get_json()

    dao = TherapistDAO(current_app.driver)
    output = dao.getTherapist(data)

    # sort by distance
    if data['address'] != '':
        geo_user = getGeo(data['address'])
        print('User location', geo_user)
        calDistance(output, geo_user)
        output.sort(key=lambda x: x["distance"])

    return jsonify(output)

