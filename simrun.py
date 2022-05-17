#!/usr/bin/env python

import numpy as np
import string
import random

class simple:

    def __init__(self,num_obs):
        self.num_obs=num_obs
        self.func_dict={'float':np.random.uniform,
                        'int' : np.random.randint,
                        'cat':np.random.choice}

    def numeric(self,single_range=None,dict_range_prob=None,type=None):

        # pass the ranges as tuples in dict_range_prob

        if single_range is not None:

            return self.func_dict[type](*single_range,self.num_obs)
        
        if dict_range_prob is not None :

            temp=[]

            for key in dict_range_prob.keys():

                temp.extend(self.func_dict[type](*key,int(self.num_obs*dict_range_prob[key])))

            return(temp)

    def cat(self,choices=None,dict_choices_prob=None):

        if choices is not None:

            return(self.func_dict['cat'](choices,self.num_obs))

        if dict_choices_prob is not None:

            return(self.func_dict['cat'](list(dict_choices_prob.keys()),self.num_obs,p=list(dict_choices_prob.values())))

    def ID(self,chars=None):

        temp=[]

        for i in range(self.num_obs)

        temp.append(''.join(random.choices(string.ascii_uppercase +string.digits, k = chars)))

    



    
class nested_pair :

    def __init__ (self,nested_in=None):

        self.nested_in=nested_in
        self.func_dict={'float':np.random.uniform,
                        'int' : np.random.randint,
                        'cat':np.random.choice}

    def cat_nested_in_numeric(self,choices=None,nested_probs=None):

        # example 
        # choices =["a","b"]
        # nested_prob={(18,45):[0.2,0.8],(46,90):[0.6,0.4]}

        # this essentially implies that , say in age range 18,45 , marital statuses a,b appear with different probability vs age range 46,90
        # this can probably be made faster

        # also right now i have not included a way to preserve order which we can by adding a temp id and later sorted by this before returning

        ranged_subsets={}

        for _range in nested_probs.keys():

            ranged_subsets[_range]=np.array(self.nested_in)[np.array(self.nested_in)>=_range[0] & np.array(self.nested_in)<=_range[1]]

        temp=[]

        for _range in nested_probs.keys():

            temp.extend(zip(ranged_subsets[_range],self.func_dict['cat'](choices,len(ranged_subsets[_range]),p=nested_probs[_range])))

        return(temp)





    


        

            