# coding-competition-toolbox

# Google Hashcode

Compute the solutions: `python -m hashcode.main compute-solutions` <br>
Run genetic algorithm: `python -m hashcode.main genetic-algorithm` <br>


build docker: `docker build . -t hash`
run container: `docker run --user $(id -u):$(id -g) -v $PWD:/project/ -it hash /bin/bash` <br>
set venv: `source /virtualenv/env/bin/activate`
