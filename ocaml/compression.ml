let occurences l =
	let t = Array.make 256 0
	in let rec aux r =
		match r with
		| [] -> ()
		| a::q -> t.(a) <- t.(a) + 1; aux q
	in aux l; t;;
	
	
let nonzero_occurences t = 
	let n = Array.length t
	in let l = ref []
	in for i = 0 to n - 1
	do if t.(n-i-1) > 0 then l := (n-i-1, t.(n-i-1))::(!l) done; Array.of_list !l;;


type tree = F of int | N of tree * tree;;

let cq a t =
	let cq = ref 0
	in let rec parcours a i =
		match a with
		| F(x) -> cq := !cq + i*t.(x)
		| N(g, d) -> parcours g (i+1) ; parcours g (i+1)
	in parcours a 0; !cq;;

let get_path n aa =
	let rec parcours n a =
		match a with 
		| F(x) -> if x = n then (true, []) else (false, [])
		| N(g, d) -> 
			let pg = parcours n g
			in if fst pg 
				then (true, 0::(snd pg))
				else let pd = parcours n d
					in if fst pd 
					then (true, 1::(snd pd))
					else (false, [])
	in snd (parcours n aa);;





let rec integers l_ = 
	let rec puiss n k = 
		if k = 0 
			then 1 
			else n*(puiss n (k-1))
	in let rec full h e =
		if h = 0 
			then F(e)
			else N(
				full (h-1) e, 
				full (h-1) (e+puiss 2 (h-1))
			)
	in let rec aux l p e =
		if p = (l + 1) then F(e)
		else N (
			full p e, 
			aux l (p+1) (e+(puiss 2 p)
			)
		)
	in aux l_ 0 0;;

integers 2;;

let rec decomp1 s tree =
	let rec aux l t =
		match t with
		| F(x) -> (x)::(aux l tree)
		| N(g, d) ->
			if (List.length l) = 0 then []
			else 
				let c, q = List.hd l, List.tl l
				in aux q (if c = 0 then g else d)
	in aux s tree;;

let a = 1;;
let c = 2;;
let b = 3;;
let d = 0;;
let tree = N(F(d),N(N(F(a),F(c)),F(b)));;

get_path c tree;;
decomp1 [1;0;0;0;1;1;0;1;0;1;0] tree;;
