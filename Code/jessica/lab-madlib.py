name = input ('what is your name?')

output = 'hello name {}!'.format(name)
print(output)


adjective = input ('give me an adjective')
plural_noun = input ('give me a plural noun')
plural_noun2 = input ('give me another plural noun')
silly_word = input ('give me a silly word ')
type_of_liquid = input ('give me a type of liquid')

output = 'American children are fascinated by {0}stuff like stories that scare the {1} off them or make their {2} stand on end. Scientists say this is because being frightened causes the {3} gland to function and puts {4} into their blood.'.format(plural_noun, adjective, plural_noun2, silly_word, type_of_liquid)

print (output)
