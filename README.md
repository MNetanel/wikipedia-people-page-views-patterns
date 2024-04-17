# Wikipedia People Page Views Pattern Identification and Analysis

In this work I identify and investigate the commonness of six intuitive different page views patterns of around two
million Wikipedia pages of persons over nine years (2015-2023), using publicly available page views information
and pages data. My goal is to have a better intuitive understanding of different groups of pages by characterizing
the patterns that are present in their views over time.

This project is a final project for the course *The Art of Analyzing Big Data*.

I have uploaded both the page view data and the wikidata entity data to Kaggle, and they are available in [this dataset](https://www.kaggle.com/datasets/netanelmad/wikipedia-people-page-views-data). The verified people dataset by Laouenan et al. (2022) is avialable at [this link](https://data.sciencespo.fr/dataset.xhtml?persistentId=doi:10.21410/7E4/RDAG3O).

If you wish to run the notebooks locally, first create a `.env` file in the following format:
```
RAW_DATA_DIR=path/to/raw_data/directory
PROCESSED_DATA_DIR=path/to/desired/processed_data/directory
```
The `RAW_DATA_DIR` should contain the files from the Kaggle dataset as well as the verified people dataset as `cross-verified-database.csv`.
