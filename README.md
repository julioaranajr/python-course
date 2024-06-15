# How to collaborate on this project: 

- [ ] Repository Fork
- [ ] Clone the repository
- [ ] Update the master branch
- [ ] Create a branch
- [ ] Make changes
- [ ] Make a Pull Request

## 1.-Repository Fork

**IMPORTAN:** The first step is to "Fork" the repository.

A fork is a copy of a repository that you manage. Forks let you make changes to a 
project without affecting the original repository. You can fetch updates from or 
submit changes to the original repository with pull requests.

Forking a repository is similar to copying a repository, with two major differences:

* You can use a pull request to suggest changes from your user-owned fork to the original repository in its GitHub instance, also known as the upstream repository.
* You can bring changes from the upstream repository to your local fork by synchronizing your fork with the upstream repository.



## 2.- Clone the repository

After having the repository in our account, select the repository address "SSH or HTTP" and clone:

```sh
$ https://github.com/julioaranajr/aws_services_db.git
```

Inside the folder it generates, check the repository URL:

```sh
$ git remote -v
```

### Before making modifications add the URL of the original repository of the project:

```sh
$ git remote add upstream https://github.com/julioaranajr/aws_services_db.git(Forked)
```

### Check

```sh
$ git remote -v
```


## 3.- Update the Master branch
Before starting work, get the latest changes from the Original Repo:

```sh
$ git pull -r upstream master
```

### Create a Branch
To create a branch use the git "checkout" option:

```sh
$ git checkout -b feature-branch-name
```


## 4.- Make changes

### Make all the changes you want to make to the project.

### Add the files and commit

After committing, push to our repository indicating the branch we have created.

```sh
$ git push origin feature-branch-name
```

### Make a Pull Request

Click on "Compare & Pull Request"


* Write Pull Request changes.

If everything is ok, send with the "Send Pull Request" button. Wait for the repository duel to review it, accept it, and merge it into the appropriate branch.
