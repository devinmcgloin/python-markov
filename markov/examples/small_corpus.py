from markov.chain.markov_simple import markov_chain



s = "Elderly man’s fishing net hangs in his shed \
The fish he caught in his backyard stream multiply \
Net use was banned; he couldn’t afford a pole \
Joy and sustenance gone, a tear falls from his eye \
House Bill 875 would ban backyard farms \
Forcing vegetable growers to invest cash \
In overpriced produce on supermarket shelves \
Uncle Sam flexes his muscle, makes his whip lash \
The right to freely worship is endangered \
As prayer is prohibited in public schools \
Government intrusion invades all our lives \
Public pleas are not heard by those who make rules \
Freedom to choose our doctors is now threatened \
Socialized medicine diminishes choice \
Speech censorship? Just ask the Smothers Brothers \
Who canceled their own show with a stifled voice \
As crime escalates, look to the constitution \
The NRA spends billions to protect Americans' rights \
To bear arms against oppressors while thieves laugh \
And sue owners of homes invaded in the night \
Can this be what our forefathers had in mind \
When they sought to escape a king’s tyranny? \
Our rights are being limited more each day \
In a nation spawned to promote liberty \
Natural disasters prelude Judgment Day \
Eerie escalation – tsunamis, earthquakes \
But perhaps when the dust finally settles \
Those who survive will learn from our past mistakes \
Governments will form only to preserve peace \
Not to strip away rights ancestors pursued \
Don’t blink!  Precious freedoms are now endangered \
By those who feel they’re elected to intrude".split()

chain = markov_chain(s, 2)
chain.random_state()
print(chain.predict(15))
