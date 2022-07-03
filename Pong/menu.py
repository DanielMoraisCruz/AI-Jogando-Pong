import pygame

from Pong.globais import BLACK, DISPLAY_SIZE


class Menu():
    def __init__(self, game) -> None:
        self.game = game
        self.mid_w = DISPLAY_SIZE[0]/2
        self.mid_h = DISPLAY_SIZE[1]/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.main_menux = DISPLAY_SIZE[0]/2
        self.main_menuy = DISPLAY_SIZE[1]/2 - 20
        self.startx, self.starty = self.mid_w, self.mid_h+30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h+50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h+70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(BLACK)
            self.game.draw_text(
                'Main Menu', 20, self.main_menux, self.main_menuy)
            self.game.draw_text("StartGame", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.widtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.widtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.widtop = (
                    self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.widtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.widtop = (
                    self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.widtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            pass
