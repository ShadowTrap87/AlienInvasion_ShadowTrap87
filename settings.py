"""
Program: settings.py
Author: Kennett Aguilar-Zaldana
Purpose: Stores all configuration settings for the Alien Invasion game.
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
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'pizza_freddy.png'
        self.ship_w = 80
        self.ship_h = 80

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pizza_bullet.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'pizza_child.png'
        self.alien_w = 80
        self.alien_h = 80
        self.fleet_direction = 1

        self.button_file = Path(__file__).parent / 'Assets' / 'images' / 'pizza_start.png'
        self.button_w = 200
        self.button_h = 200
        self.button_color = (0, 136, 0)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.hud_color = (0,0,0)

        self.text_color = (255,255,255)
        self.button_font_size = 30
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'SixtyfourConvergence.ttf'

    def initialize_dynamic_settings(self):
        """Initialize settings that change as the game difficulty increases.
        """
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 80
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50 

    def increase_difficulty(self):
        """Increase game speed settings to raise difficulty each level.
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

