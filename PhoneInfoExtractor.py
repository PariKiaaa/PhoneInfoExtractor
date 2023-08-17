import phonenumbers
from phonenumbers import geocoder, carrier

# The phone number you want to analyze
phone_number = "+989123456789"    #just a random number

# Parsing the phone number for geolocation (CH)
ch_number = phonenumbers.parse(phone_number, "CH")
print("Geolocation:", geocoder.description_for_number(ch_number, 'en'))

# Parsing the phone number for carrier information (RO)
service_number = phonenumbers.parse(phone_number, 'RO')
print("Carrier:", carrier.name_for_number(service_number, 'en'))
