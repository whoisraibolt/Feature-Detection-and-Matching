# Feature Detection and Matching

![GitHub language count](https://img.shields.io/github/languages/count/whoisraibolt/Feature-Detection-and-Matching)
![GitHub top language](https://img.shields.io/github/languages/top/whoisraibolt/Feature-Detection-and-Matching)
![GitHub repo size](https://img.shields.io/github/repo-size/whoisraibolt/Feature-Detection-and-Matching)
![GitHub](https://img.shields.io/github/license/whoisraibolt/Feature-Detection-and-Matching)

Feature Detection and Matching between two images using Local Feature Descriptors and Local Binary Descriptors through the Brute Force and FLANN algorithms.

From this application it is possible to solve several problems in the area of Computer Vision, such as: image recovery, motion tracking, motion structure detection, object detection, recognition and tracking, 3D object reconstruction, and others.

## Overview

This project performs Feature Detection and Matching with SIFT, SURF, KAZE, BRIEF, ORB, BRISK, AKAZE and FREAK through the Brute Force and FLANN algorithms using Python (version 3.6.10) and OpenCV (version 3.3.1).

![Feature Detection and Matching with KAZE through the Brute Force algorithm](https://raw.githubusercontent.com/whoisraibolt/Feature-Detection-and-Matching/master/Figures/BF-with-KAZE.png)

## Dependencies

To install the dependencies run:

`pip install -r requirements.txt`

## Usage

`python main.py --detector <detector> --descriptor <descriptor> --matcher <matcher>`

| Arguments     | Info                                                                    |
| :------------ | :---------------------------------------------------------------------- |
| `-h`, `--help`| Show help message and exit                                              |
| `--detector`  | Specify SIFT or SURF or KAZE or ORB or BRISK or AKAZE                   |
| `--descriptor`| Specify SIFT or SURF or KAZE or BRIEF or ORB or BRISK or AKAZE or FREAK |
| `--matcher `  | Specify BF or FLANN                                                     |

## Examples

####  Help
`python main.py --help`

#### Brute Force with ORB
`python main.py --detector ORB --descriptor ORB --matcher BF`

## Recommended Readings
- [Feature Detection and Description](https://github.com/whoisraibolt/Feature-Detection-and-Description "Feature Detection and Description")

- KRIG, Scott. [Computer vision metrics: Survey, taxonomy, and analysis](https://link.springer.com/content/pdf/10.1007%2F978-1-4302-5930-5.pdf "Computer vision metrics: Survey, taxonomy, and analysis"). Apress, 2014.

- [Keypoints and Descriptors](https://www.cs.utah.edu/~srikumar/cv_spring2017_files/Keypoints&Descriptors.pdf "Keypoints and Descriptors")

- [Feature Detection and Matching](https://www.comp.nus.edu.sg/~cs4243/lecture/feature.pdf "Feature Detection and Matching")

## License

Code released under the [MIT](https://github.com/whoisraibolt/Feature-Detection-and-Matching/blob/master/LICENSE "MIT") license.
