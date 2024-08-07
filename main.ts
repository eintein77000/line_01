function Gripper_closed () {
    maqueen.motorStop(maqueen.Motors.All)
    angle = 100
    maqueen.servoRun(maqueen.Servos.S1, angle)
    basic.pause(1000)
    executionFlag = 1
}
function Gripper_Open () {
    maqueen.motorStop(maqueen.Motors.All)
    angle = 30
    maqueen.servoRun(maqueen.Servos.S1, angle)
    basic.pause(1000)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 120)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 40)
    basic.pause(500)
    executionFlag = 1
    ultrasonicFlag = 1
}
let distance = 0
let ultrasonicFlag = 0
let executionFlag = 0
let angle = 0
angle = 30
maqueen.servoRun(maqueen.Servos.S1, angle)
executionFlag = 1
ultrasonicFlag = 1
basic.forever(function () {
    distance = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (ultrasonicFlag == 1) {
        if (distance <= 6 && distance != 0) {
            executionFlag = 2
            ultrasonicFlag = 0
        } else {
            executionFlag = 1
        }
    }
    if (executionFlag == 1) {
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 100)
        }
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 20)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 160)
        }
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 160)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
        }
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
            executionFlag = 3
        }
    }
    if (executionFlag == 2) {
        Gripper_closed()
    }
    if (executionFlag == 3) {
        Gripper_Open()
    }
})
