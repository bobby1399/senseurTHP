#Tran Robert
#TP2 - Programmation en reseau
#Pour Karine

from flask import Flask, render_template
import os

# Directory path
path = "C:/Environnement/Configuration/Environnement.config"

# Initialiser la configuration
config_path = open(path,"r")
config_Lines = config_path.readlines()
new_Path = config_Lines[0].split("\n")[0].split("=")[1]
new_File = config_Lines[1].split("\n")[0].split("=")[1]
config_path.close()

def FnAfficherDonnees(fichDonnees):
	
	# Initialisation des variables    
	lines_r = 0         # variable pour representer les lignes restantes         
	n = 0
	check = 0
	y=0
	d = 0
	p=0
	z=0
	global donnee_moyenne
	global html_data1
	global html_data2
	global html_data3
	global html_data4
	global html_data5
	global header
	donneesFichier = open(fichDonnees,"r")
	donneesLignes = donneesFichier.readlines()  
	donneesFichier.close()

	# Nombre de donnees dans le fichier .csv
	for i in donneesLignes:    
			lines_r += 1
	#Selectionner 5 derniere lignes
	if lines_r >=96:    
		for i in range(5):
			elements = donneesLignes[n].split("\n")[0].split(" ")
			date_1 = elements[0].replace("-","/") 
			Heure = elements[1].split(",")[0].split(":")[0]
			Minute = elements[1].split(",")[0].split(":")[1]
			donnee1 = elements[1].split(",")[1]
			donnee2 = elements[1].split(",")[2]
			donnee3 = elements[1].split(",")[3]
			#donnes pour moyenne de la temperature    
			x = float(donnee1)
			y += x
			#donnes pour moyenne de l'humidite
			p = float(donnee2)
			z += p

			lines_r -= 1
			n += 1
			
			#lignes de lecture
			if i == 0:
				#heure initial
				heure_2 = str(Heure + 'h' + Minute)
				html_data1 = date_1 + " " + Heure + "h" + Minute + " UTC   %.4f"  %float(donnee1) + "          %.4f" %float(donnee2)
			if i == 1:
				html_data2 = date_1 + " " + Heure + "h" + Minute + " UTC   %.4f"  %float(donnee1) + "          %.4f" %float(donnee2)
			if i == 2:
				html_data3 = date_1 + " " + Heure + "h" + Minute + " UTC   %.4f"  %float(donnee1) + "          %.4f" %float(donnee2)
			if i == 3:
				html_data4 = date_1 + " " + Heure + "h" + Minute + " UTC   %.4f"  %float(donnee1) + "          %.4f" %float(donnee2)
			if i == 4:
				html_data5 = date_1 + " " + Heure + "h" + Minute + " UTC   %.4f"  %float(donnee1) + "          %.4f" %float(donnee2)
			#heure final
			heure_3 = str(Heure + 'h' + Minute)
			#ecart entre les deux heures
			heure_f = heure_2 + '-' + heure_3

	elif lines_r == 0:   
		return
	#moyenne
	d = y/5
	s = z/5
	#test formal print
	donnee_moyenne = str(heure_f + '            %.4f' %d + '        ' + '  %.4f' %s)
	header = str('Heure' + '                  ' + 'C' + '               ' + '%Hum')

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
@app.route('/')

def hello_world():
	#variables globales pour les assigner aux variables html
	global a
	global b
	global c
	global d 
	global e 
	global k
	global j
	
	# write-html.py
	
	f = open('C:/Users/greseau/Desktop/TP2_final/templates/test.html','w')

	message = """<html>
	<head></head>
	<body>Moyennes
	<pre>
<font color="#99BBFF">{{header1}}</font>
{{allo0}}
	</pre>

Lectures
	<pre>
{{donnee1}}
{{donnee2}}
{{donnee3}}
{{donnee4}}
{{donnee5}}
	</pre></body>
	</html>"""

	f.write(message)
	f.close()
	
	return render_template("test.html",allo0 = k, header1 = j, donnee1= a, donnee2 = b, donnee3 = c, donnee4 = d, donnee5=e)
  
if __name__ == '__main__':
	full_path = new_Path + "/" + new_File
	FnAfficherDonnees(full_path)
	a = str(html_data1)
	b = str(html_data2)
	c = str(html_data3)
	d = str(html_data4)
	e = str(html_data5)
	k = str(donnee_moyenne)
	j = str(header)

	app.run()