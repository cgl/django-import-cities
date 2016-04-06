# django-import-cities

    python3 -m venv cities-env
    . cities-env/bin/activate #or source
    pip install -r lindysite/requirements.txt
    pip install ipython

    ./manage.py migrate
    ./manage.py makemigrations plus location
    ./manage.py migrate location
    ./manage.py migrate plus
    ./manage.py createsuperuser

export JAVA_HOME=`/usr/libexec/java_home -v '1.8*'`
export CLASSPATH="$CLASSPATH:/Users/cagil/work/django-import-cities/stanford-ner-2015-12-09"
export STANFORD_MODELS="/Users/cagil/work/django-import-cities/stanford-ner-2015-12-09/classifiers"


## References:
http://tutorial.djangogirls.org/
http://stackoverflow.com/a/15079531/1257959
http://nlp.stanford.edu/software/CRF-NER.shtml
http://stackoverflow.com/a/34364699/1257959

https://github.com/coderholic/django-cities/tree/master/cities
