liebt(werner, birgit) :- liebt(karl, rita).

liebt(fritz, karin) :- liebt(herbert, birgit).
    
liebt(herbert, claudia) :- liebt(werner, birgit), not(liebt(fritz, birgit)), not(liebt(herbert, birgit)), not(liebt(karl, birgit)).

liebt(karl, birgit) :-not(liebt(fritz, karin)).
    
liebt(karl, rita).

liebt(fritz, X) :- not(liebt(werner, X)), not(liebt(herbert, X)), not(liebt(karl, X)).