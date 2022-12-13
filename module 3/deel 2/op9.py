from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 5
# Jouw python instructies zet je vanaf hier:
for x in range(3):
    robotArm.moveRight()
for x in range (4):
    robotArm.grab(), robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft()
robotArm.moveLeft()
for x in range(3):
    robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft()
robotArm.moveLeft()
for x in range(2):
    robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()