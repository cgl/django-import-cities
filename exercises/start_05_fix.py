# downloads Stanford NER tagger
import subprocess,os

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def main():
    if os.path.exists("pyner"):
        exit("\n\t Repo exists \n")
    git("clone", "https://github.com/erickpeirson/pyner.git")
    #git("clone","https://github.com/dat/stanford-ner.git")

if __name__=="__main__":
    main()
