"""
Program: bullet.py
Author: Kennett Aguilar-Zaldana
Purpose: Defines the Bullet class which represents a single laser bullet fired 
by the player's ship.
Starter Code: None
Date: 04/08/26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represents a single bullet fired from the player's ship.

    Args:
        Sprite (pygame.sprite.Sprite): Base sprite class providing image and 
        rect attributes.
    """
    def __init__(self, game: 'AlienInvasion'):
        """Initialize a bullet at the current position of the ship's top center.

        Args:
            game (AlienInvasion): The main AlienInvasion game instance.
        """
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upward based on bullet speed setting.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet image to the screen at its current position.
        """
        self.screen.blit(self.image, self.rect)
