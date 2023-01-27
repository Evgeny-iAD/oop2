from abc import ABC, abstractmethod

class Toy(ABC):
    """Абстрактный класс объекта КОТ"""
    def __init__(self):
        self.__material_t = 'material'
        self.__color_t = 'color'
        self.__name_t = 'name'

    def set_param_t(self, name,  material, color):
        self.__name_t = name
        self.__color_t = color
        self.__material_t = material

    def ret_toy(self):
        return f"название: {self.__name_t}| материал: {self.__material_t}| цвет: {self.__color_t} "


