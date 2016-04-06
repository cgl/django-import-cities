# downloads Stanford NER tagger
import subprocess,os

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def main():
    git("clone", "https://github.com/dat/pyner.git")
    #git("commit", "-m", "my commit message")

if __name__=="__main__":
    main()
