from abc import ABC, abstractmethod
import numpy as np


class Environment(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add(self):
        raise NotImplementedError

    @abstractmethod
    def plot(self):
        raise NotImplementedError
