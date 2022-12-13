from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)


# Jouw python instructies zet je vanaf hier:
nummer=1
while robotArm.grab()==True:
    for x in range(nummer):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(nummer):
        robotArm.moveLeft()
    nummer=nummer+1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()