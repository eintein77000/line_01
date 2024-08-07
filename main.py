def Gripper_closed():
    global angle, executionFlag
    maqueen.motor_stop(maqueen.Motors.ALL)
    angle = 100
    maqueen.servo_run(maqueen.Servos.S1, angle)
    basic.pause(1000)
    executionFlag = 1
def Gripper_Open():
    global angle, executionFlag, ultrasonicFlag
    maqueen.motor_stop(maqueen.Motors.ALL)
    angle = 30
    maqueen.servo_run(maqueen.Servos.S1, angle)
    basic.pause(1000)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 120)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)
    basic.pause(500)
    executionFlag = 1
    ultrasonicFlag = 1
distance = 0
ultrasonicFlag = 0
executionFlag = 0
angle = 0
angle = 30
maqueen.servo_run(maqueen.Servos.S1, angle)
executionFlag = 1
ultrasonicFlag = 1

def on_forever():
    global distance, executionFlag, ultrasonicFlag
    distance = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    if ultrasonicFlag == 1:
        if distance <= 6 and distance != 0:
            executionFlag = 2
            ultrasonicFlag = 0
        else:
            executionFlag = 1
    if executionFlag == 1:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 100)
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 20)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 160)
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 160)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            executionFlag = 3
    if executionFlag == 2:
        Gripper_closed()
    if executionFlag == 3:
        Gripper_Open()
basic.forever(on_forever)
