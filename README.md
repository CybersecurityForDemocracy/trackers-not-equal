# Tracker Installations Are Not Created Equal: Understanding Tracker Configuration of Form Data Collection

## Abstract
Targeted advertising is fueled by the comprehensive tracking of users' online activity. As a result, advertising companies, such as Google and Meta, encourage website administrators to not only install tracking scripts on their websites but configure them to automatically collect users' Personally Identifying Information (PII). In this study, we aim to characterize how Google and Meta's trackers can be configured to collect PII data from web forms. We first perform a qualitative analysis of how third parties present form data collection to website administrators in the documentation and user interface. We then perform a measurement study of 40,150 websites to quantify the prevalence and configuration of Google and Meta trackers.

Our results reveal that both Meta and Google encourage the use of form data collection and include inaccurate statements about hashing PII as a privacy-preserving method. Additionally, we find that Meta includes configuring form data collection as part of the basic setup flow. Our large-scale measurement study reveals that while Google trackers are more prevalent than Meta trackers (72.6\% vs. 28.2\% of websites), Meta trackers are configured to collect form data more frequently (11.6\% vs. 62.3\%). Finally, we identify sensitive finance and health websites that have installed trackers that are likely configured to collect form data PII in violation of Meta and Google policies. Our study highlights how tracker documentation and interfaces can potentially play a role in users' privacy through the configuration choices made by the website administrators who install trackers.  

If you publish work based on the source code in this repository, please cite the paper as follows:

```
@inproceedings{pets2025trackerconfigs,
  title     = {Tracker Installations Are Not Created Equal: Understanding Tracker Configuration of Form Data Collection},
  author    = {Kieserman, Julia B. and Andreou, Athanasios and Geeng, Chris and Lauinger, Tobias and McCoy, Damon},
  booktitle = {Proceedings on Privacy Enhancing Technologies (PoPETs)},
  volume    = {2025},
  issue     = {3},
  year      = {2025}
}
```

## Data
There are two sources of data in this repository:
1. The Meta and Google documentation used for qualitative analysis (Section 3 of the paper) in `documentation-and-ui-analysis/data`.
2. The parsed website data used for analysis (Section 4 of the paper) in `website-configurations/data-analysis/data`.

## Instructions
Our pipeline is divided into three parts; as a result, there are three respective sections of the repository that can be executed independently. The specific instructions for setting up and running each section can be found in the `README.md` file within each subdirectory.

1. Data Collection (`website-configurations/data-collection`)
2. Data Parsing (`website-configurations/data-parsing`)
3. Data Analysis (`website-configurations/data-analysis`)

Additionally, we include a standalone Chrome extension that can be deployed to notify users when Meta Pixel is configured for Form Data Collection (`meta-pixel-configuration-checker`), which we refer to in the paper as a proof-of-concept for a possible mitigation technique for tracking.
