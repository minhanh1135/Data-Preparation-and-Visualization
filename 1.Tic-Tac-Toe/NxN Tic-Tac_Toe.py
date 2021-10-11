import pygame, sys
import numpy as np

pygame.init()

class XO_Game():
    def __init__(self, cell_number, player):
        self._line_color = (23,145,135)
        self.player = player
        self._space = 600/ cell_number
        self._number_cells = cell_number

    def draw_lines(self,number_cells):
        #horizontal
        temp_space = 600/number_cells
        space = temp_space
        for i in range(number_cells):
            pygame.draw.line(screen, self._line_color, (0,space), (600,space), 5)
            pygame.draw.line(screen, self._line_color, (space, 0), (space, 600), 5)
            space += temp_space

    def mark_square(self, row, column, player):
        board[row][column] = player

    def available_square(self, row, column):
        if board[row][column] == 0:
            return True
        else:
            return False

    def is_board_full(self):
        for r in range(cell_number):
            for c in range(cell_number):
                if self.available_square(r,c):
                    return False
        return True

    def draw_XO(self):
        temp= self._space/ 4
        temp2 = self._space/2
        for r in range(cell_number):
            for c in range(cell_number):
                if board[r][c] == 1:
                    pygame.draw.circle(screen,(250,0,0), (int(c * self._space + self._space / 2), int(r * self._space + self._space / 2)),self._space//5,5)
                elif board[r][c] == 2:
                    pygame.draw.line(screen, (250,0,0), (c * self._space + temp, r*self._space + temp), ((c+1)*self._space- temp, (r+1)* self._space - temp), 5)
                    pygame.draw.line(screen, (250,0,0), ((c+1)* self._space - temp, r* self._space+ temp), (c*self._space + temp, (r+1)*self._space - temp) , 5)

    def check_winner(self, player):
        for cell in range(0,cell_number):
            for i in range(2):
                if board[cell,i] == player and board[cell, i+1] == player and board[cell, i+2] == player:
                    # self.draw_winning_line("row",cell,i, player)
                    return True
                if board[i, cell] == player and board[i+1, cell] == player and board[i+2, cell] == player:
                    # self.draw_winning_line("column",cell,i, player)
                    return True


        for c in range(1,cell_number-1):
            for r in range(1,cell_number-1):
                if board[r,c] == player and board[r-1,c-1] == player and board[r+1,c+1] == player:
                    # self.draw_winning_line('diagonal_right',r,c, player)
                    return True
                elif board[r+1,c-1] == player and board[r,c] == player and board[r-1, c+1] == player:
                    # self.draw_winning_line('diagonal_left',r,c, player)
                    return True

        return False

    def draw_winning_line(self,line_type,cell,i, player):
        if line_type == 'column':
            posX = cell * self._space + self._space/2
            pygame.draw.line(screen,(250,0,0), (posX, (i-1)*self._space + self._space/2), (posX, (i+2)* self._space - self._space/2))
        elif line_type == "row":
            posY = cell * self._space + self._space/2
            pygame.draw.line(screen, (250,0,0), ((i-1)*self._space+ self._space/2, posY),((i+2)*self._space - self._space/2 , posY))
        elif line_type == 'diagonal_right':
            row = cell
            col = i
            print("diagonal left row= {}, col={}".format(row,col))
            pygame.draw.line(screen, (250,0,0), ((row-1)*self._space+self._space/2, (col-1)*self._space + self._space/2), ((row+1)*self._space +self._space/2, (col+1)*self._space +self._space/2))
        elif line_type == 'diagonal_left':
            row = cell
            col = i
            pygame.draw.line(screen, (250,0,0), ((row+1)*self._space- self._space/2, (col-1)*self._space+self._space/2), ((row-1)*self._space+self._space/2, (col+1)*self._space-self._space/2))

    def restart_game(self):
        screen.fill((28, 170, 156))
        self.draw_lines()
        board = np.zeros(cell_number)

    def play(self):
        player = self.player
        game_over = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    (mouseX, mouseY) = (event.pos[1], event.pos[0])

                    (clicked_row, clicked_col) = (int(mouseX /self._space), int(mouseY/self._space))
                    if self.available_square(clicked_row, clicked_col):
                        if player == 1:
                            self.mark_square(clicked_row, clicked_col, 1)
                            if self.check_winner(player):
                                game_over = True
                            player = 2
                        elif player == 2:
                            self.mark_square(clicked_row,clicked_col, 2)
                            if self.check_winner(player):
                                game_over= True
                            player = 1

                        self.draw_XO()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart_game()
                        game_over = False

            pygame.display.update()


if __name__ == '__main__':
    cell_number = int(input("Please Enter the Size of Board you want to Play with:"))
    player = 1
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('XOXO')
    screen.fill((28, 170, 156))
    board = np.zeros((cell_number, cell_number))
    game = XO_Game(cell_number, player)
    game.draw_lines(cell_number)
    game.draw_XO()
    game.play()
