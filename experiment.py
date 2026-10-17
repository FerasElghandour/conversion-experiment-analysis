"""Conversion experiment inference from sufficient counts."""
import argparse
import json
import math
import numpy as np

def compare(control_converted,control_total,treatment_converted,treatment_total,draws=10000,seed=42):
    for made,total in [(control_converted,control_total),(treatment_converted,treatment_total)]:
        if type(made) is not int or type(total) is not int or total<=0 or not 0<=made<=total:raise ValueError('Valid integer counts required')
    if type(draws) is not int or draws<1:raise ValueError('Positive simulation budget required')
    pc,pt=control_converted/control_total,treatment_converted/treatment_total
    diff=pt-pc;pooled=(control_converted+treatment_converted)/(control_total+treatment_total)
    rng=np.random.default_rng(seed)
    null=rng.binomial(treatment_total,pooled,size=draws)/treatment_total-rng.binomial(control_total,pooled,size=draws)/control_total
    se=math.sqrt(pc*(1-pc)/control_total+pt*(1-pt)/treatment_total)
    return {'control_rate':pc,'treatment_rate':pt,'difference':diff,
       'difference_normal_95_interval':[diff-1.96*se,diff+1.96*se],
       'null_draws':draws,'right_tail_adjusted_p':float((1+np.count_nonzero(null>=diff))/(draws+1)),'seed':seed}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--draws',type=int,default=10000);args=parser.parse_args()
    print(json.dumps(compare(3650,34678,5469,35211,args.draws),indent=2))
