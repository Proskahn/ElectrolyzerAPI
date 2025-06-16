import json
import casadi
from .constants import LR_PRICE_in_EURO_PER_MINIGRAM


class Catalyst:
    def __init__(self, component: dict):
        self.lr = component.lr

    def compute_price(self) -> casadi.MX:
        return self.lr * LR_PRICE_in_EURO_PER_MINIGRAM
