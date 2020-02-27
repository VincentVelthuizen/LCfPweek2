walking_speed = 5   # km/h
biking_speed = 15   # km/h
driving_speed = 50  # km/h

walking_extra_time = 5      # minutes
biking_extra_time = 10      # minutes
driving_extra_time = 20     # minutes

travel_distance = int(input("How far will you travel today in km"))     # km

walking_time = (travel_distance / walking_speed) * 60 + walking_extra_time  # minutes
biking_time = (travel_distance / biking_speed) * 60 + biking_extra_time     # minutes
driving_time = (travel_distance / driving_speed) * 60 + biking_extra_time   # minutes

print("Walking", int(walking_time // 60), "hours and", int(walking_time % 60), "minutes")
print("Biking", int(biking_time // 60), "hours and", int(biking_time % 60), "minutes")
print("Driving", int(driving_time // 60), "hours and", int(driving_time % 60), "minutes")