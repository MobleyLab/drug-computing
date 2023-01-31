# PharmSci 175/275 Assigned Materials

This details (and links to, when possible) materials covered in PharmSci 175/275, and can be used together with the detailed schedule posted on EEE Canvas, to see exactly what you should be doing when.

Please note that materials which are specific to the undergraduate or graduate versions are indicated with (175) or (275) in parentheses, respectively, and materials which have no such indication are required for all students.

**In general, try and come to class with the course content already working.** If you are using Google Colab, this means you will need to allow a few minutes before the start of class to run software installation, as each Google Colab session needs works in a separate "runtime" and needs software installed from scratch.

## Materials by lecture number

### Before the course starts
Before the course starts, you should do the following:
- Read [`docs/why_computing.md`](docs/why_computing.md), a brief background document on why we are starting where we are
- Read through and/or follow the steps in [`getting-started.md`](getting-started.md) to install the software you need, if you are installing locally (if you are using Google Colab, you will install each time you begin a session; allow extra time for this). Historically, use of Linux/bash scripts was quite important, but if you are using Google Colab here that will be less important (though still worthwhile if you're doing scientific computing in general).
- Visit the [Python intro](../other-materials/python-intro/README.md) in [`../other-materials`](../other-materials) and check out the Jupyter notebooks and [Python crashcourse](../other-materials/python-intro/python_crashcourse.md) available there to make sure your Python is ready for the course.
- Try out a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html); do so on Google Colab if you plan on going that route. [Here's a great starting point on Google Colab which will work right in your web browser without any installation](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

### Before Lecture 1 ([Python and Linux](lectures/Python_Linux_Vi))
To prepare for Lecture 1, on Python, Linux, text editors, and GitHub, please:
- Download the [course GitHub repository](https://github.com/mobleylab/drug-computing) from GitHub (download as a zip file if you like, or if you have used `git` before, feel free to clone the repository instead)
- Take a quick look through the slides in `uci-pharmsci/lectures/Python_Linux_Vi`; view as a Jupyter notebook via `jupyter notebook Lec1_Python_Linux_Vi.ipynb` (interactive) if you are running locally, otherwise use Google Colab via the link in the notebook
- Make note of any questions to bring up in class, and also visit the Python materials above as needed.
- Ideally create a (free) GitHub account in case there are issues with the course materials that you want to bring up on the GitHub repository, which houses most of our course materials.

### Before Lecture 2 ([Energy landscapes and energy minimization](lectures/energy_minimization))
- Read the energy minimization Jupyter notebook/slides in [`lectures/energy_minimization/energy_minimization.ipynb`](lectures/energy_minimization/energy_minimization.ipynb)

### Before Lecture 3 ([3D structure and shape](lectures/3D_structure_shape))
- If you don't already have a chemistry drawing tool like ChemDraw that you like, you may wish to download and install [MarvinSketch](https://www.chemaxon.com/products/marvin) for free from ChemAxon. (Though in a pinch, you can use the web demo version linked from the lecture slides if you need.)
- Read the 3D structure/shape Jupyter notebook [`lectures/3D_structure_shape/3D_Structure_Shape.ipynb`](lectures/3D_structure_shape/3D_Structure_Shape.ipynb)

## Before Lecture 4 ([QM](lectures/QM))
- Skim through the PDF of the slides, noting any questions (though these provide theoretical background for subsequent classes so they are unfortunately not interactive)
- If you desire to try a sample QM calculation, open up the Psi4 example (`psi4_example.html` or `psi4_example.ipynb`) and get psi4 installed in a suitable virtual environment as per the instructions there.

## Before Lecture 5 ([MD](lectures/MD)):
- Skim through PDF of the slides, noting any questions for discussion in class
- Review MD sandbox Jupyter notebook in the same directory

## Before Lecture 6 ([MC](lectures/MC)):
- Spend some time with the MD sandbox from Lecture 5
- Skim through the PDF of the MD (part II)/MC slides in the `MC` directory, noting any questions for discussion in class
- Review the MC sandbox Jupyter notebook in the same directory

## Before Lecture 7 ([ChEMBL database work](https://github.com/volkamerlab/teachopencadd/tree/master/teachopencadd/talktorials/T001_query_chembl)
- For this lecture we draw on the [TeachOpenCADD](https://github.com/volkamerlab/teachopencadd) repo
- Clone or download the GitHub repo, or at least the content of the `T001_query_chembl` directory from the `talktorials` directory 
- Skim the content in the `talktorial.ipynb` notebook

## Before Lecture 8 ([Docking, scoring and pose prediction](lectures/docking_scoring_pose)):
- Read the `docking.ipynb` Jupyter notebook in the relevant directory and `old_slides.pdf` there, from the slide numbered 11 (bottom left corner) onwards.

## Before Lecture 9 ([Library searching](library_searching)):
- Skim the [PDF of the slides](lectures/library_searching/Library_lingo_lecture.pdf)
- Check out the relevant sandbox, `Library_searching_and_lingo_sandbox.ipynb`, in the relevant directory.

## Before Lecture 10 ([Ligand-based design](ligand_based_design)):
- Skim the [PDF of the slides](lectures/ligand_based_design/ligand_based_design_slides.pdf)
- Try out the Jupyter notebook, `ligand_based_design.ipynb`, in the relevant directory.

## Before Lecture 11 ([Empirical models/physical properties/QSAR](empirical_physical_properties)):
- Skim the [PDF of the slides](lectures/empirical_physical_properties/physprops.pdf) and come with questions/comments

## Before Lecture 12 ([Fluctuations, correlations, error analysis](lectures/fluctuations_correlations_error)):
- Skim the PDF of the slides and come with questions/comments

## Before Lecture 13 ([Fluctuations, correlations, error analysis](lectures/fluctuations_correlations_error)):
- Skim through the [Jupyter notebook](error_anlaysis_OpenMM_convergence.ipynb)
- Try to get a sample density calculation running on your computer
- If time allows, think about the optional exercise just following the density calculation

## Before Lecture 14 ([Visualization](lectures/visualization)):
- Skim through the slides on PyMol and VMD
- If you plan on doing the visualization assignment, consult `assignments/visualization` to read about it, so that you know what to focus on during class. Pick whether you are going to do the assignment in PyMol or VMD (PyMol is marginally better for high quality movies of static structures; VMD is far superior for visualization of molecular simulations.)

## Before Lecture 15 ([Simulations in OpenMM with the SMIRNOFF force field](lectures/SMIRNOFF_simulations)):
- Skim through the slides on the OpenFF effort (`SMIRNOFF_simulations/OpenFF_effort.pdf`)
- Take a look at the Jupyter notebooks for mixture simulations and host-guest binding; ideally start working on some of the exercises in the mixture simulations case.

## Before Lecture 16 ([Free energy basics](lectures/free_energy_basics)):
- Skim through the slides (PDF) in `free_energy_basics`.

## Before Lecture 17 ([Clustering and visualization](lectures/cluster_and_visualize)):
- Skim through the slides (Introduction to MSMs.pdf in that directory)
- Make sure you have the jupyter notebooks up and running

## Before Lecture 18:
- (No reading assignment for this lecture; in the past it was a guest lecture by Ioan Andricioaei; hopefully it will be updated for 2022)

## Before Lecture 19 ([proteins](lectures/proteins))
- Skim the slides on working with proteins (proteins.pdf in the relevant directory)

## Before Lecture 20 (on high performance computing, typically with a server room tour)
- No assignment
