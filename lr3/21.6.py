#БСБО-05-19 Салынь Даниил Леонидович
wb_tree = []


def fill_wb_tree():
    global wb_tree
    global i
    black = []
    white = []
    black.extend([white, white, white])
    white.extend([black, black])
    wb_tree.append(black)


fill_wb_tree()
