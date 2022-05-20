#!/usr/bin/env python

import numpy as np
import string
import random
from IPython.display import display, Markdown
from operator import le,ge,eq
import copy

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

        for i in range(self.num_obs):

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



class data_tree:

    def __init__(self,tree_struct={'parents':{},'splits':{},'obs_prop':{},'vars_ranges':{},'vars_type':{}}):

        self.tree_struct=tree_struct

        # treet strcuture dictionary format :

        # 'parent':{0 :[1,2],1:[3,4]}
        # 'splits': {0 :['var_name',>= or <= or ==, split value of the var]....}} # split should be there for each parent
        # 'obs_prop' : {2:0.2,3:0.3,4:0.6} # obs_prop should be present for all children which are not parent
        # 'vars_ranges' : allowed vars ranges on top of the tree , they will updated for each child as per the path to the child

        self.parents=list(self.tree_struct['parents'].keys())

        self.leafs=set([item for sublist in self.tree_struct['parents'].values() for item in sublist])-set(self.parents)

        self.compare={'>=':ge,'<=':le,'==':eq}

        self.vars_ranges=self.tree_struct['vars_ranges']


    def tree_checks(self):

        error=False

        def parents_should_have_splits():

            for p in self.parents:

                if p not in self.tree_struct['splits'].keys():

                    print(f'parent {p} has no split rules provided')

                    error=True
        
        def children_should_have_obs_prop():

            for c in self.leafs :

                if c not in self.tree_struct['obs_prop'].keys():

                    print(f'leaf node {c} has no obseravtion proportion provided')

                    error=True

        def obs_prop_should_add_up_to_one():

            pop_sum=round(sum(self.tree_struct['obs_prop'].values()),2)

            if pop_sum!=1.0 :

                print(f'population observations do not add upto 100%. it is {pop_sum*100}%')

                error=True
        
        parents_should_have_splits()
        children_should_have_obs_prop()
        obs_prop_should_add_up_to_one()

        if not error:
            print('There were 0 errors found')

    def find_parent(self,child):

        lr={0:'left',1:'right'}
        
        for p in self.parents:

            children=self.tree_struct['parents'][p]

            if child in children:

                return(p,lr[children.index(child)])


    def find_child_path(self,child):

        if child not in self.parents+list(self.leafs):

            print('node is not found')
            return None

        path=[(child,0)]

        reached_root=False

        while not reached_root:

            

            parent=self.find_parent(path[0][0])
            path=[parent]+path
            child=parent
            
            if parent is None : 
                reached_root=True
            
            

        return path[1:-1]

    def child_level_var_ranges(self,child):

        path=self.find_child_path(child)

        _ranges=copy.deepcopy(self.vars_ranges)
        

        for p in path:

            split=self.tree_struct['splits'][p[0]]

            _direction=p[1]
            _var=split[0]
            _sign=split[1]
            _type= self.tree_struct['vars_type'][_var]
            _val=split[2]

            if _type=='cat':

                if _direction=='left':

                    _ranges[_var]=[_val]
                else:
                    _ranges[_var].remove(_val)
            
            if _type=='num':

                if _sign==">=":

                    if _direction=='left':

                        _ranges[_var][0]=_val
                    
                    else:

                        _ranges[_var][1]=_val

                if _sign=="<=":
                    
                    if _direction=='right':

                        _ranges[_var][0]=_val
                    
                    else:

                        _ranges[_var][1]=_val

        return(_ranges)







    








    
        

    


        

            