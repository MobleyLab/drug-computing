# Syllabus for PharmSci 175/275: Drug Discovery Computing Techniques

## Course Information

### Course days, times, meeting location and office hours

See course website on Canvas for full details.
The instructor is David L. Mobley, and his office is 3134B Natural Sciences 1.

## Text

**No textbook is currently required**; however, we *strongly recommend* Leach's Molecular Modelling book, which all of you should have on hand or have access to (such as in the library):
    Molecular Modelling: Principles and Applications, 2nd Edition
    Andrew R. Leach, Prentice Hall, London, 2001
    ISBN: 0-582-38210-6

Allen & Tildesley's Computer Simulations of Liquids and Frenkel and Smit's Understanding Molecular Simulation are also both standard and valuable reference texts.

## Other requirements

A laptop computer running a recent version of OS X, Linux, or Windows (with the first two being preferable) on which you can install Anaconda's [Python distribution](https://www.anaconda.com/download) as well as other software tools, and get Jupyter notebooks working with the OpenEye toolkits.
Basically, you should be able to successfully follow the instructions in [`getting-started.md`](getting_started.md) or you will have problems.
If you have concerns, see me early to find out whether your laptop will suffice.
**Do not wait until you are attempting to work on the first assignment.**

## Prerequisites

### Undergraduate level (175) prerequisites
- Two quarters of Calculus
- At least one quarter of programming experience (CSE 41 or I&C SCI 31 or equivalent) required; a second quarter is recommended (CSE 42 or I&C SCI 32 or equivalent)
- Some familiarity with Linux
- Some experience with Python programming

### Graduate level (275) prerequisites

There are no formal prerequisites for the course, and in principle, a motivated student with no advanced Calculus training and no background in simulations, programming, or scientific computing could do well. However, the time required to do well will be much higher the less background you have in these areas. The most substantial issue is programming experience. While the course does include a recap of Python, it is not a formal course in Python. Someone with any significant prior programming experience in any language ought to pick up enough Python quickly, but if you have no prior programming experience at all, and you're not prepared to devote a lot of time to learning Python very quickly, you will likely struggle in the class. Some knowledge of multivariable Calculus, and some familiarity with Linux would also be a plus – but again, these are not essential.

## Topics covered

- Linux, Python, Python numerics intro/recap
- Classical semi-empirical force fields, practical aspects of simulations, energy minimization
- Visualization and movie-making – PyMol, VMD
- Working with molecules in Python; 3D structure generation; shape overlays
- Quantum mechanical background/method survey/applications to solvation
- Molecular dynamics and Monte Carlo; MD refinements
- Implicit solvation, hybrid solvent models, going beyond surface area
- Docking and scoring, library searches for drug discovery; pose prediction
- Ligand-based design, Lingo searches, other library searches
- Fluctuations, correlations, and error analysis; some essential statistical ideas
- Estimating and computing physical properties; informatics-based methods (the good, the bad, and the ugly)
- Working with proteins, homology modeling, the PDB
- A bit on scientific computing practicalities and outlook

A detailed schedule (by date) will be posted on the course website on Canvas, and [assigned materials](assigned_materials.md) (by lecture number) are available in [`assigned_materials.md`](assigned_materials.md).
Exact due dates for assigned materials, and the schedule of lectures, will be posted on Canvas.

## Class structure

You should bring a laptop computer to class to allow for hands-on work and troubleshooting relating to the content being covered, unless you plan on using one of the computers in the classroom (in which case you should make prior arrangements with your instructor to ensure you have all the required software available).
We will be using numerous Jupyter notebooks in class to allow you to try things out, including working on "sandboxes" and examples in class, so it is important you have a computer with you in class.
Normally a tablet will NOT suffice.


## Homework

Students choose assignments from a menu appropriate for their level, with undergraduate students choosing **three** assignments and graduate students choosing **five** assignments.
The vast majority of your course grade is based on your performance on these assignments.

