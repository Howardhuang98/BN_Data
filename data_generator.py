#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   data_generator.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/9/3 22:06  
------------      
"""

# use Bayesian Model Sampling method to generate data

from pgmpy.readwrite import BIFReader
from pgmpy.sampling import BayesianModelSampling


def sample(path: str, size, output_path):
    reader = BIFReader(path)
    model = reader.get_model()
    s = BayesianModelSampling(model)
    data = s.forward_sample(size=size)
    data.to_csv(output_path)


if __name__ == '__main__':
    sample(r"datasets/bnlearn/survey/survey.bif", 1000, r"datasets/bnlearn/survey/survey.csv")
