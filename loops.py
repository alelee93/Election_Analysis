x = 0

while x <=5:
    print(x)
    x = x + 1


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)


for i in counties_dict:
    print(i)

for county, voters in counties_dict.items():
    #print(county + " has " + str(voters) + " registered voters ")
    print(f"{county} county has {voters} registered voters" )



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict["registered_voters"])