####################################################
import sys
sys.path.append('..')
from assign02 import *
from assign02_01 import *
####################################################
print("[import ./../assign02.py] is done!")
####################################################
#
# Please implement (10 points)
# mylist_quicksort (see list_quicksort in assign02.sml)
#
####################################################


def mylist_quicksort(xs):

    def qsort(xs):
        if mylist_nilq(xs):
            return mylist_nil()
        else:
            x1, xs= xs.get_cons1(), xs.get_cons2()
            ys, zs = qpart(xs, x1)
            return mylist_append(qsort(ys),mylist_append(mylist_cons(x1, mylist_nil()),qsort(zs)))

    def qpart(xs, p0):
        if mylist_nilq(xs):
            return xs, xs
        else:
            x1, xs = xs.get_cons1(), xs.get_cons2()
            ys, zs = qpart(xs, p0)
            if x1 <= p0:
                return mylist_cons(x1, ys), zs
            else:
                return ys, mylist_cons(x1, zs)
    
    return qsort(xs)


