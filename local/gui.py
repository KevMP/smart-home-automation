from database import Database
## Here are the functions from the Database class you will be using,
def Example_CreatingTheProfile():
    ## get random id number
    id = 0
    Database().setCurrentProfile(id) ## 0 is the identification number
    Database().setMinimumPreferredTemperature(id, 70)
    Database().setMaximumPreferredTemperature(id, 75)

def Example_GettingTheProfiles():
    profile_array = Database().getAllProfilesAsArray()
    for profile in profile_array:
        minimumTemp = Database().getMinimumPreferredTemperature(profile)
        maximumTemp = Database().getMaximumPreferredTemperature(profile)
        ## Do your GUI magic here to write it to your profile section on load.
