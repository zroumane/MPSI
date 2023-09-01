
(* FEUILLE "RENCONTRE AVEC OCAML" *)

(* Ex 4*)
let rec fact n =  
        if n=0 then 1 
        else n * fact (n-1);;

let rec puissance k n =
        if k=0 then 1
        else n *  puissance (k-1) n;;

(* Ex 5*)
let rec somme f n =
        if n=0 then f 0
        else f n + somme f (n-1);;

(* Ex 6*)
let rec somme_cubes n =
        let cube x = x*x*x in somme cube n;;

(* Ex 7*)
let rec egalite f g n =
        if n=0 then f 0 = g 0
        else f n = g n && egalite f g (n-1);;

(* Ex 8*)
let rec somme_entiers n=
        if n=0 then 0 else n + somme_entiers (n-1) ;;

let carre_somme n= 
        let s=somme_entiers n in
        s*s;;

egalite somme_cubes carre_somme 100;;


(* Ex 9*)

let somme_cubes = somme (puissance 3);;


(* Ex 10*)
let rec somme l=
        match l with
        |[]->0
        |a::q-> a + somme q;;

(* Ex 11*)
let rec compte x l =
        match l with
        |[]-> 0
        |a::q when a=x -> 1 + compte x q
        |a::q -> compte x q;;

(* Ex 12*)
let rec appartient x l =
        match l with 
        | []-> false
        | a::q -> a=x || appartient x q;;


(* Ex 13*)
let rec images f l=
        match l with 
        |[]-> []
        |a::q-> f a :: images f q;;


(* Ex 14*)
let rec concat l g = 
        match l with
        | [] -> g
        | a::q -> a:: concat l g;;


(* Ex 15*)
let rec addition l g =
        match (l,g) with
        | [],[]-> []
        | a::q , b::r -> (a+b):: addition q r
        | _ -> failwith "listes de longueurs différentes" ;;

(* Ex 16*)
let rec element k l =
        match l with
        | [] -> failwith "liste trop courte"
        | a::q when k=0 -> a
        | a::q -> element (k-1) q;;

(* Ex 17*)
let rec minimum l =
        match l with 
        | [] -> failwith "minimum liste vide"
        | [a]-> a
        | a::q -> min a (minimum q);;

(* DEUXIEME SEANCE *)

(* 4 versions de factorielle *)
(* version 1 : multiplications "en remontant" de 1 à n *)
let rec fact n=
        if n=0 then 1 
        else n * fact(n-1);;
(* version 2 : mutliplications "en remontant" de n à 1 *)
let rec aux n k = (* renvoie k*(k+1)*...*n *)
        if k=n then n 
        else k*aux n (k+1);;
let fact n=aux n 1;;
(* version 3 : multiplications "en descendant" de 1 à n *)
let rec aux n k acc =  (* renvoie acc*k*(k+1)*..*n  *)
        if k=n then acc*n  
        else aux n (k+1) (acc*k);;
let fact n= aux n 1 1;;
(* version 4 : multiplications "en descandant" de n à 1 *)
let rec aux n acc=  (* renvoie acc*n! *)
        if n=0 then acc
        else aux (n-1) (acc*n);;
let fact n= aux n 1;;

