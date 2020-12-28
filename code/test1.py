import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='DVC')
    parser.add_argument('--f_in', type=str, metavar='N', default='../data/in1.txt')
    parser.add_argument('--f_out', type=str, metavar='N', default='../repro/out1.txt')
    
    args = parser.parse_args()
     
    f_in = args.f_in
    f_out = args.f_out
    
    fh_in = open(f_in,'r')
    fh_out = open(f_out,'w')
    
    lines = fh_in.read()
    fh_out.write(lines)
    
    line = '\n\nThis is for out1.txt'
    fh_out.write(line) 
    
    fh_in.close()
    fh_out.close()
    
