import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Set of locations
num_locations = 100
K = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(num_locations)]

# Users not associated with a DBS
num_users = 500
I1 = [(random.randint(0, 99), random.randint(0, 99), pathloss) for _ in range(num_users) for pathloss in [50, 60, 70, 80, 90]]

# Users already associated with a DBS
I2 = []

# DBS locations
dbs_locations = []

# User-DBS associations
user_dbs_map = {}

def find_lowest_pathloss_user(I1):
    return min(I1, key=lambda user: user[2])

def get_user_association_radius(pathloss_requirement):
    # Calculate r_max based on Eq. 4
    return math.sqrt(pathloss_requirement / math.pi)

def place_dbs(h, i_bar):
    max_users = 0
    best_location = None
    
    for k in K:
        x, y = k
        users_in_range = [(x_, y_, p_) for x_, y_, p_ in I1 if (x - x_)**2 + (y - y_)**2 <= get_user_association_radius(i_bar[2])**2]
        if len(users_in_range) > max_users:
            max_users = len(users_in_range)
            best_location = k
    
    if best_location is None:
        return None, 0
    else:
        return best_location, max_users

# Set the DBS altitude
h_bar = 10

while I1:
    i_bar = find_lowest_pathloss_user(I1)
    dbs_location, num_users = place_dbs(h_bar, i_bar)
    
    if dbs_location is None:
        print("No suitable location found to place DBS.")
        break
    
    # Update I1, I2, DBS locations, and user-DBS associations
    associated_users = [(x_, y_, p_) for x_, y_, p_ in I1 if (x_ - dbs_location[0])**2 + (y_ - dbs_location[1])**2 <= get_user_association_radius(i_bar[2])**2]
    I2.extend(associated_users)
    I1 = [user for user in I1 if user not in associated_users]
    dbs_locations.append(dbs_location)
    
    for user in associated_users:
        if user not in user_dbs_map:
            user_dbs_map[user] = len(dbs_locations)
    
    print(f"DBS placed at {dbs_location} with {num_users} users in range.")

print(f"All users associated with a DBS. I1 is empty: {not I1}")

# Visualize user and DBS locations
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('User and DBS Locations')

# Plot user locations colored by DBS association
for user in I1 + I2:
    if user in user_dbs_map:
        ax.scatter(user[0], user[1], color=f'C{user_dbs_map[user]}', s=50)
    else:
        ax.scatter(user[0], user[1], color='gray', s=50)

# Plot DBS locations
dbs_x, dbs_y = zip(*dbs_locations)
ax.scatter(dbs_x, dbs_y, color='red', marker='x', s=100, label='DBS')

ax.legend()
plt.show()