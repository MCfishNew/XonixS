import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QSlider, QPushButton

width = 900
height = 600
cell_size = 15
player_hp = ['3']
score = 1200
cells_in_row = width / cell_size
cells_in_col = height / cell_size
color = {0: 'lightblue', 1: 'khaki', 2: 'green', 3: 'red', 5: 'plum'}
countBot = 1
volume = 15
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


class RedSettings(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")
        self.setStyleSheet('background: khaki;')
        self.move(500, 150)
        self.setFixedSize(900, 600)
        self.player = QMediaPlayer()
        buttonRule_Menu = QtWidgets.QPushButton("", self)
        buttonRule_Menu.setGeometry(20, 20, 70, 60)
        buttonRule_Menu.setIcon(QIcon('arrow.png'))
        buttonRule_Menu.setStyleSheet('solid black; font-size: 25px; color: white;')
        buttonRule_Menu.clicked.connect(self.switch_set_menu)

    def media(self):
        media_content = QMediaContent(QUrl.fromLocalFile("menu.wav"))

        self.player.setMedia(media_content)

        self.volume_slider = QSlider()
        self.volume_slider.setOrientation(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setStyleSheet("QSlider::handle { width: 40px; }")
        self.player.setVolume(volume)
        self.volume_slider.setValue(volume)
        self.volume_slider.setFixedWidth(900)
        self.volume_slider.setFixedHeight(20)
        self.volume_slider.valueChanged.connect(self.change_volume)

        self.play_button = QPushButton("Воспроизвести")
        self.play_button.clicked.connect(self.play_music)

    def switch_set_menu(self):
        RedSettings.hide()
        mainMenu.show()

    def play_music(self):
        self.player.play()

    def change_volume(self, volume):
        self.player.setVolume(volume)


class RulesOfNature(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.setStyleSheet('background: khaki;')
        self.move(500, 150)
        self.setFixedSize(900, 600)
        self.setupUi()

    def switch_rule_menu(self):
        RulesOfNature.hide()
        mainMenu.show()

    def setupUi(self):
        text_label = QLabel(self)
        text_label.move(50, 60)
        text_label.resize(780, 650)

        text_label.setWordWrap(True)
        text_label.setText("В игре есть два типа поля: “Суша” и “Море”. "
                           "\nИгрок управляет персонажем, который находится на территории суши. "
                           "\nИгрок управляет движением объекта на игровом поле. "
                           "Он должен нарисовать линию, начиная от края поля, и продолжать движение по полю противника,"
                           "\nпока он не вернется на любое место своего поля,чтобы закрыть область."
                           "\nПосле этого область противника становится областью игрока. "
                           "Во время захвата территории игроку будут мешать хаотично двигающиеся объекты,"
                           " которые будут перемещаться по своему полю “Море”,"
                           " если игрок коснется противника или его линия пересечется с ним, игрок проиграет."
                           " Чем больше территории игрок захватит, тем больше очков он заработает."
                           " Если игрок разделит игровое поле на несколько частей, то каждый сектор станет игровой "
                           "территорией игрока,"
                           " если там не находится противник."
                           "\nЦель игры - захватить как можно больше территории на игровом поле за определенное время"
                           " и набрать как можно больше очков. "
                           "Игра заканчивается после захвата определённого количества территории или при потере всех "
                           "жизней."

                           )
        text_label.setStyleSheet('font-size: 20px; color: black;')

        rules = QLabel(self)
        rules.move(10, 100)
        rules.resize(780, 30)

        rules.setWordWrap(True)
        rules.setText("Правила игры Xonix")
        rules.setFont(QFont('Segoe UI Semibold'))
        rules.setStyleSheet('font-size: 30px; color: black;')

        buttonRule_Menu = QtWidgets.QPushButton("", self)
        buttonRule_Menu.setGeometry(20, 20, 70, 60)
        buttonRule_Menu.setIcon(QIcon('arrow.png'))
        buttonRule_Menu.setStyleSheet('solid black; font-size: 25px; color: white;')
        buttonRule_Menu.clicked.connect(self.switch_rule_menu)


class mainMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Xonix")
        self.setStyleSheet('background: khaki;')
        self.move(500, 150)
        self.setFixedSize(900, 600)

        game_name = QLabel(self)
        game_name.resize(700, 70)
        game_name.setStyleSheet('font-size: 50px; color: cian; background: khaki;')
        game_name.setAlignment(Qt.AlignCenter)
        game_name.setFont(QFont('Segoe UI Semibold'))
        game_name.setText("XONIX")
        game_name.move(100, 85)

        buttonPlay = QtWidgets.QPushButton("Играть", self)
        buttonPlay.setGeometry(150, 180, 600, 80)
        buttonPlay.setStyleSheet('solid white; color: white; background: black;')
        buttonPlay.setStyleSheet("QPushButton::hover"
                                 "{"
                                 "background-color : rgb(133, 245, 88);"
                                 "}")
        buttonPlay.setFont(QFont('Comic Sans MS', 14))
        buttonPlay.clicked.connect(self.switch_play)

        buttonRule = QtWidgets.QPushButton("Правила", self)
        buttonRule.setGeometry(150, 280, 600, 80)
        buttonRule.setStyleSheet('solid white; color: white; background: black;')
        buttonRule.setStyleSheet("QPushButton::hover"
                                 "{"
                                 "background-color : rgb(99, 171, 247);"
                                 "}")
        buttonRule.setFont(QFont('Comic Sans MS', 14))
        buttonRule.clicked.connect(self.switch_rule)


        buttonExit = QtWidgets.QPushButton("Выйти", self)
        buttonExit.setGeometry(150, 380, 600, 80)
        buttonExit.setStyleSheet('solid white; color: white; background: black;')
        buttonExit.setStyleSheet("QPushButton::hover"
                                 "{"
                                 "background-color : rgb(245, 88, 88);"
                                 "}")
        buttonExit.setFont(QFont('Comic Sans MS', 14))
        buttonExit.clicked.connect(self.switch_exit)

    def switch_play(self):
        Window.move(mainMenu.x(), mainMenu.y())
        RulesOfNature.move(mainMenu.x(), mainMenu.y())

        Window.show()
        self.hide()

    def switch_rule(self):
        Window.move(mainMenu.x(), mainMenu.y())
        RulesOfNature.move(mainMenu.x(), mainMenu.y())

        RulesOfNature.show()
        self.hide()

    def switch_settings(self):
        Window.move(mainMenu.x(), mainMenu.y())
        RedSettings.move(mainMenu.x(), mainMenu.y())

        RedSettings.show()
        self.hide()

    def switch_exit(self):
        sys.exit(app.exec_())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.switch_exit()


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
        self.setFixedSize(900, 660)
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
        bar.resize(877, 600)
        bar.setStyleSheet('font-size: 30px; color: white; background: rgb(99, 171, 247); border: 2px solid #000000')
        bar.move(13, 600)
        sidebar.append(bar)

        heart = QLabel(self)
        heart.resize(50, 50)
        heart.setStyleSheet('font-size: 30px; color: white; background-image: url("icons8-pixel-heart-48.png")')
        heart.setAlignment(Qt.AlignJustify)
        heart.setText(player_hp[0])
        heart.move(830, 610)
        sidebar.append(heart)

        scoreL = QLabel(self)
        scoreL.resize(200, 100)
        scoreL.setStyleSheet('font-size: 35px; color: white;')
        scoreL.setAlignment(Qt.AlignCenter)
        scoreL.setText(f'Счёт: {score}')
        scoreL.move(30, 585)
        sidebar.append(scoreL)
        return sidebar

    def create_cell(self, x, y):
        cell_color = cell_dictionary[f'{x}_{y}'][2]
        self.cell = QLabel()
        self.cell.resize(cell_size, cell_size)
        self.cell.setFixedSize(cell_size,cell_size)
        # self.cell.setText(str(cell_dictionary[f'{x}_{y}']))
        self.cell.setStyleSheet(f'background-color: {color[cell_color]};'
                                'border: 0px solid #EEE;'
                                'padding: 0; margin: 0; ')
        return self.cell

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

    def proverka(self):
        location_index = self.grid_layout.indexOf(self.player)
        location = self.grid_layout.getItemPosition(location_index)

        if cell_dictionary[f'{location[0]}_{location[1]}'][2] == 0:
            cell_dictionary[f'{location[0]}_{location[1]}'][2] = 5
            self.grid_layout.addWidget(self.create_cell(location[0], location[1]), location[0], location[1])
            self.create_player(location[0], location[1])
        if cell_dictionary[f'{location[0]}_{location[1]}'][2] == 0:
            self.create_player(location[0], location[1])
    def Picovalka(self):
        location_index = self.grid_layout.indexOf(self.player)
        location = self.grid_layout.getItemPosition(location_index)

        global trajectory
        trajectory.append([location[0], location[1]])
        print(f'траектория: {trajectory}')

        print(vector)

        print(f'first_point: {trajectory[0]}')

        print(f'текущее положение: {location[0]}, {location[1]}')

        if trajectory != []:
            if cell_dictionary[f'{location[0]}_{location[1]}'][2] == 1:
                first_point_row = trajectory[0][0]
                first_point_col = trajectory[0][1]
                last_point_col = trajectory[-1][1]
                last_point_row = trajectory[-1][0]
                for row in range(first_point_row, last_point_row + 1):
                    for col in range(first_point_col, last_point_col + 1):
                        if cell_dictionary[f'{row}_{col}'][2] == 0 or cell_dictionary[f'{row}_{col}'][2] == 5:
                            cell_dictionary[f'{row}_{col}'][2] = 1
                            self.grid_layout.addWidget(self.create_cell(row, col), row, col)
                trajectory = []
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
        self.Picovalka()

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
        if event.key() == Qt.Key_Escape:
            Window.close()
            mainMenu.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Window = Window()
    mainMenu = mainMenu()
    RulesOfNature = RulesOfNature()
    RedSettings = RedSettings()
    mainMenu.show()
    app.exec_()
