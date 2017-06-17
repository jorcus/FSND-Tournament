#Swiss Tournament Generator

This application was created as my submission for Project 2 of Udacity's Full Stack NanoDegree program.  The objective was to create an application using Python and PSQL that could effectively conduct a Swiss Style Tournament and that would pass all of the checks within the *tournament_test.py* file.


## Installation
####Prerequisites:
| Prerequisite | Documentation | Download |
|---------------|---------------|----------|
| **Git** | [docs](https://git-scm.com/doc) | [download](http://git-scm.com/downloads) |
| **Virtual Box** | [docs](https://www.virtualbox.org/wiki/Documentation) | [download](https://www.virtualbox.org/wiki/Downloads)|
| **Vagrant** | [docs](https://docs.vagrantup.com/v2/) | [download](https://www.vagrantup.com/downloads)       |

## How to Run
Once the installation steps are complete, you are ready to connect to the
Vagrant box.  To connect:

1. Log into Vagrant VM 'vagrant u[' by entering: `vagrant ssh`
2. Move to *tournament* directory by entering: `cd /tournament`
3. Create the *tournament* database by entering: `psql -f tournament.sql`
4. To test the database enter: `python tournament_test.py`
5. Launch Python command line by entering `python`
6. Import tournament by entering: `import tournament`
7. Execute a desired function.

