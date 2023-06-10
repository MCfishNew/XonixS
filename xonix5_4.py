import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QApplication, QLabel, QWidget

width = 600
height = 600
cell_size = 15
cells_in_row = width / cell_size
cells_in_col = height / cell_size
color = {0: 'lightblue', 1: 'khaki', 2: 'green', 3: 'red', 5: 'plum'}
countBot = 1
vector = None
trajectory = []
cell_dictionary = {}

# Создаем список ячеек (словарь)
for i in range(int(cells_in_col)):
    for j in range(int(cells_in_row)):
        if i == 0 or i == cells_in_col - 1 or j == 0 or j == cells_in_row - 1:
            c = 1
        else:
            c = 0
        cell_dictionary[f'{i}_{j}'] = [i, j, c]


class Player(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(cell_size, cell_size)
        # self.move(0, 0)
        self.setStyleSheet(f'background-color: {color[2]};'
                           'border: 1px solid #EEE;'
                           'padding: 0; margin: 0; ')


class Bot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(cell_size, cell_size)
        self.move(0, 0)
        self.setStyleSheet(f'background-color: {color[3]};'
                           'border: 1px solid #EEE;'
                           'padding: 0; margin: 0; ')


class RulesOfNature(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class mainMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Xonix")
        self.setStyleSheet('background: khaki;')
        self.move(500, 150)
        self.setFixedSize(600, 600)

        game_name = QLabel(self)
        game_name.resize(400, 50)
        game_name.setStyleSheet('font-size: 40px; color: white; background: black;')
        game_name.setAlignment(Qt.AlignCenter)
        game_name.setText("Xonix")
        game_name.move(100, 85)

        buttonPlay = QtWidgets.QPushButton("Играть", self)
        buttonPlay.setGeometry(100, 180, 400, 80)
        buttonPlay.setStyleSheet('border: 1px solid white; color: white; background: black;')
        buttonPlay.setFont(QFont('Arial', 14))
        buttonPlay.clicked.connect(self.switch_play)

        buttonRule = QtWidgets.QPushButton("Правила", self)
        buttonRule.setGeometry(100, 280, 400, 80)
        buttonRule.setStyleSheet('border: 1px solid white; color: white; background: black;')
        buttonRule.setFont(QFont('Arial', 14))
        buttonRule.clicked.connect(self.switch_rule)

        buttonExit = QtWidgets.QPushButton("Выйти", self)
        buttonExit.setGeometry(100, 380, 400, 80)
        buttonExit.setStyleSheet('border: 1px solid white; color: white; background: black;')
        buttonExit.setFont(QFont('Arial', 14))
        buttonExit.clicked.connect(self.switch_exit)

    def switch_play(self):
        Window.move(mainMenu.x(), mainMenu.y())
        RulesOfNature.move(mainMenu.x(), mainMenu.y())

        Window.show()
        self.hide()

    def switch_rule(self):
        Window.move(mainMenu.x(), mainMenu.y())
        # form3.move(mainMenu.x(), mainMenu.y())

        # form3.show()
        # self.hide()

    def switch_exit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.switch_exit()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.sidebar = self.sidebar()
        self.cell_color = None
        self.player = None
        self.cell = None
        self.bot = None
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        for x in range(int(cells_in_col)):
            for y in range(int(cells_in_row)):
                self.grid_layout.addWidget(self.create_cell(x, y), x, y)

        self.start_coordinates()
        self.create_bot()

        self.setWindowTitle('Xonix')
        self.setGeometry(80, 80, width, height)
        self.setLayout(self.grid_layout)
    def sidebar(self):
        sidebar = []

        bar = QLabel(self)
        bar.resize(600, 400)
        bar.setStyleSheet('font-size: 30px; color: white; background: black')
        bar.move(200, 600)
        sidebar.append(bar)
        return sidebar
    def create_cell(self, x, y):
        cell_color = cell_dictionary[f'{x}_{y}'][2]
        self.cell = QLabel()
        self.cell.resize(cell_size, cell_size)
        # self.cell.setText(str(cell_dictionary[f'{x}_{y}']))
        self.cell.setStyleSheet(f'background-color: {color[cell_color]};'
                                'border: 1px solid #EEE;'
                                'padding: 0; margin: 0; ')
        return self.cell

    # Ботяра появляется, где нужно или не нужно
    def create_bot(self):
        bots = []
        for bot in range(countBot):
            i_bot = random.randrange(1, int(cells_in_col - 1))
            j_bot = random.randrange(1, int(cells_in_row - 1))
            if i_bot != 0 or i_bot != int(cells_in_col - 1):
                i_bot = random.choice([1, int(cells_in_col - 4)])
                if j_bot == 0 or j_bot == i_bot:
                    j_bot = random.choice([1, int(cells_in_row - 4)])
            bot = Bot(self)
            self.bot = QLabel()
            self.bot.setStyleSheet(f'background-color: {color[3]}')
            self.grid_layout.addWidget(self.bot, i_bot, j_bot)
            bots.append(bot)
        return bots

    def move_bots(self):

        location_index = self.grid_layout.indexOf(self.bot)
        locationBot = self.grid_layout.getItemPosition(location_index)
        direction1 = random.choice(['left', 'right', 'up', 'down'])
        print(direction1)
        if direction1 == 'left':
            moving_left = locationBot[1] - 1
            if cell_dictionary[f'{locationBot[0]}_{locationBot[1] - 1}'][2] != 1:
                self.grid_layout.addWidget(self.bot, locationBot[0], moving_left)
            else:
                direction1 = random.choice(['right', 'up', 'down'])

        if direction1 == 'right':
            moving_right = locationBot[1] + 1
            if cell_dictionary[f'{locationBot[0]}_{locationBot[1] + 1}'][2] != 1:
                self.grid_layout.addWidget(self.bot, locationBot[0], moving_right)
            else:
                direction1 = random.choice(['left', 'up', 'down'])

        if direction1 == 'up':
            moving_up = locationBot[0] - 1
            if cell_dictionary[f'{locationBot[0] - 1}_{locationBot[1]}'][2] != 1:
                self.grid_layout.addWidget(self.bot, moving_up, locationBot[1])
            else:
                direction1 = random.choice(['left', 'right', 'down'])

        if direction1 == 'down':
            moving_down = locationBot[0] + 1
            if cell_dictionary[f'{locationBot[0] + 1}_{locationBot[1]}'][2] != 1:
                self.grid_layout.addWidget(self.bot, moving_down, locationBot[1])
            else:
                direction1 = random.choice(['left', 'right', 'up'])

    def start_coordinates(self):
        i_player = random.randrange(0, int(cells_in_col))
        if i_player == 0 or i_player == int(cells_in_col):
            j_player = random.randrange(0, int(cells_in_row))
        else:
            j_player = random.choice([0, int(cells_in_row) - 1])

        self.create_player(i_player, j_player)

    def create_player(self, i_player, j_player):
        self.player = QLabel()
        self.player.setStyleSheet(f'background-color: {color[2]}')
        self.grid_layout.addWidget(self.player, i_player, j_player)

        location_index = self.grid_layout.indexOf(self.player)
        location = self.grid_layout.getItemPosition(location_index)
        # print(f'строка и столбец при создании: {location[0]}, {location[1]}')

    def proverka(self):
        location_index = self.grid_layout.indexOf(self.player)
        location = self.grid_layout.getItemPosition(location_index)

        # закраска под игроком
        if cell_dictionary[f'{location[0]}_{location[1]}'][2] == 0:
            cell_dictionary[f'{location[0]}_{location[1]}'][2] = 5
            self.grid_layout.addWidget(self.create_cell(location[0], location[1]), location[0], location[1])
            self.create_player(location[0], location[1])

            global trajectory
            trajectory.append([location[0], location[1]])
            print(f'траектория: {trajectory}')

            print(vector)

            print(f'first_point: {trajectory[0]}')

            first_point_row = trajectory[0][0]
            first_point_col = trajectory[0][1]
            last_point_row = None
            last_point_col = None

            print(f'текущее положение: {location[0]}, {location[1]}')

            if first_point_col == 1 and vector != 'left':
                if 0 < first_point_row < 29 and vector == 'right':
                    print('куда-то движемся вправо')

            if first_point_col == 28 and vector != 'right':
                if 0 < first_point_row < 29 and vector == 'left':
                    print('куда-то движемся влево')

            if first_point_row == 1 and vector != 'down':
                if 0 < first_point_col < 29 and vector == 'up':
                    print('куда-то движемся вверх')

            if first_point_row == 28 and vector != 'up':
                if 0 < first_point_col < 29 and vector == 'down':
                    print('куда-то движемся вниз')

            if location[0] > first_point_row:
                last_point_row = location[0]
            else:
                last_point_row = trajectory[0][0]

            if location[1] > first_point_col:
                last_point_col = location[1]
            else:
                last_point_col = trajectory[0][1]

            print(f'last_point: [{last_point_row}, {last_point_col}]')

        if cell_dictionary[f'{location[0]}_{location[1]}'][2] == 1:
            print(f'{trajectory}')

    def move_player(self, direction):
        global vector
        vector = direction
        location_index = self.grid_layout.indexOf(self.player)
        location = self.grid_layout.getItemPosition(location_index)

        if direction == 'left':
            moving_left = location[1] - 1
            if moving_left >= 0:
                self.grid_layout.addWidget(self.player, location[0], moving_left)

        if direction == 'right':
            moving_right = location[1] + 1
            if moving_right < int(cells_in_row):
                self.grid_layout.addWidget(self.player, location[0], moving_right)

        if direction == 'up':
            moving_up = location[0] - 1
            if moving_up >= 0:
                self.grid_layout.addWidget(self.player, moving_up, location[1])

        if direction == 'down':
            moving_down = location[0] + 1
            if moving_down < int(cells_in_col):
                self.grid_layout.addWidget(self.player, moving_down, location[1])

        self.proverka()

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Left:
            self.move_player('left')
        if event.key() == Qt.Key_Right:
            self.move_player('right')
        if event.key() == Qt.Key_Up:
            self.move_player('up')
        if event.key() == Qt.Key_Down:
            self.move_player('down')
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Insert:
            print(cell_dictionary)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Window = Window()
    mainMenu = mainMenu()
    RulesOfNature = RulesOfNature()
    mainMenu.show()
    app.exec_()
