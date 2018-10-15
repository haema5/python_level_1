from os import mkdir, rmdir
from os.path import abspath


def make_dir(dir_name):
    mkdir(abspath(dir_name))


def del_dir(dir_name):
    rmdir(abspath(dir_name))


def main():
    print('Hello world!')


if __name__ == "__main__":
    main()
