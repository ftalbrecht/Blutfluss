Benutzung von ode.py



Damit das Programm funktioniert muss das folgende installiert sein:
	- Python 2 oder 3
	- Das Python Package "scipy" (z.B. durch die Anaconda Distribution)
	- gnuplot 5 f�r die Visualisierung
	
	
Im Programmordner m�ssen sich die folgenden Dateien/Ordner befinden:
	- das Hauptprogramm "ode.py"
	- das GnuPlot-Skript "plot.plt" zur Visualisierung
	- ein Ordner mit dem Namen "out"
	
	
Wenn Python und GnuPlot in der PATH-Umgebungsvariablen registriert sind (ggf. auf Haken bei der Installation achten),
l�sst sich das Programm mit dem Befehl

	"python ode.py"

ausf�hren.
Das Programm sollte abschlie�end selber den Befehl

	"gnuplot plot.plt"

aufrufen, um eine Grafik zu erstellen. Alternativ kann man diesen auch selber ausf�hren, um GnuPlot die Grafik erstellen zu lassen.


Die Output-Daten sowie die Grafik befinden sich im "out"-Ordner.