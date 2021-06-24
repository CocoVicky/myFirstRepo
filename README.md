# Basic flask app

This repository contains a Flask python application used as part of a practical work of the [Gitlab-CI basics](https://trainings.pages.gitlab.tech.orange/gitlab-ci/basics.htm) training.

The main program is located in the `app.py` file, it is a website that returns the first ten numbers of the fibonacci sequence.

The directory also contains a test file, which is executed using pytest, which must therefore be installed if you want to test the program locally

## Install required dependencies

In order to start the Flask server it is necessary to install the required dependencies. To do this, you must execute the following command:

```console
$ pip install -r requirements.txt
...
```

## Execute unit tests locally

```console
$ pip install pytest
...
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
rootdir: /builds/ckrv5190/test-docker
collected 1 item
test_fibonacci.py .                                                      [100%]
============================== 1 passed in 0.52s ===============================
```

> The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
see [https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/) for more information

## Start the server

Start the server with the following command :

```console
$ python app.py
 * Serving Flask app "app.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

Then you can test it using `curl` in another console :

```console
$ curl -s http://127.0.0.1:8080/
Fibonacci suite: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

# What you have to do

Well, now, we have to build from scratch a pipeline to automatize the testing of this application, and the creation of a Docker image embedding it.

## STEP 1 : Unit testing

Let's start with the unit tests with **python 3.8** ... 

Complete the following `.gitlab-ci.yml` skeleton in order to test the app.py application:

  ```yaml
  stages:
    - test

  unit-tests:
    stage: 
    image: 
    script: 
  ```
>concepts : "stage", "image", "script"

## STEP 2 : Building an image

After testing the application, now we want to:
- build a Docker image containing the application
- publish it in the GitLab registry of our project

A `Dockerfile` is provided to build the image.

Update your `.gitlab-ci.yml` pipeline in order to integrate a new build stage:

  ```yaml
  build-image:
    stage: build
    image: ...

  ```
>concepts : "kaniko", "Dockerfile", "variables $CI_*", "container registry"

Verify that your image is now present in the **Packages & Registries / Container Registry** section of your GitLab project.

## STEP 3 : Testing an image built

And if we have to check the result of this web application with curl command ...

Update your `.gitlab-ci.yml` pipeline in order to integrate a new test stage for the image which was previously built and published.

We rely on the [`services:`](https://docs.gitlab.com/ce/ci/yaml/#services) parameter which allows us to execute a Docker container in background while the GitLab job is running:

  ```yaml
  test-image:
    stage: package-test
    services:
      - name: ...
        alias: fibonacci  # services hostname 
    image: alpine
    before_script:
      - apk add curl  # curl is not part of alpine image: we need to install it before running the script
    script: 
      - curl ...

  ```

>concepts : "before_script", "services", "container registry", "artifact"

# Using GitLab CI templates

Another way to build a pipeline is to use GitLab CI templates based on [To Be Contenuous](https://orange-opensource.pages.gitlab.tech.orange/tbc/doc/intro/).

Use the [kicker](https://orange-opensource.pages.gitlab.tech.orange/tbc/kicker/) to generate your pipeline based on the GitLab templates which meet your needs.
