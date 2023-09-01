let nuage n graine max  =
	Random.init graine;
	let l = ref []
	in for i = 1 to n do  l := (Random.float max, Random.float max)::(!l) done; 
	!l;;

let rec decoupe l n =
	match l with
	| a :: q -> if n = 0 then ([], a::q) 
		else let l1, l2 = decoupe q (n-1) in
		(a :: l1, l2);;

let rec fusion l1 l2 cle =
	match l1, l2 with 
	| [], _ -> l2
	| _, [] -> l1
	| a :: q, b :: p ->
		if (cle a) > (cle b) 
			then b :: (fusion (a::q) p cle) 
			else a :: (fusion q (b::p) cle);;

let rec tri_fusion l cle =
	if List.length l = 1 then l
	else 
		let l1, l2 = decoupe l ((List.length l)/2) in 
		let l1t = tri_fusion l1 cle in
		let l2t = tri_fusion l2 cle in
		fusion l1t l2t cle;;

let distance p1 p2 = (((fst p2) -. (fst p1))**2.0 +. ((snd p2) -. (snd p1))**2.0)**0.5;;

let cle_x p = fst p;;
let cle_y p = snd p;;

let rec bande d x l = 
	match l with
	| [] -> []
	| a::q -> if (fst a) >= x-.d && (fst a) <= x+.d then a::(bande d x q) else (bande d x q)
	;;


let rec min_d a q =
	if List.length q = 1 then a, (List.hd q), (distance a (List.hd q))
	else (
		let p = List.hd q
		in let d = distance a p 
		in let a_, p_, d_ = (min_d p (List.tl q))
		in if d < d_ then a, p, d else a_, p_, d_
	);;

let rec balayage l =
	if (List.length l = 1) then (match l with | a::b::q -> a, b, (distance a b))
	else (
		match l with 
		| a::a1::a2::a3::a4::a5::a6::b::c::q -> 
			let p11, p12, d1 = (min_d a [a1;a2;a3;a4;a5;a6])
			in let p21, p22, d2 = balayage (a1::a2::a3::a4::a5::a6::b::c::q)
			in if d1 < d2 then p11, p12, d1 else p21, p22, d2
		| a :: q -> min_d a q
	)
;;



let rec plus_proches l =
	let lt = tri_fusion l cle_x
	in let n = (List.length lt)
	in if n = 2 then 
		(match lt with | a::b::q -> (a, b, distance a b))
	else
	if n = 1 then
		((0.0,0.0), (0.0,0.0), max_float)
	else (
		let l1, l2 = decoupe lt (n/2)
		in let p11, p12, d1 = plus_proches l1
		in let p21, p22, d2 = plus_proches l2
		in let d = min d1 d2
		in let best = if d1 = d then (p11, p12, d1) else (p21, p22, d2)
		in let x = fst (List.hd l2)
		in let b = bande d x lt
		in if List.length b < 2 then best else (
			let p31, p32, d3 = balayage (tri_fusion b cle_y)
			in if d3 < d then (p31, p32, d3) else best
		)
	);;

plus_proches (nuage 10 1 100.);;
