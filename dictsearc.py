d={
 "India" : {
 "Karnataka" : ["Bangalore", "Mysore"],
 "Maharashtra" : ["Mumbai", "Pune"]
 },
 "USA" : {
 "Texas" : ["Dallas", "Houston"],
 "IL" : ["Chicago", "Aurora", "Pune"]
 }
}

for i in d.values():
    #print(i)
    for j in i.values():
       # print(j)
        k=j
       # print(k)
        for l in k:
            if(l=="Pune"):
                d.get(l)
                
            