import pygame
import ui
import mglobals
import utils
from player import Player
from wheel import Wheel
from time import sleep


def game_loop():

    player = Player(mglobals.PLAYER)
    wheel = Wheel()
    player_ui = ui.PlayerUI()
    event_ui = ui.EventUI()
    player_ui.update(player.cash, player.heart, player.face)
    msg_ui = ui.MsgUI()

    utils.draw_board()
    player.render()
    player_ui.render()

    while True:

        event_ui.update(player.position)
        if player.position in mglobals.CellTypes.MSG.value and player.round > 0:
            msg_ui.update(player.position)
            msg_ui.play()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_RETURN:
                    wheel.spin()
                    wheel.show()

                    # Move the player token across the board
                    for _ in range(wheel.number):
                        utils.draw_board()
                        player_ui.render()
                        player.advance(1)
                        event_ui.update(player.position)
                        if player.round > mglobals.ZERO:
                            sleep(0.4)
                            break
                        sleep(0.4)
                        pygame.display.update()

            event_ui.play()
        pygame.display.update()
        mglobals.CLK.tick(30)


def main():
    mglobals.init()
    ui.draw_start_screen()
    ui.draw_char_select_screen()
    #ui.init_centre_displays()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

