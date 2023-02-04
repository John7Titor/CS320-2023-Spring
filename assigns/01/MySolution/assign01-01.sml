use "./../MySolution/assign01-01.sml";

fun xlist_size(xs: 'a xlist): int =
case xs of
[] => 0
|
x1 :: xs => 1 + xlist_size(xs)
