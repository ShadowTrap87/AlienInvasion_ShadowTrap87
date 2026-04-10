"""
Program: arsenal.py
Author: Kennett Aguilar-Zaldana
Purpose: Defines the Arsenal class which manages the collection of bullets 
fired by the player's ship.
Starter Code: None
Date: 04/08/26
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Arsenal:
    """Manages the group of active bullets fired by the player's ship.
    """
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the arsenal with an empty bullet group.

        Args:
            game (AlienInvasion): The main AlienInvasion game instance.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update all bullet positions and remove any that have left the screen.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove bullets that have moved off the top of the screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all active bullets to the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire a new bullet if the bullet limit has not been reached.

        Returns:
            bool: True if a bullet was created and added, False if at the limit.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False