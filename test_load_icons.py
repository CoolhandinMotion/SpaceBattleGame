import pygame
from pathlib import Path
from collections import namedtuple


Student = namedtuple('Student',('name','address'))

me = Student("Nader","Besat st")


def send_student():
    return me
