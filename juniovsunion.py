if __name__ == '__main__':
	boleta = str()
	ciudadania = str()
	sur = 40000
	norte = 40000
	oriental_alta = 80000
	oriental_baja = 90000
	occidental_baja = 140000
	occidental_alta = 120000
	cont = 0
	acum = 3
	usuarios = 10
	costo = 0
	ubi = 0
	ubi2 = 0
	while True:# no hay 'repetir' en python
		print("Ingrese su nombre y su apellido: ")
		nombre_usu = input()
		print("¿Desea comprar su boleta en línea? (Responda Si/No): ")
		boleta = input()
		print("¿Es usted barranquillero? (Responda Si/No):")
		ciudadania = input()
		if boleta=="si" or boleta=="Si" or boleta=="SI":
			if ciudadania=="si" or ciudadania=="Si" or ciudadania=="SI":
				print("Usted comprará su boleta en línea y es barranquillero")
				usuarios = usuarios-1
				if acum>0:
					print("En donde desea ubicarse, digite 1.Sur 2.Norte 3.Oriental 4.Occidental: ")
					ubi = float(input())
					if ubi==1:
						costo = (sur*40)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==2:
						costo = (norte*40)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==3:
						print("Digite 1 para Oriental alta o 2 para Oriental baja: ")
						ubi2 = float(input())
						if ubi2==1:
							costo = (oriental_alta*40)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
						else:
							costo = (oriental_baja*40)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==4:
						print("Digite 1 para Occidental alta o 2 para Occidental baja: ")
						ubi2 = float(input())
						if ubi2==1:
							costo = (occidental_alta*40)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
						else:
							costo = (occidental_baja*40)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
			else:
				print("Usted comprará su boleta en línea y es Samario")
				usuarios = usuarios-1
				if acum>0:
					print("En donde desea ubicarse, digite 1.Sur 2.Norte 3.Oriental 4.Occidental: ")
					ubi = float(input())
					if ubi==1:
						costo = (sur*25)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==2:
						costo = (norte*25)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==3:
						print("Digite 1 para Oriental alta o 2 para Oriental baja: ")
						ubi2 = float(input())
						if ubi2==1:
							costo = (oriental_alta*25)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
						else:
							costo = (oriental_baja*25)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					if ubi==4:
						print("Digite 1 para Occidental alta o 2 para Occidental baja: ")
						ubi2 = float(input())
						if ubi2==1:
							costo = (occidental_alta*25)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
						else:
							costo = (occidental_baja*25)/100
							acum = acum-1
							print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
		else:
			print("Usted comprará su boleta en taquilla")
			if acum>0:
				print("En donde desea ubicarse, digite 1.Sur 2.Norte 3.Oriental 4.Occidental: ")
				ubi = float(input())
				if ubi==1:
					costo = (sur*10)/100
					acum = acum-1
					print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
				if ubi==2:
					costo = (norte*10)/100
					acum = acum-1
					print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
				if ubi==3:
					print("Digite 1 para Oriental alta o 2 para Oriental baja: ")
					ubi2 = float(input())
					if ubi2==1:
						costo = (oriental_alta*10)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					else:
						costo = (oriental_baja*10)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
				if ubi==4:
					print("Digite 1 para Occidental alta o 2 para Occidental baja: ")
					ubi2 = float(input())
					if ubi2==1:
						costo = (occidental_alta*10)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
					else:
						costo = (occidental_baja*10)/100
						acum = acum-1
						print(nombre_usu," el costo final de tu boleta es de: ",costo," pesos")
		if usuarios==0: break