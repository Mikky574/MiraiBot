from abc import abstractmethod

from PIL import Image
from chinese_chess.enum import Team
from chinese_chess.component import Transform


class Chess:

    def __init__(self, team: str, img: Image, x: int, y: int, name: str = ''):
        self.image = img  # 棋子的图片,子类传过来~
        self.name: str = name  # 棋子名字，子类传过来~
        self.team: str = team  # 阵营，子类传过来~
        self.transform: Transform = Transform(self, x, y)  # 变换组件,初始坐标进行设置
        self.one_hot = ''  # 为后续人机对战，需要将棋子进行one-hot编码挖坑

    @abstractmethod
    def move(self, command: str, mp):  # 移动棋子，子类实现~（子类先判断移动是否合法，再调用自身的self.transform.move()进行移动）
        pass

    @abstractmethod
    def is_legal(self, command: str, mp):  # 判断移动是否合法~
        pass

    def on_destroy(self):  # 被吃时调用，挖坑~
        pass

    def update_position(self, new_x: int, new_y: int):  # 每次移动后要记得更新棋子位置
        pos = self.transform.position
        pos.x = new_x
        pos.y = new_y

    def __repr__(self):  # 方便print
        return self.team + self.name

    def __str__(self):  # str()时调用
        return self.team + self.name

    def get_cow_by_num(self, num):
        if num == '1' or num == '一':
            if self.team == Team.Red:
                return 8
            else:
                return 0
        elif num == '2' or num == '二':
            if self.team == Team.Red:
                return 7
            else:
                return 1
        elif num == '3' or num == '三':
            if self.team == Team.Red:
                return 6
            else:
                return 2
        elif num == '4' or num == '四':
            if self.team == Team.Red:
                return 5
            else:
                return 3
        elif num == '5' or num == '五':
            if self.team == Team.Red:
                return 4
            else:
                return 4
        elif num == '6' or num == '六':
            if self.team == Team.Red:
                return 3
            else:
                return 5
        elif num == '7' or num == '七':
            if self.team == Team.Red:
                return 2
            else:
                return 6
        elif num == '8' or num == '八':
            if self.team == Team.Red:
                return 1
            else:
                return 7
        elif num == '9' or num == '九':
            if self.team == Team.Red:
                return 0
            else:
                return 8

    def get_dis_by_num(self, num):
        if num == '1' or num == '一':
            return 1
        elif num == '2' or num == '二':
            return 2
        elif num == '3' or num == '三':
            return 3
        elif num == '4' or num == '四':
            return 4
        elif num == '5' or num == '五':
            return 5
        elif num == '6' or num == '六':
            return 6
        elif num == '7' or num == '七':
            return 7
        elif num == '8' or num == '八':
            return 8
        elif num == '9' or num == '九':
            return 9
