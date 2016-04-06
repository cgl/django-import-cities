import os

def main():
    my_text = "\n\tHello Tech Talk Participants\n"
    print(my_text)

    script_filename = "exercises/start_03.py"
    dir_name = os.path.dirname(script_filename)
    print("\tDirectory name of %s is %s\n" %(script_filename,dir_name))

if __name__=="__main__":
    main()
