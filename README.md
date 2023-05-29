## Autor
- [@jcandiap](https://github.com/jcandiap)

## Python Version ➡️ 3.11.2

Dependencias instaladas dentro del .venv:
- asgiref **3.7.1**
- Django **4.2.1**
- sqlparse **0.4.4**

# Funcionamiento de la APP
## Usuario
- La aplicación cuenta con una parte de Login y Registro de usuario

## Productos
- Los productos se muestran todos en la página principal
- Al hacer click en un producto se puede ver la información completa de esta
- En la parte superior existe un filtro donde se pueden ver los productos por categoria

## Mantenedores
- Existen mantenedores para Productos, Categorias y Paises (Esta ultima se usa solo para el formulario de registro de los usuarios)

## Notas 🥺
- Al generar los modelos tuve un problema al utilizar el Field UUID es por eso que utilice la libreria de Python uuid para generar el valor por defecto
- Debo modificar el mantenedor de paises ya que este quedo dentro de la ruta "/profile" (espero recomendaciones 🥲)
- El login lo maneje de forma distinta ya que queria que hubiera mas interacción en la pagina sin recargarla es por esto que agregue JavaScript y cambié la forma de capturar la respuesta enviando desde la vista un Json
- A estas horas de la noche recorde que le hice un modelo galeria al producto para poder almacenar mas imagenes 🤦🏻‍♂️ lo olvide completamente asi que espero poder agregarlo despues de que lo entregue o ya para la siguiente entrega 😓
- Se que me faltaron validar campos espero subir esos cambios el dia de hoy (29 de Mayo)

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jcandiap/)
