import pygame

from Pong.globais import BLACK, DISPLAY_SIZE, WINDOW


class Menu():
    def __init__(self, game) -> None:
        self.game = game
        self.mid_w = DISPLAY_SIZE[0]/2
        self.mid_h = DISPLAY_SIZE[1]/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("X", 50, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        WINDOW.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.main_menux = DISPLAY_SIZE[0]/2
        self.main_menuy = DISPLAY_SIZE[1]/2 - 50
        self.startx, self.starty = self.mid_w, self.mid_h + 15
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 45
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 75
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text(
                'Main Menu', 70, self.main_menux, self.main_menuy)
            self.game.draw_text("StartGame", 50, self.startx, self.starty)
            self.game.draw_text("Options", 50, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 50, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Options":
                pass
            elif self.state == "Credits":
                pass
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game) -> None:
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text(
                "Options", 50, self.main_menux, self.main_menuy)
            self.game.draw_text("Volume",  50, self.volx, self.voly)
            self.game.draw_text("Controls", 50, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.