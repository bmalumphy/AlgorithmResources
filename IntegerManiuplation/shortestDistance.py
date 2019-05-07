import numpy as np

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        #naively we can brute force it, but lets not
        #the struggle with the hashMap is repeats in distances, another alternative 
        #might be better
        #will attempt this again off the session
        shortestDistances = {}
        #lol
        pointCollection = []
        x = 0
        y = 0
        distance = 0
        #print(shortestDistance)
        for i in points:
            #print(i)
            x = i[0]**2
            y = i[1]**2
            distance = np.sqrt(x+y)
            #print(distance)
            if(len(shortestDistances)<K):
                if(distance in shortestDistances):
                    hortestDistances[distance+0.00000000000001] = {0:i[0], 1:i[1]}
                else:
                    shortestDistances[distance] = {0:i[0], 1:i[1]}
                print(shortestDistances)
            elif(len(shortestDistances) == K):
                maximum = max(shortestDistances.keys())
                minimum = min(shortestDistances.keys())
                if(distance < maximum):
                    if(distance == minimum):
                        del shortestDistances[maximum]
                        shortestDistances[distance+0.00000000000001] = {0:i[0], 1:i[1]}
                        print(shortestDistances)
                    else:
                        del shortestDistances[maximum]
                        shortestDistances[distance] = {0:i[0], 1:i[1]}
                        print(shortestDistances)
                else:
                    continue
            else:
                continue
        for key in shortestDistances:
            newPoint = []
            #print(shortestDistances[key][0])
            newPoint.append(shortestDistances[key][0])
            newPoint.append(shortestDistances[key][1])
            pointCollection.append(newPoint)
        return pointCollection

                    
            
#             if(shortestDistances == 0):
#                 pointCollection.append(i)
#                 shortestDistances.append(distance)
#                 print(pointCollection)
#             for k in shortestDistances:
#             elif(shortestDistances >= distance):
#                 if(len(shortestDistances) == k):
#                     largerDistance = shortestDistances.max()
#                     index = shortestDistances.index(largerDistance)
#                     shortestDistances.remove(largerDistance)
#                     shortestDistances.append(distance)
#                     pointsCollection[index] = i
#                     print(pointCollection)
                    
#                 else:
#                     pointCollection = []
#                     pointCollection.append(i)
#                     shortestDistances.append(distance)
#                     print(pointCollection)
            
        return pointCollection

