import numpy as np
import pandas as pd
import re
df = pd.read_excel('df.xlsx', engine='openpyxl')



def extract_date(description):
    if not isinstance(description, str):  # Check if the description is a string
        return None

    # Regular expression pattern to match "Month day" format
    pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December|Aug|Feb|Jan|Sept|Apr|Aug.|Sept.|Feb.|Mar|Dec) \d{1,2}"
    match = re.search(pattern, description)
    if match:
        return match.group(0)
    return None


def extract_event(description):
    if not isinstance(description, str):  # Check if the description is a string
        return None

    # Using regex to account for different variations of COVID-19
    if re.search(r'covid[-\s]?19', description, re.IGNORECASE):
        return 'COVID-19'

    events = ['earthquake', 'flood', 'tsunami', 'hurricane', 'tornado', 'cyclone', 'wildfire', 'explosions', 'Ebola', 'Hurricane']

    for event in events:
        if event in description.lower():
            return event

    return None

df['event'] = df['Description'].apply(extract_event)
df['date'] = df['Description'].apply(extract_date)
country_to_continent = {
    'Afghanistan': 'Asia',
    'Albania': 'Europe',
    'Algeria': 'Africa',
    'Andorra': 'Europe',
    'Angola': 'Africa',
    'Antigua and Barbuda': 'North America',
    'Argentina': 'South America',
    'Armenia': 'Asia',
    'Australia': 'Australia/Oceania',
    'Austria': 'Europe',
    'Azerbaijan': 'Asia',
    'Bahamas': 'North America',
    'Bahrain': 'Asia',
    'Bangladesh': 'Asia',
    'Barbados': 'North America',
    'Belarus': 'Europe',
    'Belgium': 'Europe',
    'Belize': 'North America',
    'Benin': 'Africa',
    'Bhutan': 'Asia',
    'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe',
    'Botswana': 'Africa',
    'Brazil': 'South America',
    'Brunei': 'Asia',
    'Bulgaria': 'Europe',
    'Burkina Faso': 'Africa',
    'Burundi': 'Africa',
    'Côte d\'Ivoire': 'Africa',
    'Cabo Verde': 'Africa',
    'Cambodia': 'Asia',
    'Cameroon': 'Africa',
    'Canada': 'North America',
    'Central African Republic': 'Africa',
    'Croatia': 'Europe',
    'Cyprus': 'Europe',
    'Czechia': 'Europe',
    'Denmark': 'Europe',
    'Djibouti': 'Africa',
    'Dominica': 'North America',
    'Dominican Republic': 'North America',
    'East Timor (Timor-Leste)': 'Asia',
    'Ecuador': 'South America',
    'Egypt': 'Africa',  # Geographically, Egypt is mainly in Africa, but the Sinai Peninsula is in Asia.
    'El Salvador': 'North America',
    'Equatorial Guinea': 'Africa',
    'Eritrea': 'Africa',
    'Estonia': 'Europe',
    'Eswatini': 'Africa',
    'Ethiopia': 'Africa',
    'Fiji': 'Australia/Oceania',
    'Finland': 'Europe',
    'France': 'Europe',
    'Gabon': 'Africa',
    'Gambia': 'Africa',
    'Georgia': 'Asia',  # Geographically, Georgia straddles both Europe and Asia.
    'Germany': 'Europe',
    'Ghana': 'Africa',
    'Greece': 'Europe',
    'Grenada': 'North America',
    'Guatemala': 'North America',
    'Guinea': 'Africa',
    'Guinea-Bissau': 'Africa',
    'Guyana': 'South America',
    'Haiti': 'North America',
    'Holy See': 'Europe',
    'Honduras': 'North America',
    'Hungary': 'Europe',
    'Iceland': 'Europe',
    'India': 'Asia',
    'Indonesia': 'Asia',
    'Iran': 'Asia',
    'Iraq': 'Asia',
    'Ireland': 'Europe',
    'Israel': 'Asia',
    'Italy': 'Europe',
    'Jamaica': 'North America',
    'Japan': 'Asia',
    'Jordan': 'Asia',
    'Kazakhstan': 'Asia',  # Geographically, Kazakhstan is mainly in Asia, but a small part lies in Europe.
    'Kenya': 'Africa',
    'Kiribati': 'Australia/Oceania',
    'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia',
    'Laos': 'Asia',
    'Latvia': 'Europe',
    'Lebanon': 'Asia',
    'Lesotho': 'Africa',
    'Liberia': 'Africa',
    'Libya': 'Africa',
    'Liechtenstein': 'Europe',
    'Lithuania': 'Europe',
    'Luxembourg': 'Europe',
    'Madagascar': 'Africa',
    'Malawi': 'Africa',
    'Malaysia': 'Asia',
    'Maldives': 'Asia',
    'Mali': 'Africa',
    'Malta': 'Europe',
    'Marshall Islands': 'Australia/Oceania',
    'Mauritania': 'Africa',
    'Mauritius': 'Africa',
    'Mexico': 'North America',
    'Micronesia': 'Australia/Oceania',
    'Moldova': 'Europe',
    'Monaco': 'Europe',
    'Mongolia': 'Asia',
    'Montenegro': 'Europe',
    'Morocco': 'Africa',
    'Mozambique': 'Africa',
    'Myanmar (Burma)': 'Asia',
    'Namibia': 'Africa',
    'Nauru': 'Australia/Oceania',
    'Nepal': 'Asia',
    'Netherlands': 'Europe',
    'New Zealand': 'Australia/Oceania',
    'Nicaragua': 'North America',
    'Niger': 'Africa',
    'Nigeria': 'Africa',
    'North Korea': 'Asia',
    'North Macedonia (formerly Macedonia)': 'Europe',
    'Norway': 'Europe',
    'Oman': 'Asia',
    'Pakistan': 'Asia',
    'Palau': 'Australia/Oceania',
    'Palestine': 'Asia',
    'Panama': 'North America',
    'Papua New Guinea': 'Australia/Oceania',
    'Paraguay': 'South America',
    'Peru': 'South America',
    'Philippines': 'Asia',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Qatar': 'Asia',
    'Romania': 'Europe',
    'Russia': 'Europe',  # Geographically, Russia spans both Europe and Asia.
    'Rwanda': 'Africa',
    'Saint Kitts and Nevis': 'North America',
    'Saint Lucia': 'North America',
    'Saint Vincent and the Grenadines': 'North America',
    'Samoa': 'Australia/Oceania',
    'San Marino': 'Europe',
    'Sao Tome and Principe': 'Africa',
    'Saudi Arabia': 'Asia',
    'Senegal': 'Africa',
    'Serbia': 'Europe',
    'Seychelles': 'Africa',
    'Sierra Leone': 'Africa',
    'Singapore': 'Asia',
    'Slovakia': 'Europe',
    'Slovenia': 'Europe',
    'Solomon Islands': 'Australia/Oceania',
    'Somalia': 'Africa',
    'South Africa': 'Africa',
    'South Korea': 'Asia',
    'South Sudan': 'Africa',
    'Spain': 'Europe',
    'Sri Lanka': 'Asia',
    'Sudan': 'Africa',
    'Suriname': 'South America',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'Syria': 'Asia',
    'Taiwan': 'Asia',
    'Tajikistan': 'Asia',
    'Tanzania': 'Africa',
    'Thailand': 'Asia',
    'Togo': 'Africa',
    'Tonga': 'Australia/Oceania',
    'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa',
    'Turkey': 'Europe',  # Geographically, Turkey is mainly in Asia, but a small part lies in Europe.
    'Turkmenistan': 'Asia',
    'Tuvalu': 'Australia/Oceania',
    'Uganda': 'Africa',
    'Ukraine': 'Europe',
    'United Arab Emirates': 'Asia',
    'United Kingdom': 'Europe',
    'United States of America': 'North America',
    'Uruguay': 'South America',
    'Uzbekistan': 'Asia',
    'Vanuatu': 'Australia/Oceania',
    'Vatican City (Holy See)': 'Europe',
    'Venezuela': 'South America',
    'Vietnam': 'Asia',
    'Yemen': 'Asia',
    'Zambia': 'Africa',
    'Zimbabwe': 'Africa',
    'Abkhazia': 'Europe',  # Some consider it part of Europe, others Asia. It's also a disputed territory.
    'Artsakh': 'Asia',  # Also known as Nagorno-Karabakh, a disputed territory.
    'Cook Islands': 'Australia/Oceania',
    'Faroe Islands': 'Europe',
    'French Polynesia': 'Australia/Oceania',
    'Greenland': 'North America',  # Politically associated with Europe (Denmark), but geographically part of North America.
    'Guadeloupe': 'North America',
    'Guam': 'Australia/Oceania',
    'Hong Kong': 'Asia',
    'Kosovo': 'Europe',
    'Macao': 'Asia',
    'Martinique': 'North America',
    'Mayotte': 'Africa',
    'New Caledonia': 'Australia/Oceania',
    'Niue': 'Australia/Oceania',
    'Puerto Rico': 'North America',
    'Réunion': 'Africa',
    'Sahrawi Arab Democratic Republic': 'Africa',  # Also known as Western Sahara, a disputed territory.
    'Tokelau': 'Australia/Oceania',
    'Transnistria': 'Europe',
    'Chad': 'Africa',
    'Comoros': 'Africa',
    'Congo (Brazzaville)': 'Africa',  # This is the Republic of the Congo.
    'Congo (Kinshasa)': 'Africa',  # This is the Democratic Republic of the Congo.
    'Djibouti': 'Africa',
    'Equatorial Guinea': 'Africa',
    'Eritrea': 'Africa',
    'Eswatini': 'Africa',  # Previously known as Swaziland.
    'Ethiopia': 'Africa',
    'Gabon': 'Africa',
    'Gambia': 'Africa',
    'Ghana': 'Africa',
    'Guinea': 'Africa',
    'Guinea-Bissau': 'Africa',
    'Kenya': 'Africa',
    'Lesotho': 'Africa',
    'Liberia': 'Africa',
    'Libya': 'Africa',
    'Madagascar': 'Africa',
    'Malawi': 'Africa',
    'Republic of the Congo': 'Africa',
    'Cuba' : 'Caribbean',
    'Republic of Korea': 'Asia'
}

