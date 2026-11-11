# 🔥 Análisis de datos: Pokémon de primera generación

Limpieza, análisis estadístico y visualización de los 151 Pokémon de la primera generación con pandas.

Proyecto académico de Ciencia de Datos — Ingeniería en Informática, UTEM.

## Qué hace

1. **Limpieza de datos**: elimina espacios, valores negativos y duplicados; valida que cada Pokémon sea de primera generación (contra una lista de referencia) y que sus tipos sean válidos.
2. **Filtrado y selección**: por ejemplo, Pokémon de tipo Fuego con su ataque y velocidad.
3. **Estadística descriptiva**: media, mediana y moda del ataque; rango y desviación estándar de PS; mayor defensa, menor velocidad y Pokémon de doble tipo.
4. **Visualización**: histograma de ataque, dispersión ataque vs velocidad, boxplot de PS por tipo y violín de defensa.
5. **Manipulación**: crea la columna *Poder total* y exporta el dataset actualizado.

## Archivos

| Archivo | Contenido |
|---|---|
| `tarea.py` | Script principal |
| `pokemon_primera_gen.csv` | Datos originales (con errores a limpiar) |
| `lista_limpia_de_pokemones_de_primera_generacion.csv` | Lista de referencia para validar |
| `pokemon_primera_gen_actualizado.csv` | Resultado con *Poder total* |

## Tecnologías

Python · pandas · NumPy · matplotlib · seaborn

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python tarea.py
```
