cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_space_per_car = passengers / cars_driven
car_capacity = cars - space_in_a_car - drivers + passengers 

print "there are",cars,"car available"
print "there are only drivers",drivers,"drivers available"
print "there will b ",car_not_driven,"empty cars today"
print "we can transport",carpool_capacity,"people today"
print "we have",passengers,"to carpool today"
print "we need to put about",average_space_per_car,"in each car"
print "this is just to check weather it is working fine or not ",car_capacity
