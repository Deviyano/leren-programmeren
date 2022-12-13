from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop()
robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop()
robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop()
robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.moveLeft(),robotArm.grab(),robotArm.moveRight(),robotArm.moveRight(),robotArm.moveRight(),robotArm.drop()
robotArm.moveLeft(),robotArm.moveLeft(),robotArm.grab(),robotArm.moveRight(),robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()