(* somme d'une liste : 2 versions *)
(* v1 additions en partant de la fin de la liste, "en remontant" *)
let rec somme l=
        match l with
        | []-> 0
        | a::q -> a+somme q;;

(* v1 additions en partant du debut de la liste, "en descendant" *)
let rec aux l acc= (* renvoie acc + la somme des elements de l *)
        match l with
        | []-> acc
        | a::q -> aux q (acc+a);;
let somme l= aux l 0;;

(* liste [1;...;n]  : 2 versions *)
(* version 1 : construction "en remontant"*)
let rec aux k n = (* renvoie la liste [k;k+1;...;n] *)
        if k=n then [n]
        else k::aux (k+1) n;;
let range n=aux 1 n;;

(* version 2 : construction "en descendant" *)
let rec aux k n acc = (* renvoie la liste 1::2::...::k::acc *)
        if k=0 then acc
        else aux (k-1) n (k::acc);;
let range n = aux n n [];;

(* liste [n;...;1] : 2 versions *)
(* version 1 :  construction "en remontant" *)
let rec dec_range n =
        if n=0 then []
        else n::dec_range (n-1);;
(* version 2 : construction "en descendant" *)
let rec aux n k acc = (* renvoie n::(n-1)::...::k::acc *)
        if n=k then n::acc
        else aux n (k+1) (k::acc);;
let dec_range n= aux n 1 [];;

(* premiere occurrence : 2 versions *)
(* utilisons le type option pour dire proprement None si x n'est pas dans la liste *)
(* version 1 : le résultat est incrémenté "en remontant" *)
let rec fst_ind x l =
        match l with
        | [] -> None
        | a::q when a=x-> Some 0
        | _::q -> match fst_ind x q with
                  | None -> None
                  | Some i -> Some (i+1);;
(* version 2 : le resultat est incrémenté "en descendant" *)
let rec aux x l k = (* renvoie k + le premier indice de x dans l, ou None s'il n'y en a pas. *)
        match l with
        | [] -> None
        | a::q when a=x -> Some k
        | _::q -> aux x q (k+1);;
let fst_ind x l = aux x l 0

(* dernier indice *)
(* version 1 : le résultat est incrémenté "en remontant" *)
let rec lst_ind x l =
        match l with
        |[]-> None
        | a::q -> match lst_ind x q with
                  | Some i -> Some (i+1)
                  | None -> if a=x then Some 0 else None;;

(* version 2 : l'indice k est incrémenté et calculé "en descendant" *)
let rec aux x l k res = (* renvoie k + le dernier indice de x dans l, ou  res s'il n'y en a pas *)
        match l with
        |[] -> res
        | a::q when a=x -> aux x q (k+1) (Some k)
        | _::q -> aux x q (k+1) res;;
let lst_ind x l = aux x l 0 None;;

(* premier et dernier indice *)
(* version 1 :  calculs faits "en remontant", on "fusionne" les deux mécanismes utilisés ci-dessus *)
let rec fst_lst_ind x l=
        match l with 
        |[]-> None
        |a::q -> match fst_lst_ind x q with
                 | None -> if a=x then Some (0,0) else None
                 | Some(u,v) -> if a=x then Some(0,v+1) else Some(u+1,v+1);;

(* version 2 : calculs "en descendant". Là ça commence à être difficile de spécifier précisement
 * la fonction auxilliaire, et donc de se convaincre que la fonction est correcte *)
let rec aux x l k p d= 
        match l with
        | [] -> p,d
        | a::q when a<>x -> aux x q (k+1) p d
        | a::q (*a=x*) -> let np=if p= -1 then k else p in(* np : nouveau p*)
                          aux x q (k+1) np k;;
let fst_lst_ind x l = aux x l (-1) (-1) ;;

(* TROISIEME SEANCE *)

(* miroir : là on est obligé de construire le résultat "en descendant" *)
let rec aux l acc= (* renvoie le miroir de l, concaténé avec acc *)
        match l with
        |[] -> acc
        |a::q -> aux q (a::acc);;
let miroir l = aux l [];;

(* decoupe : là on peut se passer de fonction auxilliaire *)
let rec decoupe l k =
        if k=0 then [],l
        else
             let a::q = l in 
             let u,v=decoupe q (k-1) in
             a::u,v;;

(* rotation : d'une maniere ou d'une autre il faut découper et concaténer *)
let rotation l k= let u,v= decoupe l k in v@u;;


(* concat *)
let rec concat g = 
        match g with
        |[] -> []
        |l::q -> l @ concat q;;

(* A faire : *)
(* Insertion dans une liste triée *)
(* Tri par insertion *)
(* Retrait du maximum *)
(* Tri par selection *)





