mensch(aristoteles).
mensch(sokrates).
tier(schlange).
gott(zeus).
gott(apollo).

sterblich(X) :- (mensch(X) ; tier(X)), not(gott(X)).

