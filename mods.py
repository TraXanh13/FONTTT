import pygame

def inverseControls(player, *_):
    player.changeSpeed(-player.speed)


def shrinkPaddle(player, op, ball):
    if (ball.getBallDirection() and player.getHeight() > 50):
        player.changeHeight(-player.getHeight() * .25)
    elif (not ball.getBallDirection() and op.getHeight() > 50):
        op.changeHeight(-player.getHeight() * .25)


def growPaddle(player, op, ball):
    if (not ball.getBallDirection() and player.getHeight() < 300):
        player.changeHeight(player.getHeight() * 1.25)
    elif (ball.getBallDirection() and op.getHeight() < 300):
        op.changeHeight(player.getHeight() * 1.25)


def slowMotion(player, op, ball):
    if (ball.getBallDirection() and player.getSpeed() > 3):
        player.changeSpeed(player.getSpeed() * .75)
    elif (not ball.getBallDirection() and op.getSpeed() > 3):
        op.changeSpeed(op.getSpeed() * .75)


def speedUp(player, op, ball):
    if (ball.getBallDirection() and op.getSpeed() < 15):
        op.changeSpeed(op.getSpeed() * 1.25)
    elif (not ball.getBallDirection() and player.getSpeed() < 15):
        player.changeSpeed(player.getSpeed() * 1.25)


def fastBall(player, op, ball):
    if (ball.getBallDirection()):
        ball.changeSpeed(ball.getSpeed() * 1.15)
    else:
        ball.changeSpeed(ball.getSpeed() * -1.15)