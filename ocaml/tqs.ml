let creer_vide () = ref (Array.make 4 0);;

let rec echange_insere tas i = 
	if i != 1 && !tas.(i) < !tas.(i/2)
	then 
		let temp = !tas.(i/2)
		in 
			!tas.(i/2) <- !tas.(i); 
			!tas.(i) <- temp; 
			echange_insere tas (i/2)
	else ();;


let insere_safe tas n = 
	!tas.(!tas.(0) + 1) <- n ; 
	!tas.(0) <- (!tas.(0) + 1); 
	echange_insere tas !tas.(0)
	;;

let agrandir tas = 
	let n = (Array.length !tas) 
	in let temp = Array.make (1 + 2*(n-1)) 0
	in temp.(0) <- (!tas.(0))
	; for i = 1 to n-1
		do temp.(i) <- (!tas.(i));
		done;
	tas := temp;;

let insere tas n = 
	if (Array.length !tas) - 1 = !tas.(0)
	then agrandir tas else ();
	insere_safe tas n
	;;

let rec echange_retire tas i = 
	let f = if (i*2) <= !tas.(0) then (
		if (i*2+1) > !tas.(0)
		then (
			if (min !tas.(i*2+1) !tas.(i*2)) < !tas.(i)
			then (if !tas.(i*2+1) < !tas.(i*2) then (i*2+1) else (i*2))
			else 0	
		)
		else (if !tas.(i*2) < !tas.(i) then (i*2) else 0)
	) else 0
	in print_int f ;
	if f > 1 then
		let temp = !tas.(f)
		in 
			!tas.(f) <- !tas.(i); 
			!tas.(i) <- temp; 
			echange_retire tas (f)
	else ();;


let retirer_min tas = 
	let n = !tas.(1)
	in 
		!tas.(1) <- !tas.(!tas.(0));
		!tas.(!tas.(0)) <- 0;
		!tas.(0) <- (!tas.(0) - 1);
		echange_retire tas 1;
	n;;	

let tri_par_tas table = 
	let tas = creer_vide ()
	in for i = 0 to (Array.length table) - 1 do insere tas table.(i) done; 
	let res = Array.make !tas.(0) 0
	in for i = 0 to !tas.(0) - 1 
	do res.(i) <- (retirer_min tas) done; res;;
	
	
let rec rand_list m n = 
	let l = Array.make n 0
	in for i = 0 to n do l.(i) <- (Random.int m) done; 
	l;;


let est_trie t = 
	let b = ref true
	in for i = 0 to (Array.length t) - 2
		do if t.(i) > t.(i+1) then b := false else ()
	done; !b;;


let t = [|7;2;5;1;3;8;6|];;

est_trie [|1;4;6;8|];;

tri_par_tas t;;
	
	
	
	
	
	