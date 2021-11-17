# VCFAnnotation
A program to annotate variants in a VCF file 


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
|Col|Abbrv.|Description|
|---|---|---|
|1|CHROM|Chromosome|
|2|POS|The reference position|
|3|ID|Identifier|
|4|REF|Reference base(s)|
|5|ALT|Alternate base(s)|
|6|QUAL|Quality|
|7|FILTER|Filter status|
|8|VarType|Type of variation|
|9|VarEff|Variant Effect|
|10|DP|Depth of sequence coverage at the site of variation|
|11|AO|Number of reads supporting the variant|
|12|AO:RO|Reads supporting the variant versus reads supporting reference reads|
|13|ExAC_alle_fre|Allele frequency of variant from ExAC database. If this variant is not in the database, the value will be '.'|





