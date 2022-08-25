basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 
True
'crabgrass' in basket
False
a = set('abracadabra')
b = set('alacazam')
a                                  
{'a', 'r', 'b', 'c', 'd'}
a - b                              
{'r', 'd', 'b'}
a | b                              
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                         
{'a', 'c'}
a ^ b                              
{'r', 'd', 'b', 'm', 'z', 'l'}
a = {x for x in 'abracadabra' if x not in 'abc'}
a
print(a)