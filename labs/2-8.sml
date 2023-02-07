fun h1 x = 1;
fun h2 x = h1 x;
fun h3 x = h4 x
and
h4 x = 2;



val x = h1 1;
val y = h2 1;
val z = h3 1;