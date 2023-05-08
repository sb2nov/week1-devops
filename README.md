# Week 1 - Project 

# Goal
To Establish a Robust and Reliable Development process by settting version control using Git, implementing comprehensive Unit Tests, and setting up effective workflows to ensure that only properly tested code is merged from other branches into the Master branch.

## Requirements

<br> Link to setup Python 3.9 - https://www.python.org/downloads/ </br>
<br> Link to setup Git the first time - https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup </br>
<br> Use a Editor of your choice </br>
<br> Link to get pip3 - https://pip.pypa.io/en/stable/installation/ </br>

## Step 1 - Get the inital start code onto your system

Git clone initial code from this Github Repo - https://github.com/vj-m/week1-devops/tree/initial_starter_code
```
git clone git@github.com:vj-m/week1-devops.git
```
## Step 2 - Add Unit Tests

```
def test_add():
    assert add(1,1) == 2

def test_sub():
    assert sub(1,1) == 0

def test_mul():
    assert mul(1,1) == 1

def test_div():
    assert div(2,1) == 2
```

## Step 3 - Create a workflow

1.) Create a directory called .github/workflows within the directory containing .git
2.) And create a workflow ‘YAML’ file, let's call it ci_cd_wf.yml
3.) Git add and push changes (This automatically invokes the Git actions and sets up the CI/CD Pipeline which on push to the master branch)

```
name : test

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on : ubuntu-latest

    steps:
      - name: Check out repo code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: "3.x"

      - name: Install Dependencies
        run: |
          python -m pip install -r requirements.txt
      - name: Run tests
        run: |
          python -m pytest calculator.py
```

## Step 4 - Check our Gitflow with a new branch
<br> 1.)  Create a new feature branch to check a case where the push to master or PR fails by making a purposeful mistake in the code to fail a test </br>
<br> 2.)  Create a new feature branch called test </br>

```
def test_add():
    assert add(1,1) == 0
```
<br> We have changed the test_add method to assert a False </br>
<br> 3.) Git add, push and commit </br>

## Step 5 - Fix all the errors to make a successful build
<br> 1.) Change back the test_add function </br>
<br> 2.) Add, commit, and push the new changes to the master branch again </br>

### As the first week of the project comes to a close, it's important to reflect on the progress made so far.

## Future Scope Recommendations - 
<br> Now that the initial code is in place, it's time to focus on improving its quality. One way to do this is to add more checks such as linters, code coverage, and code quality checks. </br>
<br> Another recommended step is to add 'runs on' actions like a pull request. This allows for a more streamlined workflow and can help ensure that the code changes are thoroughly tested before being merged into the main branch. </br>

### As you move forward into Week 2 of the project, keep these next steps in mind. By continually improving the quality of your code, you'll be setting yourself up for success in the long run. 

## Appendix
<br> This repository has three branches -
### 'main' branch contains the file code for the project
### 'initial_starter_code' contains the inital code to start with
### 'test' - The state of the project with a wrong test added for reference - this is supposed to fail the merge to master process in our workflow
</br>
