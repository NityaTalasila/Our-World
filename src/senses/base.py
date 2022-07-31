from abc import ABC, abstractmethod
import numpy as np


class Sense(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def sense(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError


class Smell(Sense):
    def __init__(self):
        super().__init__()
        self.intensity = 0

    def sense(self):
        return None

    def update(self):
        self.intensity += 1