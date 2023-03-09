import phonenumbers
from phonenumbers import geocoder

phone = input('Type the phone in the format +551140028922: ')
phone_number = phonenumbers.parse(phone)
print(geocoder.description_for_number(phone_number, 'en'))
