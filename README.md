# Python SharePoint Office365 API
You will find example on connecting to Office 365 SharePoint using the Office 365 Rest Python Client package.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`sharepoint_email`

`sharepoint_password`

`sharepoint_url_site`

`sharepoint_site_name`

`sharepoint_doc_library`


## Installation

Create Virtual Environment  

```bash
  python -m venv env
```

Activate Environment
```bash
  source env/Scripts/activate
```

Install Packages
```bash
  pip install -r requirements.txt
```

Install Office365 API Package Directly from Github
```bash
  pip install git+https://github.com/vgrem/Office365-REST-Python-Client.git#egg=Office365-REST-Python-Client
```

    Descargas necesarias además de Python:
* Libreria Pandas
* Libreria Office365-REST-Python-Client





Creación y ejecución de entorno virtual, conexión y extracción de archivos alojados en SharePoint Microsoft365:
 

C:\Users\crist>python -m venv env

C:\Users\crist>.\env\Scripts\activate

(env) C:\Users\crist>pip install Office365-REST-Python-Client

(env) C:\Users\crist>pip freeze > requirements.txt

cd C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main


---------->>>>>>>>>>> Este ultimo comando descarga los archivos completos que tiene una carpeta junto a sus subcarpetas y aloja estos en la ruta especificada de manera local.

python download_files_with_subfolder.py "Anexo IEB/Reportes" "C:\Users\crist\OneDrive\Documentos\Cristhian\Cristhian\CRISS\Allcot\DocumentosProyectos\python-sharepoint-office365-api-main\ARCHIVOS" Yes"# AnexoIEB_Allcot_Conexion365" 
