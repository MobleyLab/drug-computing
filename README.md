# Drug Discovery Computing Techniques: Educational Materials

This repository provides an introduction to computing techniques in drug discovery, and presents educational materials for David Mobley's course Drug Discovery Computing Techniques (PharmSci 175/275), taught at UC Irvine.
Materials here focus on providing an introduction to computing techniques in drug discovery, including (but not limited to) topics covered in the course.

## Repository goals

This repository has two main goals:
1) To provide a general introduction to computing techniques used in drug discovery which will be broadly useful to the community, including providing access to course-specific materials which may be of broader utility.
2) To give UCI PharmSci 175/275 students access to the materials they need for their course, as well as other relevant material which may be of interest.

In its initial stages, this will contain primarily material for item (2) as this provides the initial content for the repository.
However, a goal is that this repository may also broaden to encompass material not directly related to the class (perhaps including related materials that others use in similar classes), and perhaps even could eventually provide tutorials which could be suitable for publication such as in the [Living Journal of Computational Molecular Science](http://www.livecomsjournal.org/).

## Organization

In keeping with the two goals above, this repository is broadly organized to clearly delineate materials which students specifically need for UCI's PharmSci 175/275 from those which are here for other purposes, such as background material or tutorials on related or peripheral topics which are not specifically needed for the course.
Usually each level of organization will have a `README.md` file, like this one, which explains what you can find there and how to navigate around. 

### Overall layout
Current organization is simple: At the base level is `uci-pharmsci` which provides materials relating to UCI's PharmSci 175/275 courses, and `other-materials` which contain other content.

### Manifest
- `README.md`: This document
- `LICENSE`: A CC-BY 4.0 license giving others to reuse this content and do a variety of other things with it as long as credit is given.
- `other-materials`: A directory which will contain materials not explicitly used in/required for UCI's PharmSci 175/275 course, but which may be referenced from there or from other courses.
- `uci-pharmsci`: Content directly utilized in and (usually) required for UCI's PharmSci 175/275 course.

## Requirements

The content here has a variety of requirements which vary depending on the topic, especially if you want to use the tutorial/interactive material which involve the interactive Jupyter notebooks environment for Python.
Many of the materials also require an OpenEye license, which is free for academics (though if you are in PharmSci 175/275, you can use our educational license for that course).
PharmSci 175/275 students should begin with [Getting Started](uci-pharmsci/getting-started.md) for installation instructions.

## Contributing

If you would like to contribute to this repository, please raise issues on the issue tracker or if you have changes you would like to propose to the material here, submit a pull request.
Potentially, the repository could be broadened to include materials for other, related courses at different institutions; please contact us if you would like to propose this, but it's certainly a possibility we would like to pursue.
We could potentially add folders at the base level for additional courses in addition to UCI's PharmSci 175/275.

## Authors
In general, authorship will be noted in the individual documents presented.
The current primary authors are:
- David L. Mobley, UC Irvine

However, this material also draws heavily (with permission) on content adapted from M. Scott Shell's ["Principles of modern molecular simulations"](https://engineering.ucsb.edu/~shell/che210d/assignments.html) course at UC Santa Barbara; when material is adapted from Shell, this will typically be noted in the content itself and he should be acknowledged if it is reused in any form.


## Acknowledgments

We would like to particularly acknowledge:
- M. Scott Shell for his excellent course material (see [Authors](#authors))
- OpenEye Scientific Software for extending a free academic license (which much of our content relies heavily on)
- The previous students of PharmSci 275 for their contributions to this content and notes on what was unclear, etc.
- James Haigh at OpenEye Scientific Software for answering many support questions over the years which helped me, both directly and indirectly, in developing the portions o fthis content utilizing OpenEye tools
- John Chodera (MSKCC), from whom I (Mobley) learned a great deal when we were both at UCSF and afterwards. His contribution here is hard to quantify or even identify directly -- I've used so much of his code over the years, reading it, modifying it, repurposing it, and moving it around from one place to another that possibly some snippets from his code occur in some of the materials here without me realizing it. Certainly some of this material draws heavily on [openmoltools](http://github.com/choderalab/openmoltools) which Chodera and I and others have both contributed substantially to, and which draws on even earlier material we began preparing when we were both at UCSF. 
- The many contributors to [openmoltools](http://github.com/choderalab/openmoltools)

Additional acknowledgments will be given in specific content. 
