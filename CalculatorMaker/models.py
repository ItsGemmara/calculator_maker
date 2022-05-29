
from django.db import models

from multiselectfield import MultiSelectField


VARIABLE_CHOICES = (('a', 'a'),
                    ('a', 'a'),
                    ('b', 'b'),
                    ('c', 'c'),
                    ('d', 'd'),
                    ('e', 'e'),
                    ('f', 'f'),
                    ('g', 'g'),
                    ('h', 'h'),
                    ('i', 'i'),
                    ('j', 'j'),
                    ('k', 'k'),
                    ('l', 'l'),
                    ('m', 'm'),
                    ('n', 'n'),
                    ('o', 'o'),
                    ('p', 'p'),
                    ('q', 'q'),
                    ('r', 'r'),
                    ('s', 's'),
                    ('t', 't'),
                    ('u', 'u'),
                    ('v', 'v'),
                    ('w', 'w'),
                    ('x', 'x'),
                    ('y', 'y'),
                    ('z', 'z'),)


class Calculator(models.Model):

    name = models.CharField(verbose_name='name', max_length=500, unique=True)
    formula = models.TextField(verbose_name='Formula', unique=True)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    variables = MultiSelectField(choices=VARIABLE_CHOICES,
                                 max_choices=20,
                                 max_length=1)

