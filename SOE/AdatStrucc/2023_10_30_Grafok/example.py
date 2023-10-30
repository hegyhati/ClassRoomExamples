
edges_matrix = [        """    0       1       2       3       4       5"""       
   """ 0 """ [  None,   False,  True,   False,  True,   False ],
   """ 1 """ [  False,  None,   True,   False,  False,  False ],
   """ 2 """ [  True,   True,   None,   False,  False,  False ],
   """ 3 """ [  False,  False,  False,  None,   True,   False ],
   """ 4 """ [  True,   False,  False,  True,   None,   True ],
   """ 5 """ [  False,  False,  False,  False,  True,   None ]
]


edges_neighbor_list = [
    """ 0 """ [ 2, 4 ],
    """ 1 """ [ 2 ],
    """ 2 """ [ 0, 1 ],
    """ 3 """ [ 4 ],
    """ 4 """ [ 0, 3 , 5 ],
    """ 5 """ [ 4 ]
]

    