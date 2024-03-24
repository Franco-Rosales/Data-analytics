import pandas as pd
from ydata_profiling import ProfileReport

def generate_profile_report(csv_file_path, report_title, output_file_path, delimiter=','):
    """
    Genera un informe de perfil para un archivo CSV dado y guarda el informe en un archivo HTML.

    Parameters:
    csv_file_path (str): Ruta del archivo CSV.
    report_title (str): Título del informe.
    output_file_path (str): Ruta y nombre del archivo HTML de salida.
    delimiter (str, optional): Carácter utilizado como delimitador en el archivo CSV. Por defecto, ','.
    """
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(csv_file_path, sep=delimiter)

    # Generar un informe de perfil
    profile = ProfileReport(df, title=report_title)

    # Guardar el informe en un archivo HTML
    profile.to_file(output_file_path)

# Ejemplo de uso de la función para el archivo "netflix_titles.csv" (delimitador ';')
generate_profile_report("CSV/netflix_titles.csv", "Análisis Descriptivo - Netflix Titles", "Reportes/netflix_report.html", delimiter=';')

# Ejemplo de uso de la función para el archivo "Disney_plus_titles.csv" (delimitador ',')
generate_profile_report("CSV/Disney_plus_titles.csv", "Análisis Descriptivo - Disney+ Titles", "Reportes/disney_report.html", delimiter=',')
