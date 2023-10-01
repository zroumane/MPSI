(* A faire : *)
(* Insertion dans une liste triée *)
let rec insere_tri x l =
match l with
| [] -> [x]
| a::q -> if x < a then x :: l else a :: (insere_tri x q);;

(* Tri par insertion *)

let rec tri_insertion l =
match l with
| [] -> []
| a :: q -> insere_tri a (tri_insertion q);;

(* Retrait du maximum *)

let rec retire_max l =
match l with
| [] -> ([], 0)
| a :: q -> let m = retire_max q in
if (snd m) > a then (a :: (fst m), snd m) else (q, a);;

(* Tri par selection *)

let rec tri_selection l = 
match l with
| [] -> []
| _ -> let m = retire_max l
in (snd m) :: (tri_selection (fst m));;


(* Tri par fusion *)

let rec decoupe l n =
	match l with
	| a :: q -> if n = 0 then ([], a::q) 
		else let l1, l2 = decoupe q (n-1) in
		(a :: l1, l2);;

let rec fusion l1 l2 =
	match l1, l2 with 
	| [], _ -> l2
	| _, [] -> l1
	| a :: q, b :: p ->
		if a > b 
			then b :: (fusion (a::q) p) 
			else a :: (fusion q (b::p));;

let rec tri_fusion l =
	if List.length l = 1 then l
	else 
		let l1, l2 = decoupe l ((List.length l)/2) in 
		let l1t = tri_fusion l1 in
		let l2t = tri_fusion l2 in
		fusion l1t l2t;;


tri_fusion [7;5;2;9;6;3;1];;












