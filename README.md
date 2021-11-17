# VCFAnnotation
A program to annotate each variant in the file 


## Installation
Download the ‘ExAC_allel_freq.pkl’ file (allele frequency in ExAC database) from the link below: 

https://filetransfer.io/manage-package/2q7g12ol

## Dependencies
The implementation of VCFAnnotation is based on Python 3.6. It depends on 2 Python packages (`re`,`pickle`).


## Input data
1. ExAC_allel_freq.pkl
2. Variants file in VCF format


## Usage
Sample run using the test VCF file in the repo
```
Python VCFAnnotation.py –i test/Challenge_data_with_SnpEff.vcf –p ExAC_allel_freq.pkl –o annotation_Challenge_data_with_SnpEff.tsv
```

## Output data


