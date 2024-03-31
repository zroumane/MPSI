let et = -1;;
let pl = -2;;
let pt = -3;;
let po = -4;;
let pf = -5;;

let expr_of_str s=
  let expr=Array.make (String.length s) 0 in
  for i=0 to String.length s -1 do
    expr.(i)<- int_of_char s.[i]-int_of_char 'a';
    if s.[i]='+' then expr.(i)<-pl;
    if s.[i]='.' then expr.(i)<-pt;
    if s.[i]='*' then expr.(i)<-et;
    if s.[i]='(' then expr.(i)<-po;
    if s.[i]=')' then expr.(i)<-pf;
  done;
  expr;; 


let est_symbole x = x < 0 && x > -6;;

let cesure expr debut fin =
  if fin - debut < 2 
  then -1
  else 
    (
      let i = ref (-1)
      in for j = (debut + 1) to (fin - 1)
      do
        if !i = -1 && (expr.(j) = pl || expr.(j) = pt)
        then (
          let npo = ref 0
          in let npf = ref 0
          in for k = debut + 1 to j - 1
          do (
            if expr.(k) = po then incr npo;
            if expr.(k) = pf then incr npf;
          ) done;
          if !npo = !npf then i := j
        )
      done;
      !i
    );;


let rec est_rationelle expr debut fin =
  if debut = fin && not (est_symbole expr.(debut)) then true
  else if expr.(fin) = et then est_rationelle expr (debut + 1) (fin - 2)
  else let c = cesure expr debut fin
    in if c = -1 then (
      let car = ref 0
      in for i = debut to fin
      do if not (est_symbole expr.(i)) then incr car done;
      !car = 1 
    ) else (est_rationelle expr (debut + 1) (c - 1)) && (est_rationelle expr (c + 1) (fin-1));;


type arbre=
  |Feuille of int
  |Etoile of arbre
  |Plus of (arbre*arbre)
  |Point of (arbre*arbre);;

let rec expression_vers_arbre expr debut fin=
  let i=cesure expr debut fin in
  if i= -1 then
     (*lettre*)
    if debut=fin then Feuille (expr.(debut))
    else (*etoile*)
      Etoile ( expression_vers_arbre  
                 expr (debut+1)(fin-2)
             )
  else
    (* plus ou point *)
    let g=expression_vers_arbre
        expr (debut+1) (i-1) in
    let d=expression_vers_arbre
        expr (i+1) (fin-1) in
    if expr.(i)=pt 
    then Point(g,d)
    else Plus(g,d);;


let rec contient_epsilon arbre=
  match arbre with
  | Feuille _ -> false
  | Etoile _ -> true
  | Point (g,d)-> contient_epsilon g && contient_epsilon d
  | Plus(g,d)->  contient_epsilon g || contient_epsilon d;;




let appartient mot i f p =
  let l = Array.length mot
  in let a = ref true
  in if not i.(mot.(0)) then a := false;
  if not f.(mot.(l-1)) then a := false;
  for j = 0 to l-2
  do if not p.(mot.(j+1)).(mot.(j)) then a := false done;
  !a;;


let rec calcul_I arbre i =
  match arbre with
  | Feuille n -> i.(n) <- true
  | Etoile a -> calcul_I a i
  | Plus (a1, a2) -> calcul_I a1 i ; calcul_I a2 i
  | Point (a1, a2) -> calcul_I a1 i ; if contient_epsilon a1 then calcul_I a2 i
;;

let rec calcul_F arbre f =
  match arbre with
  | Feuille n -> f.(n) <- true
  | Etoile a -> calcul_F a f
  | Plus (a1, a2) -> calcul_F a1 f ; calcul_F a2 f
  | Point (a1, a2) -> calcul_F a2 f ; if contient_epsilon a2 then calcul_F a1 f
;;

let ajout_couple produit t1 t2 =
  let n = Array.length t1
  in for i = 0 to n - 1
  do for j = 0 to n - 1
    do produit.(i).(j) <- t1.(i) && t2.(j) done;
  done;;


let rec calcul_P arbre p =
  let n = Array.length p.(0)
  in match arbre with
  | Feuille n -> ()
  | Etoile a -> calcul_P a p ;
      let i = Array.make n false
      in let f = Array.make n false
      in calcul_I a i ; calcul_F a f ; ajout_couple p i f
  | Plus (a1, a2) -> calcul_P a1 p ; calcul_P a2 p
  | Point (a1, a2) -> calcul_P a1 p ; calcul_P a2 p ;
      let f1 = Array.make n false
      in let i2 = Array.make n false
      in calcul_F a1 f1 ; calcul_I a2 i2; ajout_couple p f1 i2
;;

let lettres_distinctes expr n =
  let b = ref true
  in let s = Array.make n false
  in for i = 0 to (Array.length expr) - 1
  do if not (est_symbole expr.(i)) then (
      if s.(expr.(i)) then b := false else s.(expr.(i)) <- true 
    ) done; !b;;

(* s = {a, b, c}*)

let expr1 = expr_of_str "(((a.c))*+b)";;
let expr2 = expr_of_str "((b)*.(a+((a)*.b)))";;

let a1=expression_vers_arbre expr1 0 11 ;;
let a2=expression_vers_arbre expr2 0 18;; 

est_rationelle expr1 0 11;;
est_rationelle expr2 0 18;;

contient_epsilon a1;;
contient_epsilon a2;; 

let i_a1 = (Array.make 3 false) in calcul_I a1 i_a1; i_a1;;
let f_a1 = (Array.make 3 false) in calcul_F a1 f_a1; f_a1;;

let i_a2 = (Array.make 3 false) in calcul_I a2 i_a2; i_a2;;
let f_a2 = (Array.make 3 false) in calcul_F a2 f_a2; f_a2;;

let p_a1 = (Array.make_matrix 3 3 false) in calcul_P a1 p_a1; p_a1;;
let p_a2 = (Array.make_matrix 3 3 false) in calcul_P a2 p_a2; p_a2;;