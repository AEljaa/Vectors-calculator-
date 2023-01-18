import math
vec_1=[]
vec_2=[]

def Menu():
    print("Welcome to the vector calculator")
    print("1. Dot Product Calcultaor")
    print("2. Cross Product Calculator")
    print("3. Shortest distance betwwen a point and a plane Calculator")
    print("4. Angle between 2 vectors, a plane and a vector or 2 planes")
    print("")
    choice=int(input("Which mode would you like to use?\n"))
    if choice==1:
        key=True
        dot_product(key)
    
    
    
    if choice==2:
        cross_product()

    if choice==3:
        shortest_distance_point_and_plane()

    if choice==4:
        angle_between_vectors_or_planes()
    

def direction_vec():
    for i in range (0,3):
        x=int(input("Enter the direction vector (x then y then z ) this could be the direction vector of a line or the normal of a plane "))
        vec_1.append(x)
    for i in range (0,3):
        x=int(input("Enter the second direction vector (x then y then z ) this could be the direction vector of a line or the normal of a plane "))
        vec_2.append(x)
    

def dot_product(key):
    direction_vec()
    i=0
    dot_prod=0
    while i<len(vec_1):
        dot_prod+=(vec_1[i]*vec_2[i])
        i+=1
    if key:
        print("The dot product is ",dot_prod)
    return [dot_prod]





def cross_product():
    direction_vec()
    d2vec_array=[]
    cross_prod=[]
    d2vec_array.append(vec_1)
    d2vec_array.append(vec_2)
    cross_prod.append((d2vec_array[0][1]*d2vec_array[1][2])-(d2vec_array[0][2]*d2vec_array[1][1]))
    cross_prod.append((d2vec_array[0][2]*d2vec_array[1][0])-(d2vec_array[0][0]*d2vec_array[1][2]))
    cross_prod.append((d2vec_array[0][0]*d2vec_array[1][1])-(d2vec_array[0][1]*d2vec_array[1][0]))
    print(cross_prod)

def shortest_distance_point_and_plane():
    position=[]
    for i in range (0,3):
        x=int(input("Enter the position vector of the point (x then y then z ) "))
        position.append(x)
    plane=[]
    for i in range (0,4):
        x=int(input("Enter the equation of the plane  (x then y then z then d Ax +By +Cz = D) "))
        plane.append(x)

    distance=abs((plane[0]*position[0]+plane[1]*position[1]+plane[2]*position[2]-plane[3])/(plane[0]**2+plane[1]**2+plane[2]**2)**0.5)
    print(distance)


def angle_between_vectors_or_planes():
    DotProd=dot_product(False)[0]
    choice=int(input("Angle between 2 lines(press 1), Angle between a line and a plane(press 2), Angle between 2 planes(3)?\n"))
    angle=math.acos(DotProd/((vec_1[0]**2+vec_1[1]**2+vec_1[2]**2)**0.5 * (vec_2[0]**2+vec_2[1]**2+vec_2[2]**2)**0.5))
    if choice==2:
        angle=math.pi/2-angle
    degrees=(angle*180)/math.pi
    print(angle,"which is also",degrees,"degrees")



Menu()
