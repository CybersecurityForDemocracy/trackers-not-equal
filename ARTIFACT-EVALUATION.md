# Artifact Appendix

Paper title: Tracker Installations Are Not Created Equal

Artifacts HotCRP Id: #3

Requested Badge: **Available**

## Description
This artifact contains the following:
1. The screenshots, documentation, codebook (Table 1), and extracted text elements used in Section 3 of the paper.
2. The data collection and parsing code used in Section 4 of the paper. It includes the Chrome extensions and VM tooling used for data collection and the parsing scripts used for analysis.
3. The final parsed dataset and Jupyter notebooks that generated the data tables (Tables 3-7) and related numbers reported in the paper.
4. A Chrome extension that detects when a Meta Pixel is set up to collect data. When installed, it displays a pop-up whenever a page has a Meta Pixel configured for Form Data Collection, including the specific PII fields that the pixel is configured to collect.

### Security/Privacy Issues and Ethical Concerns
This code does not contain any security risks. However, the mv2 chrome extension does trigger a form submission of fabricated data. Further, both Chrome extensions attempt to download all files present on a webpage and should be used with caution.

## Basic Requirements 
This artifact requires use of a laptop/computer.

### Hardware Requirements
No special hardware requirements.

### Software Requirements
This software has been tested on Mac OS and Linux.

### Estimated Time and Storage Consumption
This artifact does not reproduce the analysis in its entirety. 

## Environment 
Please see the subdirectory README files for details on setup.

### Accessibility
The artifacts can be accessed at this [link](https://github.com/CybersecurityForDemocracy/trackers-not-equal).
