import pandas as pd
from radar import RadarClient

def f_geocode_address_list(address_list, SECRET_KEY):
    radar = RadarClient(SECRET_KEY)
    geocoded_data = []
    for address in address_list:
        location = radar.geocode.forward(query=address)[0]
        data = {
            "addressLabel": location.address_label,
            "city": location.city,
            "confidence": location.confidence,
            "country": location.country,
            "countryCode": location.country_code,
            "countryFlag": location.country_flag,
            "county": location.county,
            "distance": location.distance,
            "formattedAddress": location.formatted_address,
            "geometryType": location.geometry['type'],
            "layer": location.layer,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "number": location.number,
            "postalCode": location.postal_code,
            "state": location.state,
            "stateCode": location.state_code,
            "street": location.street
        }
        geocoded_data.append(data)
    geocoded_df = pd.DataFrame(geocoded_data)
    return geocoded_df
