type noeud = F of bool | D of string * int * int | V;;

let rec eval_var n l = 
	 match l with
	 | [] -> false
	 | a::q -> if a = n then true else eval_var n q;;
	 
	 
let rec aux ad l i =
	match ad.(i)with
	| D (n, g, d) -> aux ad l (if eval_var n l then g else d)
	| F b -> b;;

let eval ad l = aux ad l 0;;

let redirige ad v w =
	ad.(v) <- V;
	for i = 0 to (Array.length ad) - 1
	do match ad.(i) with
		| D (n, g, d) -> 
			if g = v then ad.(i) <- D (n, w, d);
			if d = v then ad.(i) <- D (n, g, w)
		| _ -> ()
	done;;

let trouve_elimination ad = 
	let v = ref (-1)
	in for i = 0 to (Array.length ad) - 1
	do match ad.(i) with
		| D (n, g, d) -> (if g = d then v := i)
		| _ -> ()
	done; !v;;
	
let trouve_isomorphisme ad =
	let n = (Array.length ad) - 1
	in let v = ref (-1, -1)
	in for i = 0 to n do 
		for j = 0 to n do (
		if i != j then
			match ad.(i) with 
			| F b1 -> ( 
				match ad.(j) with 
				| F b2 -> if b1 = b2 then v := (i, j)
				| _ -> () 
			)
			| _ -> () ;
			match ad.(i) with 
			| D (n1, g1, d1) -> (
				match ad.(j) with 
				| D (n2, g2, d2) -> if n1 = n2 && g1 = g2 && d1 == d2 then v := (i, j)
				| _ -> () 
			)
			| _ -> () 
		) done;
	done; 
	!v;;


let reduit ad = 
	let m = ref true
	in while !m do
		m := false;
		let v = trouve_elimination ad
		in if v != -1 then (
			m := true;
			let w = (match ad.(v) with | D(n, g, d) -> g)
			in redirige ad v w
		);
		let v1, v2 = trouve_isomorphisme ad
		in if v1 != -1 && v2 != -1 then (
			m := true;
			redirige ad v1 v2
		)
	done;;
	
	
let monAD = [|
D ("v0", 1, 2);
F true;
D ("v1", 3, 4); 
D ("v2", 5, 6); 
F false; 
F true;
F false 
|];;

let monAD2 = [|
D ("z1", 1, 2);
D ("z2", 3, 4);
D ("z2", 5, 6);
D ("z3", 7, 8);
D ("z3", 9, 10);
D ("z3", 11, 12);
D ("z3", 13, 14);
F true;
F false;
F true;
F false;
F true;
F false;
F false;
F false
|];;

reduit monAD2;;

monAD2;;

