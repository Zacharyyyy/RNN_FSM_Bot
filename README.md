# RNN_FSM_Bot

Code for the finite state machine(FSM), that can recognise simple English grammar.

A Facebook messenger bot based on this finite state machine

Code of the recurrent neurall network(RNN) which learn the finite states  machine(FSM) will be given in another github page.

## How RNN learns FSM in brief
![](https://i.imgur.com/GJTnDk6.png)
In short, the RNN takes a word vector "W" and a state vector "S" as the input vector. "W" means the next word read, the value should be 1 on the corresponding position, and 0 for the rest. "S" means the current state, the value should be 1 on the current state and 0 for the rest. Transition tensor is the part that calculate the probability of going from one x state to y state through word z. And we normalize the output of transition tensor, so the outputs add up to 1, and can be seen as probability.  The output of normalized values are fed back as the input. It is a pretty intuitive thing to do. Since the nextt state depends on the current state and the next word.
A link for more explanation of how the RNN works is in the reference.

## The FSM(words shown)
![](https://i.imgur.com/i4v7Q4N.png)
### States
* 4 states, initial state: 0, final states: 2, 3
### limited dictionary: 
* noun (singular): boy, girl, book, pencil, pen, burger, cup, computer, phone, apple
* noun (plural): boys, girls, books, pencils, pens, burgers, cups, computers, phones, apples
* B_verb: is , are, am
* P: I, he, she, it
* Other: this, that, these, those, not, a, an, the, with
* verb1: read, write, eat, use, drink, have
* verb2: reads, writes, ears, uses, drinks, has
## The FSM
![](https://i.imgur.com/Z94C8qP.png)
### Condtions
* zero_to_zero
* zero_to_one
* zero_to_two
* zero_to_three
* one_to_zero
* one_to_one
* one_to_two
* one_to_three
* two_to_zero
* two_to_one
* two_to_two
* two_to_three
* three_to_zero
* three_to_one
* three_to_two
* three_to_three
## Reference
* Automation_Generator https://github.com/pgrachev/Automaton-Generator
* Reading about Neural network for synthesizing deterministic finite automata https://www.sciencedirect.com/science/article/pii/S1877050917323724
* More detail of the RNN https://github.com/Zacharyyyy/RNN
