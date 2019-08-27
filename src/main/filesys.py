from file import File

def write(file_name, message, overwrite=False):
    mode = 'w' if overwrite else 'a'
    file = File(file_name, mode)
    file.write(message)

def read(file_name, overwrite=False, splitlines=False):
    file = File(file_name)
    text = file.read(overwrite)
    return text.split('\n')