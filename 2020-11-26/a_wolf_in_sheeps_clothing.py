def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        wolf = len(queue) - queue.index("wolf") - 1
        return f"Oi! Sheep number {wolf}! You are about to be eaten by a wolf!"


#Shorter way
#def warn_the_sheep(queue):
#    n = len(queue) - queue.index('wolf') - 1
#   return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'