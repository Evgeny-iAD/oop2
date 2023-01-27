from abc import ABC, abstractmethod

class Cat(ABC):
    """Абстрактный класс объекта КОТ"""
    def __init__(self):
        self.__sex = 'sex'
        self.__color = 'color'
        self.__breed = 'breed'

    def param(self):
        return f"пол: {self.__sex}| цвет: {self.__color}| порода: {self.__breed}"

    def set_sex(self, sex):
        self.__sex = sex

    def set_color(self, color):
        self.__color = color

    def set_breed(self, breed):
        self.__breed = breed

    @abstractmethod
    def voice(self):
        pass
