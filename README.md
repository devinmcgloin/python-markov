# python-markov
Python Markov is a simple interface in python to create and use Markov Chains.

## Syntax 
The content inside the chain is stored as tuples. When you create a chain you need to specify how long you want each node in the chain to be. The longer the chain the more the text will reflect the source text. 
```python
s = "this is a simple example"

chain = markov_chain(s.split(),1) #chain of size 1
# node = ('this') 

chain = markov_chain(s.split(), 3) # size 5
# node = ('this','is','a')
```
You can get the next prediction by using dictionary syntax:
```python
chain[('this','is','a')] 
#>>> 'simple'
chain[('is','a','simple')]
#>>> 'example'
chain[('a','b','c')]
#>>> throws a KeyError
chain[('a','b')]
#>>> throws a TypeError
```

All of these markov chains implement `__iter__`, so you can generate theoretically infinite chains. I say theoretically, as it depends on the datasource you're using.

```python
# this prints out a sequence of items in the chain that can last forever. (be careful)
for item in chain:
    print(item)

# this also works
itertoolz.take(chain, 10)
# its the same as:
chain.predict(10)
```

## Variations

### Simple Markov
Simple Markov is mostly for small toy examples, or playing around with markov chains. It doesn't do well on large datasets, as the chain explicitly stores the text. Because of this you can modify the array while working with it, which is nice to get an intution about whats going on, but not useful if you're playing around with large datasets.
### Performat Markov
Reads from the data source once, and calculates percentages. Does not store the content inside the chain. Cannot have variable length chains. 
### Text Markov
Text Markov assumes you're working with text data, and gives you advantages on text based chains. Most noteably it allows you to work with sentences, and get back sentences. As well as fuzzy matching inorder to get a seed value. 
