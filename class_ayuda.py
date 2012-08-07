from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import sys
from ui_ayuda import Ui_Ayuda

# Se hereda de la clase QtGui.QDialog
class PopAyuda(QtGui.QDialog):
	# Se define el constructor de la clase __init__
	def __init__(self, categoria):
		# Se llama al constructor de la clase padre
		QtGui.QDialog.__init__(self)
		# Se crea la instancia de Ui_Dialog
		self.ventana = Ui_Ayuda()
		self.ventana.setupUi(self)
		self.categoria = categoria
		self.ventana.buttonBox.connect(self.ventana.buttonBox, SIGNAL("accepted()"),self, SLOT("accept()"))
		
		self.generalGeneral = "<!DOCTYPE html> <html> <body> <h2>Promedieitor</h2> <p> Promedieitor es una aplicacion sencilla, \
		interactiva y universal enfocada en estudiantes blablabla sacar promedios y otras cosas </p> <h3>Interfaz de usuario</h3> <p> \
		Promedieitor tiene una interfaz de usuario (UI) simplista que se basa en la diferencacion entre Evaluaciones y Variables para \
		separar los datos en bruto de los calculos  blablabla </p> <h3>Evaluaciones</h3> <p> Las evaluaciones son el combustible de \
		Promedieitor, con ellas se alimentan las variables para luego calcular la Nota Final (NF)<br> Tienen una estructura bastante \
		simple: <ul> <li>Nombre: Nombre o preferiblemente abreviacion</li> <li>Nota: Valor, entero o decimal de la Evaluacion</li> \
		</ul> La mayor caracteristica de las evaluaciones es permiten obtener resultados rapidamente, sin tener que modificar la formula \
		completa, ni reemplazar cada vez que son requeridas </p> <h3>Variables</h3> <p>El motor mismo de Promedieitor, son las encargadas \
		de procesar los datos brutos para obtener luego el resultado final, el cual se guarda en la variable mas importante de Promedieitor: \
		NF (nota final)</p> <h4>Estructura</h4> <p>La estructua es un poco mas compleja que las Evaluaciones: <ul> <li>Nombre: al igual \
		que las evaluaciones se prefieren abreviaciones</li> <li>Valor: es el valor que toman luego de ser procesadas</li> <li>Tipo: Hay \
		tres tipos de variables que luego comentaremos</li> <li>Parametros: la subrutina que dara el valor a la variable, hay una estructura \
		especifica para cada tipo de variable</li> <li>Ponderacion: Es el factor por el cual se multiplicara el resultado de la subrutina, \
		obteniendo luego el valor final</li> </ul> <h4>Tipos</h4> <p>Hay tres tipos de variables: <ul> <li>ALGEBRAICA: Ocupada para hacer \
		calculos basicos como: suma,resta, multiplicacion y divicion</li> <li>PROMEDIO: Calculo algebraico frecuente al sacar promedios: \
		suma_valores/cant_valores</li> <li>CONDICIONAL: El tipo mas complejo de Promedieitor, encargado de evaluar condiciones</li> </ul> \
		</p> <h4>Variable ALGEBRAICA</h4> <p> Los parametros que recibe tiene son de la forma: <blockquote><code>x[<+|-|*|/>y[...]]</code>\
		</blockquote> donde x e y pueden ser Variables, Evaluaciones, enteros o decimales. a continuacion algunos ejemplos: <blockquote> \
		<code>2+3</code><br> <code>C1 + C2</code><br> <code>0.34 * PC - 50   / EX</code><br> </blockquote> un punto importante a tratar es \
		el orden en que se evaluan los operandos. el orden es * -> / -> + -> - , de la misma forma en que los evalua un humano. otro punto, \
		aun mas importante es que NO ESTAN PERMITIDOS LOS PARENTESIS de ningun tipo Por ultimo recuerda NUNCA escribir primero un negativo cuando \
		solo hay uno en toda la ecuacion, por ej: <code>-x + y</code>, en este caso es preferible <code>y - x</code></p> <h4>Variable PROMEDIO\
		</h4> <p> Los parametros que recibe tiene son de la forma: <blockquote><code>x[,y[...]]</code></blockquote> donde x e y pueden ser \
		Variables, Evaluaciones, enteros o decimales. a continuacion algunos ejemplos: <blockquote> <code>C1,C2,C3</code><br> <code>Lab1 , \
		Lab2</code><br> <code>T1, -T2</code><br> </blockquote> Tan facil como ves </p> <h4>Variable CONDICIONAL</h4> <p> Los parametros que \
		recibe tiene son de la forma: <blockquote><code>< x >,< >|>=|<|<=|==|=|!= ><espacio>< y >:< valor >[& [...]][, ...][;<valor por \
		defecto>]</code></blockquote> donde x e y pueden ser Variables, Evaluaciones, enteros o decimales, siendo x la variable principal a \
		la cual comparar e y una con la cual se compara x. a continuacion algunos ejemplos: <blockquote> <code>NS,<= 55:0;NS</code> (reprobacion \
		absoluta)<br> <code>NS,>= 44 & < 55: NFG; NS</code> (nota con global)<br> <code>X, < Y: X, > Y: Y, == Y: X  </code> ( minimo de X e Y )\
		<br> </blockquote> Este tipo de variable es un poco mas complicado que el resto, por lo que si aun no entiendes, estas invitado a ver \
		la seccion particular del manual </p> </p> </body> </html>"
		
		if self.categoria == "generalGeneral":
			self.ventana.textEdit.setHtml(self.generalGeneral)
