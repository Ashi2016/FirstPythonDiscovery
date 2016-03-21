import auth,cgi,cgitb
import time,json

cgitb.enable()

#http://www.yelp.com/fremont-ca-us

def main():
    form = cgi.FieldStorage()
    Location = form.getvalue('location')
    print (Location)
    for item in Location:
        if item == "fremont":
            return (37.54,-121.98)
        elif item == "sanfrancisco":
            return (37.77,-122.41)
        print ("yyy")
        #fremont = (37.54,-121.98)
        #sanfrancisco = (37.77,-122.41)
        locations = []
        item.append(locations)    
    #api_calls = []
    for lat,long in locations:
            params = get_search_parameters(lat,long)
            locations.append(get_results(params))
	#Be a good internet citizen and rate-limit yourself
            time.sleep(1.0)
#print (main)
##Do other processing	
def get_results(params):
    #Obtain these from Yelp's manage access page
    consumer_key = "UWkH4rl_hLz3fiW9wngROg"
    consumer_secret = "sQsNeWtsWJIyTMIGzWjg3K_U6CY"
    token = "cnf_rG5CovsUB92iTt8Jh2ijJIq8OBnl"
    token_secret = "I-OcivIQysHdSLCn_7kBc62D-z0"
	
    session = rauth.OAuth1Session(
        consumer_key = consumer_key
	,consumer_secret = consumer_secret
	,access_token = token
	,access_token_secret = token_secret)
    request = session.get("http://www.yelp.com/",params=params)
    #Transforms the JSON API response into a Python dictionary
    print (request)
    data = request.json()
    session.commit()
    session.close()
    return data
#print (get_results)    		
def get_search_parameters(lat,long):
    #See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["ll"] = "{},{}".format(str(lat),str(long))
    params["radius_filter"] = "2000"
    params["limit"] = "10"
    return params

try:
    if __name__=="__main__":
        main()
except:
    print ('Nothing doing')
