import pandas as pd
import numpy as np
import re, math
from collections import Counter
from googlemaps import convert
from googlemaps import Client
from googlemaps.convert import as_list

WORD = re.compile(r'\w+')

#applying cosine similarity for finding similarities between user interests and places
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

#remove spaces from the category column of dataset
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

#calulating weighted rating of places



metadata = pd.read_csv('/home/sukrati/Desktop/BTP/Code/data4.csv', low_memory=False)
#print(metadata.head())
print("Select your preferred category:\n1.wildlife \n2.heritage \n3.pilgirmage\n4.park\n5.museum")
text1 = input("Enter User Interests: ")   #user preference
vector1 = text_to_vector(text1)
C = metadata['p_rating'].mean()
m = metadata['count'].quantile(0.75)

def weighted_rating(x, m=m, C=C):
    v = x['count']
    R = x['p_rating']
    # Calculation based on the Bayesian Rating Formula
    return (v/(v+m) * R) + (m/(m+v) * C)

metadata['category'] = metadata['category'].apply(clean_data)
metadata['score'] = metadata.apply(weighted_rating, axis=1)
#print(metadata.head())
cos=[]
for i in list(metadata['category']):
    #print(type(i))
    text2 = i
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    cos.append(cosine)
metadata['cosine']=cos
x=metadata['cosine']>0.0
rec=pd.DataFrame(metadata[x])
rec=rec.sort_values('score',ascending=False)
src=input("Enter your location: ")
dest=list(rec['title'])
#print(type(dest))



def distance_matrix(client,origins, destinations,
                    mode=None, language=None, avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
                    transit_routing_preference=None, traffic_model=None, region=None):
    params = {
        "origins": convert.location_list(origins),
        "destinations": convert.location_list(destinations)
    }

    if mode:
        # NOTE(broady): the mode parameter is not validated by the Maps API
        # server. Check here to prevent silent failures.
        if mode not in ["driving", "walking", "bicycling", "transit"]:
            raise ValueError("Invalid travel mode.")
        params["mode"] = mode

    if language:
        params["language"] = language

    if avoid:
        if avoid not in ["tolls", "highways", "ferries"]:
            raise ValueError("Invalid route restriction.")
        params["avoid"] = avoid

    if units:
        params["units"] = units

    if departure_time:
        params["departure_time"] = convert.time(departure_time)

    if arrival_time:
        params["arrival_time"] = convert.time(arrival_time)

    if departure_time and arrival_time:
        raise ValueError("Should not specify both departure_time and"
                         "arrival_time.")

    if transit_mode:
        params["transit_mode"] = convert.join_list("|", transit_mode)

    if transit_routing_preference:
        params["transit_routing_preference"] = transit_routing_preference

    if traffic_model:
        params["traffic_model"] = traffic_model

    if region:
        params["region"] = region
    #print(client._request("/maps/api/distancematrix/json", params))
    return client._request("/maps/api/distancematrix/json", params)

client = Client(key='AIzaSyA8wq3R8WASxgUqTvWCh5blEmGzU8njVZ0')
dist=[]
dur=[]
for d in dest:
    d=d+",Jaipur"
    #print(d)
    output=distance_matrix(client,src,d)
    #print(output)
    a1=(output['rows'][0]['elements'][0]['distance']['text'])
    a2=(output['rows'][0]['elements'][0]['duration']['text'])
    dist.append(a1)
    dur.append(a2)

rec['distance']=dist
rec['duration']=dur

final=pd.DataFrame(rec,index=None,columns=['title','category','score','distance','duration'])
print(final)
