import pygame

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