Homework assignments can be discussed with other students, but you each must submit your own independent work (and for assignments involving coding, you must each write your own unique code, which should be submitted with your assignments).
If you utilize code obtained elsewhere (such as online) you must explicitly credit the source in your submissions, and this should not constitute the majority of your submission.
Submitting the work of others, copying code from others, or reusing code from elsewhere without attribution constitutes [academic dishonesty](#academic-integrity-and-academic-dishonesty) and will result in a failing grade.

Exact due dates for homework are posted on Canvas.

### Homework at the undergraduate (175) level: Three of the following
1.  **(required)** Energy minimization – simple energy minimization in Python on Lennard-Jones clusters. Not directly relevant to drug discovery – but provides a foundation for understanding many of the other techniques we talk about.
2.  Implementing basic molecular dynamics simulations in Python on a simple model of a polymer. Helpful if you plan on using molecular dynamics simulations for your research – you’ll have a much better idea how they work.
3.  Basic Monte Carlo in Python on the same system as #2.
4.  3D structure generation and shape-overlays (ligand-based design)
5.  Docking and scoring and library searching (best completed with #4 also)
6.  Making and testing an empirical model for physical property (solubility) prediction



### Homework at the graduate (275) level: Five of the following
1.  **(required)** Energy minimization – simple energy minimization in Python on Lennard-Jones clusters. Not directly relevant to drug discovery – but provides a foundation for understanding many of the other techniques we talk about.
2.  Implementing basic molecular dynamics simulations in Python on a simple model of a polymer. Helpful if you plan on using molecular dynamics simulations for your research – you’ll have a much better idea how they work.
3.  Basic Monte Carlo in Python on the same system as #2.
4.  3D structure generation and shape-overlays (ligand-based design)
5.  Docking and scoring and library searching (best completed with #4 also)
6.  Advanced visualization – movie-making in PyMol
7.  Making and testing an empirical model for physical property (solubility) prediction

Really, these should typically be completed in consecutive order, though skips are allowed.
At the very least, you do not want to jump to the docking/scoring assignment or the physical property assignment without having done 3D structure generation and shape overlays, nor do you want to do the Monte Carlo assignment without having done the molecular dynamics assignment.


## Final

The final exam is a written report analyzing a paper you select from the literature in view of what you have learned from the course. This should include a summary of the paper, strengths and weaknesses, and ideas for future work based on this paper and other work in the area you are aware of in the literature. Submit a brief summary of your choice of paper and why you chose it for approval by the date posted on the course website. Your final report will be due at the scheduled time for the final, and must be submitted via the Canvas Assignment.

## Grading

Grading will be based on your homework assignments (75%), final report (15%) and participation (10%).
In the undergraduate version of this course the grading scheme will be roughly as follows:
- 90% and up: A
- 80% to 90%: B
- 70% to 80%: C
- 60% to 70%: D
- 60% and below: F
Note that because the number of assignments vary between the undergraduate and graduate version, each assignment is worth a different percentage in the two cases.

## Academic Integrity and Academic Dishonesty


### Official UCI policy
Academic honesty is a requirement for passing this class.
Any student who compromises the academic integrity of this course is subject to a failing grade.
The work you submit must be your own.
Academic dishonesty includes, but is not limited to copying answers from another student, allowing another student to copy your answers, communicating exam answers to other students during an exam, attempting to use notes or other aids during an exam, or tampering with an exam after it has been corrected and then returning it for more credit.
If you do so, you will be in violation of the UCI Policies on Academic Honesty (see [https://aisc.uci.edu/](https://aisc.uci.edu/)).
It is your responsibility to read and understand these policies.
Note that any instance of academic dishonesty will be reported to the Academic Integrity Administrative Office for disciplinary action and is cause for a failing grade in the course.

### Notes relating to this course

As noted above, it is expected that students in this course will have some degree of collaboration on and discussion of homework assignments, but each student must submit (for all homework assignments, assigned problems, etc.) their own code, their own results, and their own discussion of these results.
Copying the work of others is not permitted, though *discussion* of results, code, and results is permitted.
One practical place to draw the line is that if you are reading from someone else's screen, e-mail, or other communication while you are writing code/completing your assignment, you are in violation of this policy, and likewise if someone is typing code for you.
In contrast, if you look at someone else's code briefly, discuss it with them, then return to working on your own code without copying or memorizing their work, you are not violating this policy.
