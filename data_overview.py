area_temperature = [80,81,40] ## area temp and house temp have to be equal in array size
house_temperature = [75,76,45]
energy_runtime = 0.00 ## we could do time in minutes, or just seconds '0'
desired_temperature = 75

data = [
    area_temperature,
    house_temperature,
    energy_runtime,
    ## and
    ## [desired_temperature * length of the house_temperature or area_temperature],
    ## keep the size equal so our program doesn't blank itself.
]