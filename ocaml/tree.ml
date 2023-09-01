type arbre =
  | Vide
  | Noeud of (arbre * int * arbre);;

let rec taille a = match a with
| Vide -> 0
| Noeud (g, x, d) -> 1 + (taille g) + (taille d);;


let rec hauteur a = match a with
| Vide -> -1
| Noeud (g, x, d) -> 1 + (max (hauteur g) (hauteur d));;

let rec appartient a x = match a with
| Vide -> false
| Noeud (g, n, d) -> 
	if n = x 
	then true 
	else (appartient g x) || (appartient d x);;

let rec somme a = 
match a with
| Vide -> 0
| Noeud (g, x, d) -> x + (somme g) + (somme d);;



let a = Noeud (
	Noeud (
		Vide, 
		4, 
		Vide), 
	3, 
	Noeud (
		Noeud (
			Vide, 
			4, 
			Vide),
		2,
		Noeud (
			Vide, 
			1, 
			Vide)
		)
);;

taille a;;
hauteur a;;
appartient a 2;;
somme a;;


let a_r = Noeud (
	Noeud (
		Noeud (
		    Vide, 
		    1, 
		    Vide
		), 
		2, 
		Noeud (
		    Vide, 
		    3, 
		    Vide
		)
	), 
	5, 
	Noeud (
		Noeud (
		    Vide, 
		    8, 
		    Vide
		),
		12,
		Vide
	)
);;


let rec appartient_r x a =
match a with
| Vide -> false
| Noeud (g, y, d) -> 
    if x = y then true
    else if x > y then (appartient_r x d) else (appartient_r x g);;
    
    
let rec insere_r x a =
match a with
| Vide -> Noeud (Vide, x, Vide)
| Noeud (g, y, d) -> 
    if x > y then Noeud (g, y, insere_r x d) else Noeud (insere_r x g, y, d);;
    
let rec retire_ed a =
match a with
| Vide -> (-1, Vide)
| Noeud (g, y, d) -> 
    let x, ed = retire_ed d
    in if x = -1
        then (y, g)
        else (x, Noeud (g, y, ed));;

let rec supprime_r x a =
match a with
| Vide -> Vide
| Noeud (g, y, d) when x < y -> Noeud (supprime_r x g, y, d)
| Noeud (g, y, d) when x > y -> Noeud (g, y, supprime_r x d)
| Noeud (g, y, d) -> let x, gbis = (retire_ed g) in Noeud (gbis, x, d);;

a_r;;
supprime_r 12 a_r;;   
    
    
    
    
    
