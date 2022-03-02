# Activity selection algorithm

# The method returns the optimal position for base station placement
# using the activity selection algorithm
def optimal_base_station(house_dist):
    bs_placement = []
    bs_placement.append( house_dist[0] + 8)
    print(house_dist[1])
    count = 0
    for m in range(1,len(house_dist)):
        if house_dist[m] > bs_placement[count] + 8:
            bs_placement.append(house_dist[m]+8)
            count+=1

    return bs_placement

house_dist = [5,6,7,20,25,30,42,70,72]
bs_placement = optimal_base_station(house_dist)
print(bs_placement)
