lernt(otto, mathe).
lernt(paula, englisch).
lernt(rainer, mathe).
lernt(bibi, biologie).

lehrt(heinz, mathe).
lehrt(friedrich, physik).
lehrt(sleiglinde, englisch).
lehrt(max, physik).

geschwister(otto, rainer).
geschwister(paula, bibi).

lehrer(X, Y) :- lehrt(X, C), lernt(Y, C).

gleiches_fach(X, Y) :- lernt(X, C), lernt(Y, C).

gemeinLernen(X, Y) :- geschwister(X, Y); geschwister(Y, X), gleiches_fach(X, Y).