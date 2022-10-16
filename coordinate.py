#***time wasted on this program: 8 hours

import math
from random import *

#***file opening
path = "/Users/User/Downloads/coordinates.csv"

with open (path, 'r') as coordinates:
    data = coordinates.read()
data = list(data.split("\n"))[:-1]

for x in range(len(data)):
    data[x]=list(data[x].split(","))
    data[x][0], data[x][1] = float(data[x][0]), float(data[x][1])
#print(type(a_ra))

#***function

#***return the distance between p1 and p2, p1 and p2 must be a list
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

#***return a random point on the massive list of point
def random_point():
    return data[randint(0,len(data)-1)]

#***return the centroid value given a list of points, points must be in list form
def calculate_centroid(list_of_points):
    xtotal=0.0
    ytotal=0.0
    for x in list_of_points:
        xtotal+=x[0]
        ytotal+=x[1]
    return [xtotal/len(list_of_points), ytotal/len(list_of_points)]

#***return a list of all the points, which centroid they are close to 
def pre_centroid_loop(all_points, list_of_index, list_of_centroid):
    distance_from_closest_point = []
    total_distance = 0.0
    for x in range(len(all_points)):
        point_distance = []
        for y in list_of_index:
            point_distance.append(distance(all_points[x],list_of_centroid[y]))
        distance_from_closest_point.append([list_of_centroid[point_distance.index(min(point_distance))],point_distance.index(min(point_distance))])
        total_distance+=min(point_distance)**2
        #print(total_distance)
        point_distance.clear()
    print("the total distance for this loop is  " + str(total_distance))
    return distance_from_closest_point

#***return a boolean value to see if we need to reassign new value or not
def pre_centroid_loop_check(length_of_data,current_list_of_distance, previous_list_of_distance, list_of_index, status):
    for x in range (length_of_data):
        for y in list_of_index:
            if current_list_of_distance[y][1] == previous_list_of_distance[y][1]:
                status = True
            else:
                status = False
                break
        if status == False:
            break
    return status

#***return a dictionary of 3 centroid value
def calc_centroid_loop(all_points,list_of_distances, list_of_index, dictionary_of_distance, dictionary_of_centroid):
    for x in range(len(list_of_distances)):
        for y in list_of_index:
            if list_of_distances[x][1] == y:
                dictionary_of_distance["list_of_points_closest_to_{0}".format(y)].append(all_points[x])
    for x in index:
        dictionary_of_centroid["centroid_of_cluster_{0}".format(x)] = calculate_centroid(dictionary_of_distance["list_of_points_closest_to_{0}".format(x)])
    return dictionary_of_centroid


#main code here

#***this part is obtaining the amount of cluseter the user want

#***This part is simply getting the minimum distances and storing which cluster is the point the closest to into a list
'''for x in range(len(data)):
    point_distance = []
    for y in all_random_points:
        point_distance.append(distance(data[x],y))
    distance_from_closest_point.append([all_random_points[point_distance.index(min(point_distance))],point_distance.index(min(point_distance))])
    total_distance+=min(point_distance)**2
    point_distance.clear()
print(total_distance)
'''

#***this will be the part where we try to calculate the centroid point
'''for x in range(len(distance_from_closest_point)):
    for y in index:
        if distance_from_closest_point[x][1] == y:
            distance_dictionary["list_of_points_closest_to_{0}".format(y)].append(data[x])

for x in index:
    centroid_dictionary["centroid_of_cluster_{0}".format(x)] = calculate_centroid(distance_dictionary["list_of_points_closest_to_{0}".format(y)])

#print(distance_dictionary)
print(centroid_dictionary)
'''

#*** this will be us trying to recalculate the new distance
'''for x in range(len(data)):
    point_distance = []
    for y in index:
        point_distance.append(distance(data[x], centroid_dictionary["centroid_of_cluster_{0}".format(y)]))
    print(point_distance)
    point_distance.clear()
'''

#*** This will be the recursion/looping part

#***main code here
all_random_points = []
index = []
current_distance_from_closest_point = []
prev_distance_from_closest_point = []
distance_dictionary = {}
centroid_dictionary = {}
centroid_list = []
done = False

#***this part is obtaining the amount of cluseter the user want
number_of_cluster = int(input("Enter the number of cluster: "))
for x in range(number_of_cluster):
    all_random_points.append(random_point())
    index.append(x)
    distance_dictionary["list_of_points_closest_to_{0}".format(x)] = []
    centroid_dictionary["centroid_of_cluster_{0}".format(x)] = []

#***This part is simply getting the minimum distances and storing which cluster is the point the closest to into a list
current_distance_from_closest_point = pre_centroid_loop(data, index, all_random_points)

#***this will be the part where we try to calculate the centroid point
centroid_dictionary = calc_centroid_loop(data, current_distance_from_closest_point, index, distance_dictionary,centroid_dictionary)

#***this will be us trying to recalculate the new distance, new centroid and repeat process
while done != True:
    #***this part is basically converting the dictionary into a list
    centroid_list.clear()
    for x in index:
        centroid_list.append(centroid_dictionary["centroid_of_cluster_{0}".format(x)])
    
    #**recursion begins here
    prev_distance_from_closest_point = current_distance_from_closest_point
    #print(current_distance_from_closest_point[-1])
    current_distance_from_closest_point = pre_centroid_loop(data, index, centroid_list)
    done = pre_centroid_loop_check(len(data), current_distance_from_closest_point, prev_distance_from_closest_point, index, done)
    centroid_dictionary = calc_centroid_loop(data, current_distance_from_closest_point, index, distance_dictionary,centroid_dictionary)

#***tell us the answer above is the answer
print("the record above this is answer")