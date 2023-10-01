print_int 3;;
print_string "hello";;
print_newline ();;

(* Exercice 1*)

let produit x y = 
	let z = x*y 
	in print_int x; 
	print_string "x";
	print_int y;
	print_string "=";
	print_int z;
	z;;


(* Exercice 2*)

let rec fact n =
	print_string "Debut";
	print_int n;
	let a = if n = 0 then 1 else fact (n-1) * n in
	print_string "Fin";
	print_int n;
	a;;
	
ignore (fact 2); print_newline (); fact 3;;


(* Exercice 3*)

for i = 0 to 9 do print_int i done;;


(* Exercice 4*)

for i = 0 to 9 do print_int i; print_int i done;;


(* Exercice 5*)

let rec table n = for i = 1 to 10 do ignore (produit n i) ; print_string ("; ") done;;


(* Exercice 6*)

let tables () = for i = 0 to 10 do (table i) ; print_newline () done;;

tables ();;

let a = Array.make 10 0;;
a;;
Array.length a;;
a.(3) <- 2;;
a.(3);;

(* Exercice 7*)

let t = Array.make 100 0;;
let l = Array.length t;;
for i = 0 to (l - 1); do t.(i) <- (l - i) done;;
t;;


(* Exercice 8*)

let somme t1 t2 = 
let l = (Array.length t1)
in let t = (Array.make l 0) 
in for i = 0 to (l-1) do t.(i) <- (t1.(i) + t2.(i)) done; t;;

somme (Array.make 30 3) (Array.make 30 2);;


(* Exercice 9*)

let concat t1 t2 = 
let l1 = (Array.length t1) 
in let l2 = (Array.length t2)
in let t = (Array.make (l1+l2) 0) 
in for i = 0 to (l1+l2-1) do  
if i < l1 then t.(i) <- t1.(i)
else t.(i) <- t2.(i-l1)
done; t;;

concat [|1;2;3;4|] [|4;5;6|];;


(* Exercice 10*)

let fact_imperative n =
let p = ref 1
in for i = 1 to n do p := (!p*i) done; p;;

fact_imperative 5;;


(* Conversion liste tableau*)

let t_to_l t =
let l = ref [] in let n = (Array.length t) - 1
in for i = 0 to n do l := (t.(n - i))::(!l) done; !l;;

t_to_l [|1;2;3;4|];;

let rec t_to_l_v2 t k = if k = 0 then [] else (t.(k-1))::(t_to_l_v2 t (k-1));;

t_to_l_v2 [|1;2;3;4|] 4;;


let rec l_to_t l =
let g = ref l in
let n = List.length l in
let t = Array.make n 0 in
for i = 0 to n - 1 do
	match (!g) with 
	| a::q -> t.(i) <- a ; g := q
done; t;;

l_to_t [1;2;3;4];;







