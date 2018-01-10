# Content relating to UCI's PharmSci 175/275, Drug Discovery Computing Techniques

## What's here
This will provide course materials for UCI's PharmSci 175 and 275 courses, which are currently taught in parallel, with 175 being the undergraduate version.
This will ultimately contain syllabus information, lecture notes and slides, required reading, sandboxes and examples used in class, and assignments.

## Manifest
- [`getting-started.md`](getting-started.md): provides information on basic software requirements for the class and where to get started
- [`continuing.md`](continuing.md): Helpful tips for continuing on AFTER having followed getting started information
- [`syllabus.md`](syllabus.md): Syllabus for PharmSci 175/275
- [`assigned_materials.md`](assigned_materials.md): Assigned reading/instructional materials for the course, for use with the detailed schedule as posted on Canvas.
- [`docs`](docs): Directory containing documentation/background reading relating to the course, which are usually linked to from elsewhere in this material.
- `175`: Undergraduate course (PharmSci 175)-specific materials (e.g. assignments)
- `275`: Graduate course (PharmSci 275)-specific materials (e.g. assignments)

## Getting Started
- **[Setup and Installation](getting-started.md)**
- **[How to use Jupyter Notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)**

## Requirements

Exact steps for installing the software you need are detailed in [`getting-started.md`](getting-started.md), but for the ambitious, note you will want the following installed and working among other things:
- [Anaconda Python](https://www.continuum.io/downloads): Anaconda is the leading open data science platform powered by Python.
- [VMD](http://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD): VMD is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting.
  - Recommended Tutorials:
    - [Introduction](http://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node1.html)
    - [Working with a Single Molecule](http://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node2.html)
    - [Trajectories and Movie Making](http://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node3.html)
- [OpenEye-toolkits](https://www.eyesopen.com/toolkit-development)
  - [Documentation](https://docs.eyesopen.com/toolkits/python/index.html)

- **Optionals:**
  - [Atom](https://atom.io/): GitHub's official text editor with so many plugins.
  - [VIDA](https://www.eyesopen.com/vida): Molecular viewer for OEB files. (Requires OpenEye license)

#### Cheatsheets and dotfiles
Under the **uci-pharmasci/docs/** directory, we have included some useful command cheat sheets for [BASH](https://github.com/nathanmlim/blues-apps/tree/master/docs/bash_cheatsheet.jpg) and [vi](https://github.com/nathanmlim/blues-apps/tree/master/docs/vi_cheatsheet.pdf).

We also have a [Github](https://www.evernote.com/shard/s26/sh/ae73a67b-4d7a-4e97-a896-cef5473db895/178762935c73b559) cheat sheet/tutorial on our group Evernote. I also recommend checking out the [CodeAcademy Github](https://www.codecademy.com/learn/learn-git) tutorial.

We have also included several _dotfiles_ (configuration files with filenames beginning with the `.` character) for VMD and Vim to set some common default settings.
