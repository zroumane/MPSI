let rec longueur l =
match l with
| [] -> 0
| a::q -> 1 + longueur q;;

let rec insertion l x = 
match l with
| [] -> [x]
| a::q -> if x <= a then x::l else a::(insertion q x);;

let rec tri_insertion l =
match l with 
| [] -> []
| a::q -> insertion (tri_insertion q) a;;

let rec selection_n l n = 
match l with
| [] -> -1
| a :: q -> if n = 0 then a else selection_n q (n-1);;


let rec five l n =
match l with
| [] -> ([], [])
| a::q -> 
if n = 0 then ([a], q)
else let hd, tl = five q (n-1) in (a::hd, tl);;

let rec paquets_de_cinq l =
let hd, tl = five l 4
in if longueur tl = 0 then [hd]
else hd::(paquets_de_cinq tl);;


let rec medians l =
match l with
| [] -> []
| a::q -> 
	(selection_n (tri_insertion a ) (((longueur a) - 1) / 2))
	::
	(medians q);;

let partage p l =
let rec aux m =
	match m with
	| [] -> [], []
	| a::q ->
	if p < a 
	then [], m
	else 
		let l1, l2 = aux q
		in a::l1, l2
in let l1, l2 = aux (tri_insertion l)
in l1, l2, (longueur l1), (longueur l2);;

let rec selection l k =
let n = longueur l
in if n <= 5
	then selection_n (tri_insertion l) k
	else
		let p5 = paquets_de_cinq l
		in let m = medians p5
		in let pivot = selection m (((n+4)/5)/2)
		in let l1, l2, n1, n2 = partage pivot l
		in selection (if k < n1 then l1 else l2) k
	;;





select [1;2;3;4;5;6;7;8;9;10] 4;;



