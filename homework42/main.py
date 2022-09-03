import pygal
import random

view = pygal.Line()

# set title
view.title = 'Numbers'

# add data
view.add('1-20', [e for e in range(1, 21)])
view.add('Random', [d for d in random.sample(range(1, 21), 20)])




view.render_in_browser()


view = pygal.Pie()

# set title
view.title = 'Raspberry Pi Selling'

view.add('400', 25)
view.add('4', 60)
view.add('3', 5)
view.add('2', 10)

view.render_in_browser()