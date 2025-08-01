import random

def generate_naadan_nickname(name):
    if not name:
        return "Enter a valid name"
    suffixes = ['lu', 'ppi', 'cha', 'kunju', 'mon', 'kutty', 'etta','kanna','ku']
    return name[:3].capitalize() + random.choice(suffixes)