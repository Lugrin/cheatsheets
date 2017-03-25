# conda

```bash
conda <command> --help
conda clean --all
```


## TODO after install

### update

```bash
conda update conda
```

### channels

```bash
conda config --add channels r  # The r channel is part of the default channels, starting conda 4.3
conda config --add channels spacy
conda config --add channels auto
conda config --add channels conda-forge
conda config --add channels defaults
conda config --get channels
```

### auto-complete

For bash:

```bash
$ conda install argcomplete
```

Then add this to bash profile: `eval "$(register-python-argcomplete conda)"`

For zsh, see http://conda.pydata.org/docs/install/tab-completion.html

### default packages for all environments

create_default_packages: A list of packages that are included in every new environment by default.


## Share an environment

https://conda.io/docs/using/envs.html#share-an-environment

### Using the environment file

Cross-platform

This file handles the environment's pip packages as well as its conda packages.

```bash
source activate <env-name>
conda env export > environment.yml
#
conda env create -f environment.yml
```

### Using the spec list

These spec files are not usually cross platform.
A comment shows the platform where this spec file is known to work.

/!\ If two users have their conda channels set up differently, then
they may inadvertently create different environments from the same
spec file because conda fetches the packages from different channels.

```bash
source activate <env-name>
conda list -e > spec-file.txt
#
conda create --name <env-name> --file spec-file.txt
```

### Using urls

These explicit spec files are not usually cross platform.
A comment shows the platform where this spec file is known to work.

The file lists the universal resource locators (URLs) of the conda packages.
```bash
conda list --explicit > explicit-spec-file.txt
conda create --name <env-name> --file explicit-spec-file.txt
```

### Saved environment variables

```bash
$ cd ~/anaconda3/envs/<env-name>
$ mkdir -p ./etc/conda/activate.d
$ mkdir -p ./etc/conda/deactivate.d
$ cat > ./etc/conda/activate.d/<idio-packagename-scriptname>.sh
#!/bin/sh
export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/
$ cat > ./etc/conda/deactivate.d/<idio-packagename-scriptname>.sh
#!/bin/sh
unset MY_KEY
unset MY_FILE
```


## lasagne

*Possibly out-of-date by now. Just be careful to take the exact python version and module dependency versions as recommended.*

```bash
conda create --name lasagne_env python=3.4 scipy
conda install theano
pip install Lasagne==0.1
pip install nolearn
source activate lasagne
```


## Jupyter notebook

```bash
conda install jupyter matplotlib
```


## cleaning

```bash
conda clean
```
