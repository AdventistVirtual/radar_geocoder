import pandas as pd
from radar import RadarClient

def geocode_address_list(address_list, SECRET_KEY):
    radar = RadarClient(SECRET_KEY)
    geocoded_data = []
    for address in address_list:
        address = radar.geocode.forward(query=address)[0]
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
    geocoded_df = pd.DataFrame(geocoded_data)
    return geocoded_df