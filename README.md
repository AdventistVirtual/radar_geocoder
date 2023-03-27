# Radar Geocoder

Python function for geocoding addresses using the Radar API

This code demonstrates how to use the RadarClient class from the radar module to forward (reverse and ip to be added later on) geocode a list of addresses using the Radar API.

# Prerequisites
You should have a Radar API secret key. If you don't have one, sign up on Radar's website.

```
https://radar.com/
```

Install the ```pandas``` and ```radar``` modules in your Python environment.

```
pip install pandas
pip install radar-python
```

# Function (Combined Code Below)
Import the ```pandas``` library using its alias ```pd```.

```
import pandas as pd
```

Import the ```RadarClient``` class from the ```radar``` module.

```
from radar import RadarClient
```

Define a function called ```f_geocode_address_list``` that takes a list of addresses as an argument.

```
def f_geocode_address_list(address_list):
```

Create a ```RadarClient``` instance named ```radar``` with the secret key stored in the ```SECRET_KEY``` variable.

```
    radar = RadarClient(SECRET_KEY)
```

Initialize an empty list called ```geocoded_data``` to store the geocoded address data.

```
    geocoded_data = []
```

Loop through each ```address``` in the input ```address_list``` using a ```for``` loop.

```
    for address in address_list:
```

Query the Radar geocoding API for the latitude, longitude, and other relevant data of the current address using the forward method of the ```radar.geocode``` object. Store the result in the ```address``` variable.

```
        address = radar.geocode.forward(query=address)[0]
```

Create a dictionary object called ```data``` that stores the relevant fields of the ```address``` information.

```
data = {
            "addressLabel": address.addressLabel,
            "city": address.city,
            "confidence": address.confidence,
            "country": address.country,
            "countryCode": address.countryCode,
            "countryFlag": address.countryFlag,
            "county": address.county,
            "distance": address.distance,
            "formattedAddress": address.formattedAddress,
            "geometryType": address.geometry['type'],
            "layer": address.layer,
            "latitude": address.latitude,
            "longitude": address.longitude,
            "number": address.number,
            "postalCode": address.postalCode,
            "state": address.state,
            "stateCode": address.stateCode,
            "street": address.street
        }
```

Append the ```data``` dictionary to the ```geocoded_data``` list.

```
        geocoded_data.append(data)
```

Create a pandas DataFrame called ```df``` from the ```geocoded_data``` list using the ```pd.DataFrame()``` method.

```
    df = pd.DataFrame(geocoded_data)
```

Return the DataFrame.

```
    return df
```

# Combined Code

Code for ```f_geocode_address_list``` function.

```
def f_geocode_address_list(address_list):
    radar = RadarClient(SECRET_KEY)
    geocoded_data = []
    for query in address_list:
        address = radar.geocode.forward(query=query)[0]
        data = {
            "addressLabel": address.addressLabel,
            "city": address.city,
            "confidence": address.confidence,
            "country": address.country,
            "countryCode": address.countryCode,
            "countryFlag": address.countryFlag,
            "county": address.county,
            "distance": address.distance,
            "formattedAddress": address.formattedAddress,
            "geometryType": address.geometry['type'],
            "layer": address.layer,
            "latitude": address.latitude,
            "longitude": address.longitude,
            "number": address.number,
            "postalCode": address.postalCode,
            "state": address.state,
            "stateCode": address.stateCode,
            "street": address.street
        }
        geocoded_data.append(data)
    df = pd.DataFrame(geocoded_data)
    return df
```

# Installing the ```Radar_Geocoder``` Package
Install the package using ```pip```.

```
pip install radar_geocoder
```

#Calling The Function (Combined Code Below)
Set a ```SECRET_KEY``` variable to a string containing the secret key needed to access the Radar API.

```
SECRET_KEY = "Your_Key_Here"

```

Define a list of ```addresses``` called ```address_list```.

```
address_list = ["5 Verti Drive, Waterville, Maine, 04901", "123 Main St, Anytown, California, 12345"]
```

Call the ```f_geocode_address_list``` function with the ```address_list``` variable as an argument and store the returned DataFrame in a variable called ```df```.

```
df = f_geocode_address_list(address_list)
```

Display the DataFrame using the ```df``` variable.

```
df
```

Example Output.

```
addressLabel	city	confidence	country	countryCode	countryFlag	county	distance	formattedAddress	geometryType	layer	latitude	longitude	number	postalCode	state	stateCode	street
0	5 Verti Drive	Waterville	exact	United States	US	🇺🇸	Kennebec County	0	5 Verti Drive, Waterville, ME 04901 USA	Point	address	44.513791	-69.660212	5	04901	Maine	ME	Verti Drive
1	123 Main St	San Diego	exact	United States	US	🇺🇸	San Diego County	0	123 Main St, San Diego, CA 12345 USA	Point	address	32.552745	-117.043844	123	12345	California	CA	Main St
```

# License
This code is licensed under the MIT License.

# P.S.
This is my first package so I hope whoever uses it finds it helpful!
