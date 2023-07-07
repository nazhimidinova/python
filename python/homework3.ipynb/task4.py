connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

count = 0
total_time = 0

for connection in connections:
    city_from, city_to, time = connection
    if city_to == 'Rome':
        count += 1
        total_time += time

average_time = total_time / count if count > 0 else 0

print("{} connections lead to Rome with an average flight time of {} minutes".format(count, average_time))


    