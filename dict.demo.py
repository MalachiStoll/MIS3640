def histogram(s):
    d = dict()
    for c in s.lower():
    #     if c not in d:
    #         d[c] = 1
    #     else:
    #         d[c] += 1
    # return d

        d[c]= d.get(c, 0) + 1
    return d

h = histogram('Bookkepper')
print(h)

def print_hist():
    for c in h: 
        print(c, h[c])

print_hist()

json_example = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "231",
               "short_name" : "231",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Forest Street",
               "short_name" : "Forest St",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Babson Park",
               "short_name" : "Babson Park",
               "types" : [ "neighborhood", "political" ]
            },
            {
               "long_name" : "Wellesley",
               "short_name" : "Wellesley",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Norfolk County",
               "short_name" : "Norfolk County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Massachusetts",
               "short_name" : "MA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "02457",
               "short_name" : "02457",
               "types" : [ "postal_code" ]
            },
            {
               "long_name" : "0310",
               "short_name" : "0310",
               "types" : [ "postal_code_suffix" ]
            }
         ],
         "formatted_address" : "231 Forest St, Babson Park, MA 02457, USA",
         "geometry" : {
            "location" : {
               "lat" : 42.2993708,
               "lng" : -71.2659951
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 42.3007197802915,
                  "lng" : -71.26464611970849
               },
               "southwest" : {
                  "lat" : 42.2980218197085,
                  "lng" : -71.26734408029149
               }
            }
         },
         "place_id" : "ChIJ7xQZi0GB44kRiWrnmTgf904",
         "types" : [ "establishment", "point_of_interest" ]
      }
   ],
   "status" : "OK"

}

print(json_example['results'][0]['address_components'][0]['long_name'])
print(type(json_example['results']))

print(json_example['results'][0]['address_components'][5]['short_name'])
print(type(json_example['results']))

print(len(json_example['results']))