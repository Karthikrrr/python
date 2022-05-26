def get_key(val):
	for key, value in my_dict.items():
		if val == value:
			return key

	return "key doesn't exist"

# Driver Code

my_dict =d={
 "India" : {
 "Karnataka" : ["Bangalore", "Mysore"],
 "Maharashtra" : ["Mumbai", "Pune"]
 },
 "USA" : {
 "Texas" : ["Dallas", "Houston"],
 "IL" : ["Chicago", "Aurora", "Pune"]
 }
}

print(get_key("pune"))
print(get_key("pune"))
