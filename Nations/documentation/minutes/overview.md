# Overview of project: Nations

### 11 June 2024

1. ITER 2 start,
2. Fixed nations display,
3. less throughput time now,

### 05 June 2024

Progress:
1. flow diagram,
2. uml usecase diagram,
3. made application Authenticator,
4. install djangorestframework,
5. implement Authenticator
6. Iteration 1 achieved.


```shell
python3 -m django startapp Authenticator
python3 -m pip install djangorestframework
python3 -m pip install -U Django
```

### 02 June 2024
Progress:
1. SOC (1.1) not working


### 01 June 2024
Progress:
1. Collected names dataset,
2. 'SOC(1)' done for User class,
3. 'SOC(1)' done for all apps installed
    till this,
4. AZFlag and Nations,
 

```shell
# (sequence of commands (SOC) 1 BEGIN)
python3 manage.py migrate
python3 manage.py makemigrations
# (POC 1 END)
```

```shell
# (SOC 2)
django-admin makeproject project_name
"""
run SOC(1)
"""
django-admin startapp app_name
```

## Commands:
```shell
# Before authenticator (1)
#
django-admin startapp AZNation
#
"""
#
# Run iterM1: POC1
#
"""

```


### 31 May 2024

```shell
django-admin startproject nations
cd nations
"""
# Run I1: POC1
#
#
"""
django-admin startapp authenticator
```

