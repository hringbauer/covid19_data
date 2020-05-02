@author Harald Ringbauer,  March 20th 2020

This is a project to analyze data from publicly available COVID19 viral data.

The goal is to use genetic data to learn about key parameters and whether they vary across strains (e.g. virality), 2) To learn about the history of the outbreak and 3) to develop a realtime analyiss tool.

To align sequences:
1) Download the fasta from gisaid
Sometimes they have blank lines in the beginning. Remove these

Downoad meta data from nextstrain git. 

2) Copy these two files into `./data`

3) run `notebooks/process_data/align_fasta`
follow instructions there, top to bottom

4) run `notebooks/create_h5.ipynb`
follow instructions there