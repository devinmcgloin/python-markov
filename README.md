# python-markov
Python Markov is a simple interface in python to create and use Markov Chains. The simple markov chain, and performat markov chain are designed to be used with any data type, the string one works only on strings. The constructors for all markov classes in this package take any iterable item, this means parsing the text is up to you. It also means these models will work with musical notes, pixel colors, dance moves, whatever. You just have to make it iterable.

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

All of these markov chains implement `__iter__`, so you can generate theoretically infinite chains. I say theoretically, as it depends on the datasource you're using. Before iterating you have to set the starting state.

```python

chain.random_state() # Selects a random start point. You can specify with set_state()
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
### Performant Markov
Reads from the data source once, and calculates percentages. Does not store the content inside the chain. Cannot have variable length chains.
### Text Markov
Text Markov assumes you're working with text data, and gives you advantages on text based chains. Most noteably it allows you to work with sentences, and get back sentences. As well as fuzzy matching inorder to get a seed value.
