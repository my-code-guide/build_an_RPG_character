
full_dot = '●'
empty_dot = '○'

def validate_name(name):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'


def validate_stats(strength, ntelligence, charisma):
    for stat in (strength, ntelligence, charisma):
        if not isinstance(stat, int):
            return 'All stats should be integers'

    for stat in (strength, ntelligence, charisma):
        if stat < 1:
            return 'All stats should be no less than 1'

    for stat in ( strength, ntelligence, charisma):
        if stat > 4:
            return 'All stats should be no more than 4'
    
    if strength + ntelligence + charisma != 7:
        return 'The character should start with 7 points'

def create_dots(stat):
    return stat * full_dot + empty_dot * (10 - stat)


def create_character(name, strength, ntelligence, charisma):
    name_error = validate_name(name)
    if name_error:
        return name_error

    stats_error = validate_stats(strength, ntelligence, charisma)
    if stats_error:
        return stats_error

    return (
        f'{name}\n'
        f'STR {create_dots(strength)}\n'
        f'INT {create_dots(ntelligence)}\n'
        f'CHA {create_dots(charisma)}'
    )
    