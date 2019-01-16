# ASTR 302, Winter 2018, University of Washington: 
# Python for Astronomy

[Andrew Connolly](https://faculty.washington.edu/ajc26/)

Lectures 1 & 2

## Take the questionaire available [here](https://pollev.com/andrewconnolly)



## Using Github

1. Watch the introduction to git, and Github https://www.youtube.com/watch?v=2g9lsbJBPEs
  - If you don't have one, create a username on Github
 - Email me your Github username and I will add you to the team
 
2. Based on the instructions in the video fork the class repository from https://github.com/connolly/A302_2019
 - Clone the class repository to your desktop or directory

3. Based on the instructions in the video fork the class repository from https://github.com/connolly/A302_2019_Homework
 - Clone the class repository to your desktop or directory
 - Create a new folder in the directory “Students” and assign it your name
 - Create a test file within the directory called “github_test_yourname”
 - “commit” the directory to your local git repository (remember to add a comment)
 - issue a “pull request” to the class repository for me to accept the new directory and file

## How to update a fork 
Before starting a new homework it is a good idea to update your fork. There are two ways to do this
1. Issue a pull request from my repository to yours (this will bring over all of the new material into your fork)

2. If you have a fork of this repository and you want to update that fork to have it synchronized with the original repository there are two steps (this must be done at the level of the cloned repo you cant do this using the Github interface):
  - First you configure a clone of a fork so you can update to the upstream/master (you do this once per repo)
    - https://help.github.com/articles/configuring-a-remote-for-a-fork/
  - Every time you want to update to the lastest version you
    - https://help.github.com/articles/syncing-a-fork/
    
## Installing our software
1. In the directory that you cloned (“A302_2018”)
- Install Jupyter and Python on your machine
- cd to “jupyter” 
- Run the jupyter notebook by typing at the command prompt
  - jupyter notebook
  - this should either open a browser window for you or tell you how to open the browser. Click on the file Histograms.ipynb
 - Run the commands in the notebook
   - If you run into difficulties with the jupyter notebook check that you have astroml installed
     -  the astroML packages and add-ons can be installed using pip
     - [~]$ pip install astroML
    then
     - [~]$ pip install astroML_addons

