import os
import spotify

def init_filesys():
    home = os.environ['HOME']
    spools_home_path = '{HOME}/.spools'.format(HOME=home)
    if not os.path.exists(spools_home_path):
        os.mkdir(spools_home_path)
    profile_home_path = '{}/test'.format(spools_home_path)
    if not os.path.exists(profile_home_path):
        os.mkdir(profile_home_path)
    music_home_path = '{}/music'.format(profile_home_path)
    if os.path.exists(music_home_path):
        os.system('rm -rf {}'.format(music_home_path))
    if not os.path.exists(music_home_path):
        os.mkdir(music_home_path)

def init():
    init_filesys()