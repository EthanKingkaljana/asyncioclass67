import asyncio
import math

# พิกัดของตำแหน่งอ้างอิง
ref_x, ref_y = 3, 3

# พิกัดของจุดที่ต้องการคำนวณระยะทาง
points = [(1, 2), (2, 8), (3, 7), (4, 6), (6, 9), (7, 4), (5, 3), (8, 2), (6, 1), (3, 5)]

async def calculate_distance(point):
    x, y = point
    distance = math.sqrt((x - ref_x) ** 2 + (y - ref_y) ** 2)
    return (point, distance)

async def gather_distances():
    # Gather distances using asyncio.gather
    distances = await asyncio.gather(*(calculate_distance(point) for point in points))
    return distances

# Use asyncio.run to run the coroutine
distances_with_points = asyncio.run(gather_distances())

# หาระยะที่ใกล้ที่สุดและไกลที่สุด
min_distance_value = min(distances_with_points, key=lambda x: x[1])[1]
max_distance_value = max(distances_with_points, key=lambda x: x[1])[1]

# Find all points with the minimum distance
closest_points = [point for point, distance in distances_with_points if distance == min_distance_value]
# Find all points with the maximum distance
farthest_points = [point for point, distance in distances_with_points if distance == max_distance_value]

print("ระยะที่ใกล้ที่สุด:", closest_points, "ค่า:", min_distance_value)
print("ระยะที่ไกลที่สุด:", farthest_points, "ค่า:", max_distance_value)

# Output all points with their distances
for point, distance in distances_with_points:
    print(f"พิกัด {point} ระยะทาง: {distance}")
