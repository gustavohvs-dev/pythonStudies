from sys import path
path.append(__file__ + "\\..\\app")

import controllers.controller1 as Controller1
import models.Model2 as Model2

print(Controller1.function())
print(Model2.function())