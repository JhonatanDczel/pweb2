# <samp>Agenda telefónica :green_book:</samp>
## Directrices  generales
1. El programa necesita guardar los datos que el usuario dispone, estos datos deben ser almacenados en algún tipo de archivos. Debido a que se necesitan guardar listas de objetos, se ha decidido hacer uso de archivos JSON, un formato ligero de intercambio de datos, fácil de leer y escribir con la biblioteca json de Python, adecuado para datos estructurado.

2. Leer y escribir en archivos con Python viene de forma nativa y se utiliza a través de las funciones integradas `open`, `read`, `write` entre otras. Sin embargo para manejar ciertos formatos especificos como JSON, Python ofrece el modulo estándar `json`.

## <samp>La clase Contact :hammer:</samp>
Debe contener 4 campos: `name`, `number`, `address` y `relation` con sus respectivos métodos setters y getters y su debido constructor. También debe de contener métodos 3  métodos especiales:

- Un método que nos permita parsear el objeto actual como un diccionario. Por ejemplo, que el identificador de referencia al campo `name` sea como clave y su valor sea el correspondiente valor del campo.

- Un método que reciba como argumento un diccionario, basicamente es el objeto JSON parseado por el modulo `json` de Python. Este diccionario contiene los campos de una instancia de la clase Contact, por lo tanto con estos datos se debe crear el nuevo objeto. Si analizamos, este método será parte de cargar los datos guardados en un archivo JSON.

- El método `toString()` al igual que java, que realice la misma funcionalidad. En Python este método es denomina `__str__`

## <samp>La clase Agenda :skull:</samp>
Contiene los métodos que se llaman en la clase Main

## <samp>La clase Main :eyes:</samp>
Contienen los métodos que interactuan con el usuario

# <samp>Carrito de compras :shopping_cart:</samp>
## <samp>La clase ProductStock :eyes:</samp>
Por el momento solo contiene los 3 campos `name`, `value` y `quatity`, además de su correspondiente constructor y los métodos setters y getters.

## <samp>La clase StockProducts :hammer_and_pick:</samp>
Contiene un campo que almacena los productos en stock. Por lo tanto puede ser una lista de objetos ProductStock, sin embargo, podemos especificar un `id` para cada tipo de producto, una forma de identificarlo unicamente y que con `id` directamente podamos acceder a la informacion del producto como es el nombre, costo y cantidad.

### <samp>Entonces, ¿qué estructura usar?</samp>
Los diccionario en Python nos facilitaria acceder directamente a la informacion del producto sin la necesidad de tener que iterar por cada objeto ProductStock y comparar su campo `name` como se tendria que hacer si la estructura sería una simple lista de objetos ProductStock.

Los métodos que necesitamos implementar como minimo son los siguientes:
1. `add_product:` Se encargará de agregar un nuevo producto al diccionario, donde la clave es el nombre del producto, asi ingresar a la información del producto es más eficiente.

2. `get_product:` Se encargará de obtener el producto según el nombre que reciba como argumento, aqui podemos observar la funcionalidad del diccionario, ya que solo necesitamos pasar el argumento como clave para buscar en el diccionario en vez de tener que iterar por cada objeto en caso de una lista. Claro esta que son estructuras de datos y su concepto no involucra saber cómo esta implementado por dentro.

## <samp>La clase ShoppingCart :money_mouth_face:</samp>
Al igual que la clase StockProducts usamos el concepto de `Asociación`, pues se tendrá una referencia una instancia de StockProducts, lo cual nos permite saber la informacion de la lista de productos en stock, claro está que es un diccionario. 

### Cómo almacenar los productos puestos en el carrito de compras y qué cantidad de cada uno
Para poder conectar con los productos en stock rápidamente podemos pensar que esta estructura tambien debe de ser un diccionario donde la clave es el nombre del producto y el valor es la cantidad de unidades puestas en el carrito de compras :shopping_cart:.

Los métodos que necesitamos implementar como minimo son los siguientes:
1. `add_item:` Como vemos, este método debe de recibir 2 argumentos, que son el nombre del producto y la cantidad de unidades a comprar. Entonces la lógica en este método se divide en 2 partes:
    - Verificar si el producto está en el campo que referencia a una instancia de StockProducts y verificar tambien si la cantidad a comprar es menor o igual que la cantidad disponible.
    - Verificar que si el el producto ya está en el carrito de compras solo aumentar la cantidad de unidades, de lo contrario agregar el producto al carrito de compras con su correspondiente cantidades de unidades iniciales.

2. `finalize_purchase:` Este método debe confirmar la compra modificando la referencia a StockProducts justamente la cantidad disponible de cada producto. Recordemos que podemos no confirmar y entonces la cantidad disponible para los otros usuarios no cambiará.

3. `calculate_total:` Usando la clave de los diccionarios, podemos acceder al costo del producto y en la referencia a StockProducts y acceder a la cantidad comprada en el campo que se encargará de almacenar los productos agregados al carrito de compras. Sumamos esta multiplicación y ese sería el resultado final.
