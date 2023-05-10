area_temperature = [80,81,40] ## area temp and house temp have to be equal in array size
house_temperature = [75,76,45]
energy_runtime = 0.00 ## we could do time in minutes, or just seconds '0'
desired_temperature = 75

data = [
    area_temperature,
    house_temperature,
    energy_runtime, ## we also have to make this into an array and append to itself,
                    ## if we want the program to survive, probably.
                    ## and
                    ## [desired_temperature * length of the house_temperature or area_temperature],
                    ## keep the size equal so our program doesn't blank itself.
]

## we could also just make it into one line,
## could be easier, maybe. anyhow here's an example.

input_data = [65, 68, 60, 20]