import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 5), (8, 3), (2, 1)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
