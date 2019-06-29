# coding: utf-8
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')
import csv
import numpy as np
import pandas as pd
import sys, getopt
def read_data(unifilename, length) :
    
    #unifilename = '../data/feature/peakmerge/modoff/charge2/uni_human_2_'+ str(length) +'_feature_modoff_secondstruture.csv'
    
    with open(unifilename, 'rU') as f:  #opens PW file
        unidataLi = list(list(rec) for rec in csv.reader(f, delimiter=','))
    
    col = len(unidataLi[0])
    
    x = np.asarray([i[1:col - (length-1) * 4] for i in unidataLi[1:]], dtype='f')
    y = np.asarray([i[col - (length-1) * 4 :] for i in unidataLi[1:]], dtype='f')
    name = np.asarray([i[0] for i in unidataLi[1:]])
    
    x.shape=(x.shape[0], x.shape[1], 1)
    
    return x, y, name

def main(argv):
    
    length = 0
    try:
        opts, args = getopt.getopt(argv,"hi:o:l:",["ifile=", "ofile", "len"],)
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outfile> -l <lenth>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile> -l <lenth>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            unifilename = arg
        elif opt in ("-o", "--ofile"):
            writename = arg
        elif opt in ("-l", "--len"):
            length = int(arg)

    unifilename = '../data/feature/z2/uni_human_2_'+ str(length) +'_feature_modoff_secondstruture.csv'
    x, y, name = read_data(unifilename, length)
    model = load_model(f"../data/models/z2/model_length_{length}_fold1.h5")
    output = model.predict(x)

    ion_peak = []
    for i in range(1,length):
        ion_peak.append("b" + str(i) + "+")
    for i in range(1,length):
        ion_peak.append("b" + str(i) + "++")
    for i in range(1,length):
        ion_peak.append("y" + str(i) + "+")
    for i in range(1,length):
        ion_peak.append("y" + str(i) + "++")
    data_pd = pd.DataFrame(output, columns=ion_peak)
    data_pd.insert(loc=0, column='peptide', value=name)
    data_pd.to_csv("../result/output.csv", index=False)

if __name__ == "__main__":
    main(sys.argv[1:])