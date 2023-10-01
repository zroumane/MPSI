(* pi *)
let x = asin 1. in 2. *. x;;

(* 6 *)
let a = 3 in let b = a-1 in a*b;;

(* 5 *)
let s = 2 in let c = s*s in c+1;;

(* 10 *)
let f x = x*x in f 3 + 1;;

(* 16 *)
let f x = x*x in f (3 + 1);;

(* 9 *)
let c = let d=3 in d*d;;

(* f qui renvoie (x*x)*x *)
let f x = let g y = y*x in g (g x);;
let a = f 3;;

(* 1 *)
let u = if 4>7 then 9 else 1;;

(* max *)
let max x y = if x > y then x else y;;
let v = max 5 3


(* Ex 1, abs, si le parametre est negatif > parenthese sinon operateur *)
let abs x = if x >= 0 then x else -x;;

(* Ex 2, max3 fonctionne pour plusieurs type *)
let max3 x y z = let a = if x > y then x else y in if a > z then a else z;;

(* Utilise f définit auparavant *)
let f x = x;;
let f n = if n = 0 then 1 else 10 * f (n-1);;

(* Ex 3 si on enleve les parenthese a f(n-1), on evalue f en n et on retire 1 au resulstat *)
let rec f n = if n = 0 then 1 else 10 * f (n-1);;

(* Ex 4 *)
let rec fact n = if n = 0 then 1 else n * fact (n-1);;
let rec puissance k n = if k = 0 then 1 else n * puissance (k-1) n;;

(* Ex 5 *)
let g x = x*x;;
let rec somme h n = if n < 0 then 0 else (h n) + (somme h (n-1));; (* somme h 3 = 3*3 + 2*2 + 1*1 *)

(* Ex 6 *)
let somme_cubes n = let c x = x*x*x in somme c n;;

(* Ex 7 *)
let f x = x - 2;;
let g x = x -2;;
let rec egalite f g n = if n < 0 then true else if f n = g n then egalite f g (n - 1) else false;;

(* Ex 8 *)
let somme_carre n = let m = let c x = x in (somme c n) in m*m;;
let check = egalite somme_cubes somme_carre 100;;

(* Ex 9 *)
let somme_cubes_2 n = let c x = puissance 3 x in somme c n;;

let rec len l =
	match l with
	| [] -> 0
	| _::q -> 1 + len q;;


(* Ex 10 *)
let rec somme l =
  match l with
  | [] -> 0
  | a::q -> a + somme q;;

(* Ex 11 *)
let rec compte x l =
  match l with
  | [] -> 0
  | a::q when a = x-> 1 + compte x q
  | _::q -> compte x q;;
  
let x = compte 3 [1;3;1;3;1;3];;

(* Ex 12 *)
let rec appartient x l =
  match l with
  | [] -> false
  | a::q -> if a = x then true else appartient x q;;

(* Ex 13 *)
let z x = x + 1;;
let rec images f l =
  match l with
  | [] -> []
  | a::q -> f a :: images f q;;

(* Ex 14 *)
let rec concat l g =
  match l with
  | [] ->  g
  | a::q -> a :: concat q g;;

(* Ex 15 *)
let rec addition l g =
  match (l, g) with
  | [], [] ->  []
  | a :: q, b :: p -> a + b :: addition q p;;

(* Ex 16 *)
let rec element k l =
  match l with
  | [] -> failwith "la liste est trop courte"
  | a :: q -> if k = 0 then a else element (k-1) q;;

(* Ex 17 *)
let rec minimum l =
  match l with
  | [] -> failwith "liste vide"
  | a :: q -> if q = [] then a else min a (minimum q) ;;


let rec aux l acc =
	match l with
	| [] -> acc
	| a :: q -> aux q (min a acc);;
let minimum2 l = aux l (List.hd l);;
let c = minimum2 [5;8;9;4;3];;
 


