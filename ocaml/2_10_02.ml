let rec build n = 
	if n = 0 then []
	else n :: build (n-1);;
build 10;;

let rec build2 n k = 
	if n = k then [k]
	else k :: build2 n (k + 1);;
build2 10 1;;

let rec build3 n acc l = 
	if n + 1 = acc then l
	else 	build3 n (acc + 1) (acc :: l);;
build3 10 1 [] ;;

let rec build4 n l = 
	if n = 0 then l
	else 	build4 (n - 1) (n :: l);;
build4 10 [] ;;

(* Renvoie (le prenier indice de x ) + k *)
let rec fst_ind_1_aux x l k =
  match l with
  | [] -> failwith "l ne contient pas x"
  | a::q when x = a -> k
  | a::q -> fst_ind_1_aux x q (k+1) ;;

let fst_ind_1 x l = fst_ind_1_aux x l 0;;
fst_ind_1 4 [1;2;3;4;5;6];;

(* Renvoie (le prenier indice de x ) + k *)
let rec fst_ind_2 x l =
  match l with
  | [] -> failwith "l ne contient pas x"
  | a::q when x = a -> 0
  | a::q -> (fst_ind_2 x q) + 1 ;;
fst_ind_2 4 [1;2;3;4;5;6];;


let rec lst_ind_1_aux x l k =
  match l with
  | [] -> (-1)
  | a::q when a = x -> max k (lst_ind_1_aux x q (k+1))
  | a::q -> lst_ind_1_aux x q (k+1);;

let lst_ind_1 x l = let r = lst_ind_1_aux x l (-1) in 
    if r = (-1) then failwith "x n'est pas dans la liste" else r + 1;;
lst_ind_1 4 [3;2;4;2;2;1];;

let rec lst_ind_2_aux x l k =
  match l with
  | [] -> None
  | a::q  -> let r = lst_ind_2_aux x q (k+1) in
  	match r with 
  	| None -> if a = x then (Some a) else r
  	| _ -> r;;
let lst_ind_2 x l = lst_ind_2_aux x l 0 ;;
lst_ind_2 4 [3;2;4;2;2;1];;

let rec lst_ind_3_aux x l k acc =
  match l with
  | [] -> acc 
  | a::q when a = x -> lst_ind_3_aux x q (k+1) k
  | a::q  -> lst_ind_3_aux x q (k+1) acc
let lst_ind_3 x l = lst_ind_3_aux x l 0 0 ;;
lst_ind_3 4 [3;2;4;2;2;1];;


let rec fst_lst_ind_1_aux x l i j =
  match l with
  | [] -> (i, 0)
  | a::q when a = x && i = -1 -> fst_lst_ind_1_aux x l (j) (j)
  | a::q when a = x -> (i, max j (snd (fst_lst_ind_1_aux x q (i) (j+1))))
  | a::q -> fst_lst_ind_1_aux x q (i) (j+1);;

let fst_lst_ind_1 x l = 
  let r = fst_lst_ind_1_aux x l (-1) 0 in 
    if r = (-1, 0) then failwith "x n'est pas dans la liste" else r;;
fst_lst_ind_1 3 [1;1;3;2];;


let rec miroir_aux l g =
	match l with
	| a::q -> miroir_aux q (a :: g)
	| [] -> g;;
let miroir l = miroir_aux l [];;
miroir[1;2;3;4];;	


let rec decoupe k l=
	match l with
	| a::q when k = 0 -> ([], a::q)
	| a::q -> (a :: (fst (decoupe (k-1) q)), (snd (decoupe (k-1) q)))
	| [] -> failwith "k trop grand";;
decoupe 3 [1;2;3;4;5;6];;


let rec rotation_aux k l g =
	match l with
	| a::q when k = 0 -> l @ (miroir g)
	| a::q -> rotation_aux (k-1) (q) (a::g)
	| [] -> failwith "k trop grand";;
let rotation k l = rotation_aux k l [];;
rotation 2 [1;2;3;4;5;6];;


let rec concat g =
	match g with 
	| a::q -> a @ (concat q) 
	| [] -> [];;
concat [[1;2];[3;4];[5]];;


let rec concat_2 g =
	match g with 
	| [] -> []
	| a::q -> 
		match a with 
			| n::k -> n :: (concat_2 (k::q))
	 		| [] -> concat_2 q;;
concat_2 [[1;2];[3;4];[5]];;



