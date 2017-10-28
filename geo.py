import urllib.request, urllib.parse, urllib.error
import json
import webbrowser
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter location between latitudinal extent 8º4N to 37º6N and longitudinal extent 68º7E to 97º25E ')
    if len(address) <1 :break

    url= serviceurl + urllib.parse.urlencode({'address' : address})

    print('Retrieving' ,url)
    uh=urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data), 'Characters')

    try :
        js = json.loads(data)
        #dictionary
    except :
        js= None
    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    name=js["results"][0]["formatted_address"]
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('======Failure to Retrieve============')
        print(data)
        continue
      
    if 68<lng and lng<98 or 8<lat and lat<38:
        print(json.dumps(js, indent=4))
        print('In India, Name :',name)
        print('Latitude :' ,lat, 'Longitude :', lng)
        f=open('map.htm','w')
        msgMap = """ <! DOCTYPE html>

                    <html>
                            <head>
                                    <style>
                                            #map{
                                                    height: 50%;
                                                    width: 50%;
                                                    background-color: grey;
                                            }
                                    </style>
                            </head>
                            <body>
                                    <h3> My Google Maps Demo</h3>
                                    <div id="map"></div>
                                    <script>
                                            function initMap() {
                                                    var pt = {lat :20.5937,lng :78.9629};
                                                    var map =new google.maps.Map(document.getElementById('map'),{
                                                            zoom: 4,
                                                            center : pt
                                                    });
                                                    var marker =new google.maps.Marker({
                                                            position: pt,
                                                            map: map
                                                    });
                                                }
                                    </script>
                                     <script async defer src="https://maps.googleapis.com/maps/api/js?key=YourKeyCode&callback=initMap">
                                    <!--Key code can be created using googlemap apis(just by creating and signing in the account there-->
                                    </script>
                            </body>
                    </html>	"""
        f.write(msgMap)
        f.close()
        webbrowser.open_new_tab('map.htm')
        break
   
    print('The given values do not point in India')
    print('Name :',name)
    print('Latitude :' ,lat, 'Longitude :', lng)
    print('Enter values in specified range')
    print()

     
                               
        
