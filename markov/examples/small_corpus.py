from markov.chain.markov_simple import markov_chain

# As you can see this program isn't particularly interesting.
# That's because the text is incredibly short, and there is
# no repition.


s = "Be patient, gentlemen. I choose her for myself; \
    If she and I be pleas'd, what's that to you? \
    'Tis bargain'd 'twixt us twain, being alone, \
    That she shall still be curst in company. \
    I tell you 'tis incredible to believe. \
    How much she loves me- O, the kindest Kate! \
    She hung about my neck, and kiss on kiss \
    She vied so fast, protesting oath on oath, \
    That in a twink she won me to her love. \
    O, you are novices! 'Tis a world to see, \
    How tame, when men and women are alone, \
    A meacock wretch can make the curstest shrew. \
    Give me thy hand, Kate; I will unto Venice, \
    To buy apparel 'gainst the wedding-day. \
    Provide the feast, father, and bid the guests; \
    I will be sure my Katherine shall be fine.".split()

chain = markov_chain(s, 2)
chain.random_state()
print(" ".join(chain.predict(15)))
print(chain.random_state())
print(" ".join(chain.predict(35)))
