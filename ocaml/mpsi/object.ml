type candidat = {
	sommet: int;
	parent: int;
	mutable distance: int
};;

let a = {sommet = 1; parent = 1; distance =1};;
a;;
a.distance <- 8;;
a;;

let rec mem1 x q =
	match q with
	| [] -> false
	| a::l -> if fst a = x then true else mem1 x l;;
	
	
let rec assoc x q =
	match q with
	| [] -> 0
	| a::l -> if fst a = x then snd a else assoc x l;;
	

let n = 10;;

let rec hachage_liste w q =
	match q with
	| [] -> 0
	| a::l -> (((fst a) + (snd a)*n) + (n*n)*(hachage_liste w l)) mod w;;

type ('a, 'b) table_hachage = {
	hache: 'a -> int;
	donnees: ('a * 'b) list array;
	largeur: int
};;

let creer_table h w = {hache = h w; donnees = Array.make w []; largeur = w};;

let recherche t k = let i = t.hache k in mem1 k t.donnees.(i);;

let element t k = let i = t.hache k in assoc k t.donnees.(i);;

let ajout t k e = let i = t.hache k in 
	if recherche t k then () else t.donnees.(i) <- (k, e)::(t.donnees.(i));;

let rec sup l k = match l with | [] -> [] | a::q -> if (fst a) = k then (sup q k) else a::(sup q k);;

let suppression t k = let i = (t.hache k) in t.donnees.(i) <- sup (t.donnees.(i)) k ;;

let c = creer_table hachage_liste 7;;
for i = 0 to 10 do (ajout c [(1+i,2+i*2);(3+i*3,4+i*4);(5+i*5,6+i*6)] (i+100)) done;;
c;;

let i = 3;;
recherche c [(1+i,2+i*2);(3+i*3,4+i*4);(5+i*5,6+i*6)];;
element c [(1+i,2+i*2);(3+i*3,4+i*4);(5+i*5,6+i*6)];;
suppression c [(1+i,2+i*2);(3+i*3,4+i*4);(5+i*5,6+i*6)];;
c;;


type ('a, 'b) table_dyn = {
	hache: int -> 'a -> int;
	mutable taille: int;
	mutable donnees: ('a * 'b) list array;
	mutable largeur: int
};;

let creer_table_dyn h = {hache=h; taille=0; donnees= Array.make 1 []; largeur=1};;

creer_table_dyn hachage_liste;;

let rearrange_dyn t w2 = 
	let w = t.largeur in 
	for i = 0 to w do t.h w2 t.donnees done; t.largeur <- w2;


