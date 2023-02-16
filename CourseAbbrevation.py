
import re


abbrevations = {
    'PL:': 'Philo',
    'SW:': 'SoWi',
    'BI:': 'Bio',
    'EK:': 'Erdkunde',
    'GE:': 'Geschichte',
    'SP:': 'Sport',
    'IF:': 'Info',
    'S1:': 'Spanisch',
    'PA:': 'Päda',
    'E:': 'Englisch',
    'M:': 'Mathe',
    'D:': 'Deutsch',
    }


def remove_abb(input): 
    input = re.sub(r'\s\w+\d?: bei', ': bei', input)
    for key in abbrevations:
        input = input.replace(key,abbrevations[key])
    return input


