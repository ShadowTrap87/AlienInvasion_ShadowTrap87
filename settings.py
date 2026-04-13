"""
Program: settings.py
Author: Kennett Aguilar-Zaldana
Purpose: Stores all configuration settings for the Alien Invasion game including 
screen dimensions, ship properties, bullet properties, and asset file paths.
Starter Code: None
Date: 04/08/26
"""

from pathlib import Path
class Settings:
    """Holds all static settings for the Alien Invasion game.
    """
    
    def __init__(self):
        """Initialize game settings for screen, ship, bullets, and assets.
        """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'pizza_bg.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'pizza_freddy.png'
        self.ship_w = 80
        self.ship_h = 80
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pizza_bullet.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 80
        self.bullet_amount = 5



