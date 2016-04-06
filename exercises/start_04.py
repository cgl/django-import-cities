import os

def main():
    my_text = "\n\tHello Tech Talk Participants\n"
    print(my_text)

def print_filedir():
    dir_name = os.path.dirname(__file__)
    print("\tDirectory name of the current script is '%s'\n" % dir_name)

def print_filedir_abs():
    path = os.path.abspath(__file__)
    print("\tAbs path of the current script is '%s'\n" % path)


if __name__=="__main__":
    main()
    print_filedir()
    print_filedir_abs()
