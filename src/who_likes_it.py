"""Kata: Who likes it - implement a function which must take in an input array
containing the names of people who like an item and display "likes" based upon
the input.

#1 Best Practices Solution zadoev, fevjefvn, and others.

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
"""


def likes(names):
    if len(names) == 0:
        return ('no one likes this')
    elif len(names) == 1:
        return ('%s likes this' % (names[0]))
    elif len(names) == 2:
        return ('{} and {} like this'.format(*names))
    elif len(names) == 3:
        return ('{}, {} and {} like this'.format(*names))
    elif len(names) >= 4:
        return ('{}, {} and '.format(*names) + str(len(names) - 2) + ' others like this')
