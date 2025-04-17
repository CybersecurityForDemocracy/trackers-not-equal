# Analysis Notebooks

In this folder, we include all the results that are presented in the quantitative section of paper.

## Instructions

The *requirements.txt* contains all the depdendencies that are required to run the notebooks:

```bash
pip install -r requirements.txt
```

The analysis code has been tested with Python3.8.

## Tables

The *table_i.ipynb* files generate the tables that contain results from our analysis in the paper. If you wish to compile them in a latex environment you need to include the following macros.

```latex
\definecolor{lightgray}{gray}{0.9}

\newcommand{\mpixel}[1][]{\textit{Meta Pixel#1}\xspace}
\newcommand{\gpixel}[1][]{\textit{Google Tag#1}\xspace}

\newcommand{\statica}[1][]{%
  \ifx\relax#1\relax
    FDC configuration\xspace
  \else
    \if#1uFDC Configuration\xspace\else FDC configuration#1\xspace\fi
  \fi
}

\newcommand{\dynamica}[1][]{%
  \ifx\relax#1\relax
    form data collection\xspace
  \else
    \if#1uForm Data Collection\xspace\else form data collection#1\xspace\fi
  \fi
}

\newcommand{\tracker}[1][]{%
  \ifx\relax#1\relax
    tracker installation\xspace
  \else
    \if#1uTracker Installation\xspace\else tracker installation#1\xspace\fi
\fi
}
```

## Regression Analysis

The *regression_analysis* folder contains the code that generates the regression analysis results presented in *table_7.ipynb*. You can use this code in order to generate *regression_analysis_google_model.pkl* and *regression_analysis_meta_model.pkl* (which are already included in the repository), and see more information about the analysis results.

## Measurements not on tables.

Results measurements that are not included in the tables but are referrenced through out the paper are presented in *measurements_non_table.ipynb*, with the exception of measurements on our validation samples that are referenced in *4.2 Dataset Overview and Validation*. These are presented in *measurements_validations.ipynb*.

## Samples
The *samples* folder contains the websites we used for manual validation, as reported in Section 4.2 of the paper. Note that `TRUE` means that the website was correctly classified and `FALSE` means it was incorrectly classified. For example, a website labeled as `TRUE` in `no_detected_gtag_installation.csv`, indicates that the website indeed did not have a Google Tag installed when reviewed manually.

## Data
The *data* folder contains the parsed datasets used for our analysis and the generated tables in our paper. The following csv files are included:

### `websites.csv` includes the final dataset of websites we successfuly visited and analyzed
The columns can be interpreted as follows:
- `url`: the url of the website
- `has_gtag`: if the website had a Google Tag installation
- `has_meta_pixel`: if the website had a Meta Pixel installation
- `google_form_data_collection`: if the website had an instance of Google Tag Form Data Collection
- `meta_form_data_collection`: if the website had an instance of Meta Pixel Form Data Collection
- `form_data_collection`: if the website had any instance of Form Data Collection
- `meta_form_data_configuration`: if the website had Meta Pixel Form Data Collection
- `rank`: the Tranco rank of the website
- `is_health`: if the website was classified as a health website by SimilarWeb
- `is_finance`: if the website was classified as a finance website by SimilarWeb

### `meta_key_analysis.csv` includes the final dataset of websites with Meta Pixel configurations
The columns can be interpreted as follows:
- `url`: the url of the website
- `is_default_key_list`: if the list of PII keys that the Meta Pixel is configured to collect matches the user interface default behavior (which automatically selects all keys). A screenshot of the user interface is presented in the paper, Appendix Figure 6
- `key_list`: the list of PII keys the Meta Pixel is configured to collect