
import re


abbrevations = {
    'E:': 'Englisch',
    'M:': 'Mathe',
    'D:': 'Deutsch',
    'PL:': 'Philo',
    'SW:': 'SoWi',
    'BI:': 'Bio',
    'EK:': 'Erdkunde',
    'GE:': 'Geschichte',
    'SP:': 'Sport',
    'IF:': 'Info',
    'S1:': 'Spanisch',
    'PA:': 'Päda',
    }


def remove_abb(input): 
    input = re.sub(r'\s\w+\d?: bei', ': bei', input)
    for key in abbrevations:
        input = input.replace(key,abbrevations[key])
    return input


