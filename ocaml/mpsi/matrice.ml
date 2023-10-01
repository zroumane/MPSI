(* Produit matricielle naif *)

let rec produit_scalaire l1 l2 =
match l1, l2 with
	| [], [] -> 0
	| a::q, b::p -> a*b + (produit_scalaire q p);;

	
let rec decapitation m =
match m with
	(* ajout *)
	| [] -> [], [] 
	| (a::q)::p -> let tetes, queues = (decapitation p) in
	(a::tetes, q::queues);;

	
let rec transpose m = 
if List.hd m = [] then []
else let tetes, queues = (decapitation m) in tetes::(transpose queues);;

let rec aux l m2 =
match m2 with
	| [] -> []
	| a::q -> (produit_scalaire l a)::(aux l q);;

	
let rec produit_lignes m1 m2 = 
match m1 with
	| [] -> []
	| l::q -> (aux l m2)::(produit_lignes q m2);;


let pm a b = produit_lignes a (transpose b);;


(* Strassen *)

let rec zero n = if n = 0 then [] else 0::(zero (n-1));;

let rec parite_colone m =
match m with
	| [] -> []
	| a::q -> (a @ [0]) :: (parite_colone q);;

let rec parite m = 
match List.length m with
	| n when (n mod 2) = 0 -> m
	| n -> (parite_colone m) @ [zero (n+1)];;


let rec decoupe_ligne k m =
match m with
| a::q when k = 0 -> ([], a::q)
| a::q -> let l1, l2 = decoupe_ligne (k-1) q
	in (a::l1, l2);;

let rec aux k m =
match m with
| a::q -> (decoupe_ligne k a)::(aux k q)
| [] -> [];;

let rec decoupe_colone k l =
match l with
	| [] -> [], [], [], []
	| a::q -> let l1, l2, l3, l4 = decoupe_colone (k-1) q
	in if k < 1 
		then ([], [], (fst a)::l3, (snd a)::l4)
		else ((fst a)::l1, (snd a)::l2, l3, l4);;

let decoupe m = let k = (List.length m)/2 in decoupe_colone k (aux k m);;

let rec assemble_ligne l m = 
match l, m with
| [], [] -> []
| a::q, b::p -> (a @ b)::(assemble_ligne q p);; 

let rec assemble l1 l2 l3 l4 = (assemble_ligne l1 l2) @ (assemble_ligne l3 l4);;

let rec operate_lignes k m1 m2 =
match m1, m2 with
	| a::q, b::p -> (if k = 0 then a-b else a+b) :: (operate_lignes k q p)
	| [], [] -> [];;	
	
let rec op k m1 m2 =
match m1, m2 with
	| a::q, b::p -> (operate_lignes k a b) :: (op k q p)
	| [], [] -> [];;


let rec strassen a b =
    if List.length a = 1 then 
    let [[va]] = a in let [[vb]] = b in [[va*vb]] else
	let a_, b_ = (parite a, parite b)
	in let a1, a2, a3, a4 = decoupe a_
	in let b1, b2, b3, b4 = decoupe b_
	in let c1 = op 1 
	    (op 0 
	        (strassen a4 (op 0 b3 b1)) 
	        (strassen (op 1 a1 a2) b4)
	    )
	    (op 1
	      	(strassen (op 0 a2 a4) (op 1 b3 b4)) 
	        (strassen (op 1 a1 a4) (op 1 b1 b4))  
	    )
	in let c2 = op 1 
	    (strassen (op 1 a1 a2) b4)
	    (strassen a1 (op 0 b2 b4))
	in let c3 = op 1
	    (strassen a4 (op 0 b3 b1))
	    (strassen (op 1 a3 a4) b1)
	in let c4 = op 0
	    (op 1 
	        (strassen (op 0 a3 a1) (op 1 b1 b2)) 
	        (strassen a1 (op 0 b2 b4))
	    )
	    (op 1 
	        (strassen (op 1 a3 a4) b1) 
	        (strassen (op 1 a1 a4) (op 1 b1 b4))
	    )
	in assemble c1 c2 c3 c4;;

(*strassen [[3;4;5]; [7;8;9]; [7;8;9]] [[1;2;5]; [5;6;6]; [7;8;9]];;*)

strassen [[1;2];[3;4]] [[5;6];[7;8]];;


