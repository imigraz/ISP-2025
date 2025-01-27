# ISP-2025

Materials for 'Introduction to scientific programing – Linux, python and R' (LV 0940.197), WS 2024/25, offered at the Medical University of Graz (https://www.medunigraz.at).

Dear participant,

welcome to the course of Introduction to Scientific Programming within the PhD School MolMed. In this course, we will get the basics in two of the main languages used in Science: Python and R. We will also introduce how to work under Linux environment, the use of some command in the terminal (bash) as well as how to submit jobs to a scientific cluster using the job manager SLURM.

The course will take place the week Jan. 27-31 2025 at the Med Campus in the room **SR53 (MC2.N.01.017)**.

# 1. COURSE PREPARATION
We recommend that you bring your own laptop for the course, i.e., please prepare in advance as instructed below.

## 1.1 Python
Please install anaconda (v 3) on your laptop. You find the appropriate version for your OS following the link:  https://docs.anaconda.com/anaconda/install/

## 1.2 R
Please install R and RStudio on your laptop. You find the instructions and links in the document *Introduction course_Installation_R_RStudio_Rpackages.pdf*.


# 2. CONTENT

## 2.3 Linux environment, bash and High performance computing (HPC)

### 2.3.1 Installation and previous requirements
We have prepared a virtual machine with Debian for the course to be used on the laptops of the Pc Pool. We will cover the following topics:

### 2.3.2 Content

- Introduction to Linux environment, distributions, permissions
- Command-line basics
- Vi editor
- Environment variables, .bashrc file
- Scripts and running scientific jobs
- Visualization of data with gnuplot
- SLURM
- Introduction to HPC MedBioNode

### 2.3.3 Some useful links
Slides: 

VSC Tranining course: https://vsc.ac.at/training/2022/VSC-Linux-Oct/

Spectrum data: https://medunigraz-my.sharepoint.com/:u:/g/personal/pedro_murcia_medunigraz_at/EXy8HwgP7-FKgOI7u6GoNkUBD4uf2oHq4rhlXFDraEFg_w?e=ZFQfjf

Linux cheat sheet: https://cheatography.com/davechild/cheat-sheets/linux-command-line/ 

vi cheat sheet: https://www2.seas.gwu.edu/~mems/ece215/reference/vi-cheatsheet.pdf 

#### Some examples of bash scripts:

+ script.sh <br>
#!/bin/bash <br>
echo "foo bar" <br>
mkdir myfolder <br>

+ loop.sh (using a numeric sequence) <br>
#!/bin/bash <br>
for i in {1..5} <br>
do <br>
echo $i <br>
done <br>

+ loop2.sh (using a list of elements in test.dat) <br>
#!/bin/bash <br> 
for i in $(cat test.dat) <br>
do <br>
echo $i <br>
do <br>

# License


[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

This work is licensed under the terms of the Attribution-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. See <https://creativecommons.org/licenses/by-sa/4.0/>

You are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material 
- The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- Attribution — You must give appropriate credit , provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- NonCommercial — You may not use the material for commercial purposes . 
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
- No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.
