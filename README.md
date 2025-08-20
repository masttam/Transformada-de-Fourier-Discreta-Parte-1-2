# Examen P1 — DFT de señal AM seno


## Objetivo
- Aplicar la Transformada de Fourier Discreta (DFT) a señales muestreadas.
- Identificar picos espectrales, estimar frecuencias y amplitudes relativas.
- Calcular y utilizar la resolución en frecuencia (?f = f?/N).


## Señal
Se trabaja con la señal continua:


x(t) = [1 + m cos(2p f_m t)] sin(2p f_c t)


con parámetros: f_m = 0.5 Hz, f_c = 8 Hz, m = 0.5.


## Estructura del repositorio:
+-- main.py +-- .gitignore +-- requirements.txt +-- README.md +-- src/ ¦ +-- examen_p1.py ¦ +-- utils/ ¦ +-- grapher.py

## Cómo ejecutar
1. Crea y activa un entorno virtual (opcional pero recomendado).
2. Instala dependencias: `pip install -r requirements.txt`.
3. Ejecuta la práctica:


```bash
python main.py examen_p1