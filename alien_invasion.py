import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
##from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    # Initialize pygame, settings,  and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height), ai_settings.resizable)
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)


    # Make a ship, group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Make an alien.
    ##alien = Alien(ai_settings, screen)

    # Start the main loop for the game.
    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
            play_button)

run_game()