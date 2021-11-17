'''
Usage:
python VCFAnnotation.py -i input_vcf_file -o output_annotation_file -p ./ExAC_allel_freq.pkl

This program annotate each variant in the input vcf file

'''



import re
import argparse
import pickle



def main():
   args = Parser()
   VCFAnnotation(args.i, args.o, args.p)
   return 0



def Parser():
   parser=argparse.ArgumentParser('')
   parser.add_argument('-i', required=True, help = 'the input VCF file name')
   parser.add_argument('-o', required=True, help = 'the output VCF file name')
   parser.add_argument('-p', help = 'the path of the ExAC_allel_freq.pkl file', default = './ExAC_allel_freq.pkl')
   return parser.parse_args()



def ExtractCol(line, first_split_char, second_split_char, info_index):
   tem = line.split(first_split_char)
   return tem[1].split(second_split_char)[info_index] if len(tem)>1 else ''



def ExtractANN(line):
   res = {}
   ann_list = line.split(';ANN=')[1].split(';')[0]
   for ann in ann_list.split(','):
      alt, effect = ann.split('|')[:2]
      if alt not in res: res[alt] = effect
   return res



def VCFAnnotation(input_file, output_file, database_file):
   exac_database = pickle.load(open(database_file,'rb')) 
   with open(input_file) as f, open(output_file,'w') as w:
      w.writelines('\t'.join(['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','VarType','VarEff','DP','AO','AO:RO','ExAC_alle_fre'])+'\n')
      for line in f:
         if not re.search('^#',line): 
            chrom, pos, id, ref, alt_list, qual, filter, info = line.split()[:8]
            type_list = ExtractCol(info, 'TYPE=', ';', 0).split(',')
            ann_dict = ExtractANN(info)
            dp = ExtractCol(info, ';DP=', ';', 0)
            ao = ExtractCol(info, ';AO=', ';', 0).split(',')
            ro =  ExtractCol(info, ';RO=', ';', 0)
            for index, alt in enumerate(alt_list.split(',')): 
               ann = ann_dict[alt] if alt in ann_dict else '.'
               key = '-'.join([chrom,pos,ref,alt])
               exac_fre = exac_database[key] if key in exac_database else '.'
               w.writelines('\t'.join([chrom,pos, id, ref,alt, qual, filter, type_list[index], ann, dp, ao[index], ao[index]+':'+ro, exac_fre])+'\n')
   return 0



###
if __name__ == '__main__': 
   main()

