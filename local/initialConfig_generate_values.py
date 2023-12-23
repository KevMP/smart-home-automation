from class_profile import Profile

def fakeProfileData():
    bob = Profile("default")
    bob.setMinTemp(72)
    bob.setMaxTemp(75)
    bob.updateDatabase()

    away = Profile("away")
    away.setMinTemp(68)
    away.setMaxTemp(74)
    away.updateDatabase()

    cat = Profile("cat")
    cat.setMinTemp(74)
    cat.setMaxTemp(74)
    cat.updateDatabase()

def fakeGuiData():
    pass

fakeProfileData()