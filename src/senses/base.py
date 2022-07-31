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