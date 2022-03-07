lernt(otto, mathe).
lernt(paula, englisch).
lernt(rainer, mathe).
lernt(bibi, biologie).

lehrt(heinz, mathe).
lehrt(friedrich, physik).
lehrt(sleiglinde, englisch).

lehrer(X, Y) :- lehrt(X, C), lernt(Y, C).

gleiches_fach(X, Y) :- lernt(X, C), lernt(Y, C).
