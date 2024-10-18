# **Dictionary Comprehension**
Create dictionaries using an expression can replace for loop and certain lambda functions

**Syntax:**
* `dictionary = {key: expression for {key,value} in iterable}`
* `dictionary = {key: expression for {key,value} in iterable if conditional}`
* `dictionary = {key: (if/else) for {key,value} in iterable}`
* `dictionary = {key: function(value) for {key, value} in iterable}`

```py
cities_in_F = {'New York': 32, 'Boston': 22, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: ((value - 32)+(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

Weather = {'New York': 'Snowing', 'Boston': 'Rainy', 'Los Angeles': 'Sunny', 'Chicago': 'Cloudy'}
sunny_weather = {key: value for (key,value) in Weather.items() if value == 'Sunny'}
print(sunny_weather)

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities_in_F.items()}
print(desc_cities)

desc_cities_1 = {key: check_temp(values) for (key,values) in cities_in_F.items()}
print(desc_cities_1)
def check_temp(values):
	if values>=70:
		return "HOT"
	elif 69<=values>=40:
		return "WARM"
	else:
		return "COLD"
```