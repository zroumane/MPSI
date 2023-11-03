let dupliquer_matrice g =
  let n = Array.length g
  in let g_ = Array.make n [||]
  in for i = 0 to n-1 do 
    g_.(i) <- Array.make n false;
    for j = 0 to n-1 do 
      g_.(i).(j) <- g.(i).(j)
    done;
  done; g_;;

let verifie g c = 
  let n = (Array.length c) - 1 
  in let check = ref true
  in for i = 0 to n
  do
    for j = 0 to n do
      if i != j && c.(i) != -1 && c.(i) = c.(j)
      then check := false done;
    if c.(i) != -1 && g.(i).(c.(i)) = false then check := false
  done; !check;; 


let cardinal c = 
  let card = ref 0
  in for i = 0 to (Array.length c) - 1
  do if c.(i) != -1 then card := !card + 1 done; 
  !card ;;


let compte g n i j =
  let s = ref 0
  in for k = 0 to n - 1
  do 
    if g.(i).(k) then s := !s + 1;
    if g.(k).(j) then s := !s + 1
  done; !s;; 

let arrete_min g a = 
  let n = Array.length g
  in let s = ref (compte g n a.(0) a.(1))
  in let r = ref 0
  in for i = 0 to n - 1
  do 
    for j = 0 to n - 1 
    do 
      if g.(i).(j)
      then (
        let d = (compte g n i j)
        in if d < !s || !s = 0 then (s := d; a.(0) <- i; a.(1) <- j)
      )
      else r := !r + 1
    done;
  done;
  if !r = n*n then false else true ;; 


let supprimer g a =
  for k = 0 to (Array.length g) - 1
  do g.(a.(0)).(k) <- false; g.(k).(a.(1)) <- false done;; 
  

let algo_approche g =
  let n = Array.length g 
  in let g_ = dupliquer_matrice g 
  in let c = Array.make n (-1)
  in let a = [|0; 0|]
  in while arrete_min g_ a 
  do 
    supprimer g_ a; 
    c.(a.(0)) <- a.(1) 
  done;
  c;;

let une_arrete g a =
  let n = Array.length g
  in let s = ref 0
  in for i = 0 to n-1
  do 
    for j = 0 to n-1
    do 
      if g.(i).(j) then (a.(0) <- i;a.(1) <- j)
      else s := !s + 1
    done;
  done;
  if !s = n*n then false else true;;



let rec meilleur_couplage g =
  let a = [|0;0|]
  in let c = ref (Array.make (Array.length g) (-1))
  in if une_arrete g a 
  then (
    let g_ = dupliquer_matrice g
    in let c1 = algo_approche g_ 
    in let nc1 = cardinal c1
    in g_.(a.(0)).(a.(1)) <- false ;
    let c2 = meilleur_couplage g_
    in let nc2 = cardinal c2
    in if 0 < nc1 then 
      if nc1 < nc2 then c := c2 else c := c1 
    else if nc2 > 0 then c := c2
  ); !c;;


let g0 = [| 
  [|true;true;false;false;false;false|];
  [|true;true;false;false;false;false|];
  [|true;true;true;false;false;false|];
  [|false;false;true;true;false;false|];
  [|false;false;false;true;true;true|];
  [|false;false;false;true;true;true|];
|];;

meilleur_couplage g0;;


