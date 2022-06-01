from datetime import time
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room} on floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


class Drivers(models.Model):
    firstname = models.CharField(max_length=50)
    mi = models.CharField(max_length=1, blank=True, null=-True)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=-True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    driverid = models.CharField(max_length=6)
    licensenumber = models.CharField(max_length=20)
    licensestate = models.CharField(max_length=50)
    # licenceseclass = models.CharField(max_length=50)
    carrier = models.CharField(max_length=50)
    primaryruleset = models.CharField(max_length=50)
    secondaryruleset = models.CharField(max_length=50, blank=True, null=-True)
    autoapply = models.CharField(max_length=50)
    allowpc = models.CharField(max_length=3)
    allowym = models.CharField(max_length=3)
    accttype = models.CharField(max_length=1)
    type = models.CharField(max_length=50)
    updatedby = models.CharField(max_length=50)
    hiredate = models.DateField()
    senirotydate = models.DateField()
    dob = models.DateField()
    rate = models.CharField(max_length=6)
    shift = models.CharField(max_length=5)
    type = models.CharField(max_length=6)
    kind = models.CharField(max_length=6)
    ss = models.CharField(max_length=5)
    companycode = models.CharField(max_length=6)
    division = models.CharField(max_length=3)
    domicilecode = models.CharField(max_length=3)
    fleet = models.CharField(max_length=6)
    teamlead = models.CharField(max_length=3)
    terminalcode = models.CharField(max_length=4)
    country = models.CharField(max_length=3)
    branch = models.CharField(max_length=20)


def __str__(self):
    return f"Details for driver: {self.firstname}  {self.lastname} from {self.branch}"
