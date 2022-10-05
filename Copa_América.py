a="\n"
if __name__ == '__main__':
	brasil = int()
	chile = int()
	argentina = int()
	ecuador = int()
	peru = int()
	paraguay = int()
	uruguay = int()
	colombia = int()
	cuartos1 = str()
	cuartos2 = str()
	cuartos3 = str()
	cuartos4 = str()
	semis1 = int()
	semis2 = int()
	semis3 = int()
	semis4 = int()
	gol1_tercer_cuarto = int()
	gol2_tercer_cuarto = int()
	gol1_final = int()
	gol2_final = int()
	print("Primer partido de cuartos")
	print(a)
	print("Brasil VS Chile")
	print(a)
	print("Cuántos goles metió Brasil?")
	brasil = int(input())
	print("Cuántos goles metió Chile?")
	chile = int(input())
	if brasil>chile:
		print("Brasil pasa a semifinal")
		cuartos1 = "Brasil"
	else:
		print("Chile pasa a semifinal")
		cuartos1 = "Chile"
	print("Segundo partido de cuartos")
	print(a)
	print("Perú VS Paraguay")
	print(a)
	print("Cuántos goles metió Perú?")
	peru = int(input())
	print("Cuántos goles metió Paraguay?")
	paraguay = int(input())
	if peru>paraguay:
		print("Perú pasa a semifina")
		cuartos2 = "Perú"
	else:
		print("Paraguay pasa a semifinal")
		cuartos2 = "Paraguay"
	print("Tercer partido de cuartos")
	print(a)
	print("Argentina VS Ecuador")
	print(a)
	print("¿Cuántos goles metió Argentina?")
	argentina = int(input())
	print("¿Cuántos goles metió Ecuador?")
	ecuador = int(input())
	if argentina>ecuador:
		print("Argentina pasa a semifinal")
		cuartos3 = "Argentina"
	else:
		print("Ecuador pasa a semifinal")
		cuartos3 = "Ecuador"
	print("Cuarto partido de cuartos de final")
	print(a)
	print("Uruguay VS Colombia")
	print(a)
	print("¿Cuántos goles metió Uruguay?")
	uruguay = int(input())
	print("¿Cuántos goles metió Colombia?")
	colombia = int(input())
	if uruguay>colombia:
		print("Uruguay pasa a semifinal")
		cuartos4 = "Uruguay"
	else:
		print("Colombia pasa a semifinal")
		cuartos4 = "Colombia"
	print(a)
	print("Semifinales")
	print(a)
	print("Primer partido de semifinales")
	print(a)
	print(cuartos1," VS ",cuartos2)
	print(a)
	print("¿Cuántos goles metió ",cuartos1,"?")
	semis1 = int(input())
	print("¿Cuántos goles metió ",cuartos2,"?")
	semis2 = int(input())
	if semis1>semis2:
		print(cuartos1," pasa a la Final")
		final1 = cuartos1
		tercer_cuarto1 = cuartos2
	else:
		print(cuartos2," pasa a la Final")
		final1 = cuartos2
		tercer_cuarto1 = cuartos1
	print("Segundo partido de semifinales")
	print(a)
	print(cuartos3," VS ",cuartos4)
	print(a)
	print("¿Cuántos goles metió ",cuartos3,"?")
	semis3 = int(input())
	print("¿Cuántos goles metió ",cuartos4,"?")
	semis4 = int(input())
	if semis3>semis4:
		print(cuartos3," pasa a la Final")
		final2 = cuartos3
		tercer_cuarto2 = cuartos4
	else:
		print(cuartos4," pasa a la Final")
		final2 = cuartos4
		tercer_cuarto2 = cuartos3
	print(a)
	print("Se define el 3er y el 4to puesto")
	print(a)
	print(tercer_cuarto1," VS ",tercer_cuarto2)
	print(a)
	print("¿Cuántos goles metió ",tercer_cuarto1,"?")
	gol1_tercer_cuarto = int(input())
	print("¿Cuántos goles metió ",tercer_cuarto2,"?")
	gol2_tercer_cuarto = int(input())
	if gol1_tercer_cuarto>gol2_tercer_cuarto:
		print(tercer_cuarto1," se lleva el Tercer lugar de la Copa Am�rica")
		tercero = tercer_cuarto1
		cuarto = tercer_cuarto2
	else:
		print(tercer_cuarto2," se lleva el Tercer lugar de la Copa Am�rica")
		tercero = tercer_cuarto2
		cuarto = tercer_cuarto1
	print("Final de la Copa Am�rica")
	print("Se define el 1er y el 2do puesto")
	print(a)
	print(final1," VS ",final2)
	print(a)
	print("¿Cuántos goles metió ",final1,"?")
	gol1_final = int(input())
	print("¿Cuántos goles metió ",final2,"?")
	gol2_final = int(input())
	if gol1_final>gol2_final:
		print(final1," es el Campeón de América")
		primero = final1
		tow = final2
	else:
		print(final2," es el Campeón de América")
		primero = final2
		tow = final1
	print(a)
	print(primero," es el Campeón")
	print(a)
	print(tow," es el Subcampeón")
	print(a)
	print(tercero,"se lleva el tercer puesto")
	print(a)
	print(cuarto,"se lleva el cuarto puesto")

print(a)
print("By Julio Arellano @ Blaviken-fsociety")
print(a)