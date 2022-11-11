import pandas as pd
import csv
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_user_agent")
df = pd.read_csv('therapist3.csv', sep="\t", index_col = [0])

def getGeo1(street, city, state, postalcode):
    try:
        address = '' if street == 'nan' or street == '' else street + ','
        address = address + city + ', ' + state + ', ' + postalcode
        # print("geo1: ", address)
        loc = geolocator.geocode(address)
        return loc
    except:
        return None

def getGeo2(city, state, postalcode):
    try:
        address = city + ', ' + state + ', ' + postalcode
        # print("geo2: ", address)
        loc = geolocator.geocode(address)
        return loc
    except:
        return None

def getGeo3(city, state):
    try:
        address = city + ', ' + state
        loc = geolocator.geocode(address)
        return loc
    except:
        return None

# test
# loc = getGeo1("","Brea","CA","94915")
# if loc is None:
#     loc = getGeo2("Brea","CA","94915")
# if loc is not None:
#     print(str(loc.latitude), ",", str(loc.longitude))
# else:
#     print("NOT FOUND!!!")

newdf = []
for index, row in df.iterrows():
    print(index)
    res = getGeo1(str(row["street"]), row["city"], row["state"], str(row["postalcode"]))
    if res is None:
        res = getGeo2(row["city"], row["state"], str(row["postalcode"]))
        
    newitem = ''
    if res is not None:
        newitem = str(res.latitude) + ',' + str(res.longitude)
        
    print(newitem)
    newdf.append(newitem)

df['geo'] = newdf
df = df.loc[:,['url','name','title','mobile','street','city','state','postalcode','geo','about','website','specialities','specialties_detail','ethnicity','age','communities','therapy_type','modality']]

df.to_csv('therapist3.csv', sep="\t")

# # missing part
# for index, row in df.iterrows():
#     if len(str(row["geo"])) < 5:
#         print(index)
#         res = getGeo3(row["city"], row["state"])
#         newitem = ''
#         if res is not None:
#             newitem = str(res.latitude) + ',' + str(res.longitude)
#         print(newitem)
#         df.loc[index, "geo"] = newitem

# df.to_csv('therapist4.csv', sep="\t")
