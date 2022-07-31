from abc import ABC, abstractmethod
import numpy as np


class Sense(ABC):
    def __init__(self):
        pass

    def sense_environment(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError
