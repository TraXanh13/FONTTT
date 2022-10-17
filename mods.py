import Components.sounds as sounds


def inverseControls(player, *_):
    sounds.playInverseControlSound()
    player.changeSpeed(-player.speed)


def shrinkPaddle(player, op, ball):
    sounds.playShrinkSound()
    if (ball.getBallDirection() and player.getHeight() > 50):
        player.changeHeight(-player.getHeight() * .25)
    elif (not ball.getBallDirection() and op.getHeight() > 50):
        op.changeHeight(-player.getHeight() * .25)


def growPaddle(player, op, ball):
    sounds.playGrowSound()
    if (not ball.getBallDirection() and player.getHeight() < 200):
        player.changeHeight(player.getHeight() * .15)
    elif (ball.getBallDirection() and op.getHeight() < 200):
        op.changeHeight(op.getHeight() * .15)


def slowMotion(player, op, ball):
    sounds.playSlowDownSound()
    if (ball.getBallDirection() and player.getSpeed() > 3):
        player.changeSpeed(player.getSpeed() * .75)
    elif (not ball.getBallDirection() and op.getSpeed() > 3):
        op.changeSpeed(op.getSpeed() * .75)


def speedUp(player, op, ball):
    sounds.playSpeedUpSound()
    if (ball.getBallDirection() and op.getSpeed() < 15):
        op.changeSpeed(op.getSpeed() * 1.25)
    elif (not ball.getBallDirection() and player.getSpeed() < 15):
        player.changeSpeed(player.getSpeed() * 1.25)


def fastBall(player, op, ball):
    sounds.playFastBallSound()
    if (ball.getSpeedX() < 15 and ball.getSpeedY() < 15):
        ball.changeBallSpeed(ball.getSpeedX() * 1.15,
                             ball.getSpeedY() * 1.15)

