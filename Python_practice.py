#counties = ["Arapahoe", "Denver", "Jefferson"]  
# #print(counties[0:2]) #list[start:end] does not return end.. value 0:2 returns 0:1
#list.append()
#list.insert(index, obj)
#list.remove(obj)
#list.pop(index)

#Dictionaries
    #Keys() returns all keys
    #items() returns keys and values
    #values() returns all values
    #get(key) returns value

    #can make list of dictionaries *good for CSV files. 

#voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#voting_data[1] = {"county" : "El Paso", "registered_voters" : 461149}
#voting_data.pop(0)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county,votes in counties_dict.items():
    #print(f"{county} county has {votes} registered voters.")
print(f"{counties_dict.get('Arapahoe')}")