countries = [country for country in country_to_continent.keys() if country != 'China']
pattern_countries = r"\b(" + "|".join(countries) + r")\b"

def extract_country(description):
    if not isinstance(description, str):
        return None
    
    match = re.search(pattern_countries, description)
    if match:
        country = match.group(0)
        return country
    return None

def extract_continent(country):
    return country_to_continent.get(country, None)

# Apply the functions to the dataframe
df['Country'] = df['Description'].apply(extract_country)
df['Continent'] = df['Country'].apply(extract_continent)

country_to_latlong = {
    'Afghanistan': (34.5553, 69.2075),  # Kabul
    'Albania': (41.3275, 19.8187),      # Tirana
    'Croatia': (45.8150, 15.9819),      # Zagreb
    'Laos': (17.9667, 102.6),           # Vientiane
    'Venezuela': (10.4806, -66.9036),   # Caracas
    'Russia': (55.7558, 37.6173),       # Moscow
    'Belarus': (53.9045, 27.5615),      # Minsk
    'Kazakhstan': (51.1694, 71.4491),   # Nur-Sultan
    'Serbia': (44.7866, 20.4489),       # Belgrade
    'Thailand': (13.7563, 100.5018),    # Bangkok
    'Antigua and Barbuda': (17.0747, -61.8175), # St. John's
    'France': (48.8566, 2.3522),        # Paris
    'Ethiopia': (9.03, 38.74),          # Addis Ababa
    'Italy': (41.9028, 12.4964),        # Rome
    'Cambodia': (11.5564, 104.9282),    # Phnom Penh
    'Philippines': (14.5995, 120.9842), # Manila
    'Greece': (37.9838, 23.7275),       # Athens
    'Tunisia': (36.8065, 10.1815),      # Tunis
    'Pakistan': (33.6844, 73.0479),     # Islamabad
    'Malawi': (-13.9626, 33.7741),      # Lilongwe
    'Namibia': (-22.559722, 17.083611), # Windhoek
    'Zimbabwe': (-17.8252, 31.0335),    # Harare
    'Iraq': (33.3152, 44.3661),         # Baghdad
    'Switzerland': (46.9480, 7.4474),   # Bern
    'Turkmenistan': (37.9601, 58.3261), # Ashgabat
    'Indonesia': (-6.2088, 106.8456),   # Jakarta
    'Iran': (35.6892, 51.3890),         # Tehran
    'South Sudan': (4.8594, 31.5713),   # Juba
    'Mozambique': (-25.9692, 32.5732),  # Maputo
    'Guinea': (9.6412, -13.5784),       # Conakry
    'Nigeria': (9.0579, 7.4951),        # Abuja
    'Sri Lanka': (6.9271, 79.8612),     # Colombo
    'Yemen': (15.3694, 44.1910),        # Sana'a
    'Cuba': (23.1136, -82.3666),        # Havana
    'Tonga': (-21.1393, -175.2026),     # Nuku'alofa
    'Republic of the Congo': (-4.2634, 15.2429), # Brazzaville
    'Republic of Korea': (37.5665, 126.9780),    # Seoul
    'Benin': (6.5244, 2.5963),          # Porto-Novo
    'Equatorial Guinea': (3.7504, 8.7371), # Malabo
    'Sudan': (15.5007, 32.5599),        # Khartoum
    'Syria': (33.5138, 36.2765),        # Damascus
    'Madagascar': (-18.8792, 47.5079),  # Antananarivo
    'Lebanon': (33.8938, 35.5018),      # Beirut
    'Jordan': (31.9539, 35.9106),       # Amman
    'Sao Tome and Principe': (0.3302, 6.7333), # São Tomé
    'Botswana': (-24.6282, 25.9231),    # Gaborone
    'Djibouti': (11.5721, 43.1456),     # Djibouti City
    'Central African Republic': (4.3947, 18.5582), # Bangui
    'Egypt': (30.802498, 31.269821),    # Cairo
    'Nepal': (27.7172, 85.3240),        # Kathmandu
    'Mali': (12.6392, -8.0029),         # Bamako
    'Malaysia': (3.1390, 101.6869),     # Kuala Lumpur
    'El Salvador': (13.6929, -89.2182), # San Salvador
    'Togo': (6.1375, 1.2123),           # Lomé
    'Ukraine': (50.4501, 30.5234),      # Kyiv
    'Grenada': (12.1165, -61.6790),     # St. George's
    'Japan': (35.6895, 139.6917),       # Tokyo
    'Saudi Arabia': (24.7136, 46.6753), # Riyadh
    'Algeria': (36.7372, 3.0865),       # Algiers
    'South Africa': (-25.7461, 28.1881), # Pretoria
    'Gambia': (13.4432, -16.6929),      # Banjul
    'Liberia': (6.2907, -10.7605),      # Monrovia
    'Panama': (8.983333, -79.5167),     # Panama City
    'Burkina Faso': (12.3715, -1.5197), # Ouagadougou
    'Hungary': (47.4979, 19.0402),      # Budapest
    'Uganda': (0.3476, 32.5825),        # Kampala
    'Peru': (-12.0464, -77.0428),       # Lima
    'Gabon': (-0.8037, 10.4895),        # Libreville
    'Angola': (-8.8390, 13.2894),       # Luanda
    'Bosnia and Herzegovina': (43.8563, 18.4131), # Sarajevo
    'Tajikistan': (38.5561, 68.7708),   # Dushanbe
    'Fiji': (-18.1416, 178.4419),       # Suva
    'Papua New Guinea': (-9.4438, 147.1803), # Port Moresby
    'Vanuatu': (-17.7404, 168.3219)
}

def extract_latitude(country):
    if country in country_to_latlong:
        return country_to_latlong[country][0]
    return None

def extract_longitude(country):
    if country in country_to_latlong:
        return country_to_latlong[country][1]
    return None

# Apply the functions to the dataframe
df['Latitude'] = df['Country'].apply(extract_latitude)
df['Longitude'] = df['Country'].apply(extract_longitude)

print(df[['date', 'Country', 'Continent', 'Latitude', 'Longitude', 'event']].to_string())

df.to_csv('DfFirst.csv', index=False)
