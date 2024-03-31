type graphe = bool array array;;
type etiquetage = int array;;

let est_col g e = 
	let n = Array.length g
	in if Array.length e < n then false
	else 
	let r = ref true
	in	for i = 0 to n - 1
		do
			for j = 0 to n -1
			do
				if g.(i).(j) && e.(i) = e.(j)
				then r := false
			done
		done;
	!r;;



let deux_col g =
	let n = Array.length g
	in let e = Array.make n (-1)
	in let bi = ref true
	in let rec parcours i c =
		if e.(i) = -1
			then e.(i) <- c ;
			for j = 0 to n - 1
			do
				if g.(i).(j) then
				let et = e.(j)
				in if et = -1
					then parcours j ((c+1) mod 2)
					else if et = c then bi := false
			done 
	in 
	for i = 0 to n - 1
	do parcours i 0 done;
	e
	;;


let min_couleur_possible g e s = 
	let n = Array.length g
	in let t = Array.make n false
	in for i = 0 to n - 1
	do
		if e.(i) < n then t.(e.(i)) <- true
	done;
	let c = ref (-1)
	in for i = 0 to n - 1
	do
		if g.(s).(i) && !c = (-1) && not t.(i)
		then c := i
	done;
	if !c = -1 then n else !c;;

min_couleur_possible [|[|false;true;true;true|]|] [|0;1;2;4|] 0;;


let min_couleur_possible g e s =
	let n = ref 0
	let m = ref 0
	for i = 0 to (Array.length g) - 1
	do
		if g.(i).(j)
			let c = e.(j)
			in if c = !n
			then n := !m 
;;

let t = []

let g = [|
		[|false;false;true;true;false|];
		[|false;false;false;true;true|];
		[|true;false;false;false;true|];
		[|true;true;false;false;false|];
		[|false;true;true;false;false|];
|];;

(* R = 0, V = 1, B = 2*)
let e = [|0;0;2;1;1|];;

est_col g e;;


let g1=[|
[|false;false;false;false;true;true;false;false|];
[|false;false;false;false;true;true;true;false|];
[|false;false;false;false;false;false;true;false|];
[|false;false;false;false;false;false;false;true|];
[|true;true;false;false;false;false;false;false|];
[|true;true;false;false;false;false;false;false|];
[|false;true;true;false;false;false;false;false|];
[|false;false;false;true;false;false;false;false|];
|];;
deux_col g1;; 


