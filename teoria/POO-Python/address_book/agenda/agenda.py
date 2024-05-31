import os;
import json;
from .contacto import Contacto

class Agenda:
  def __init__(self, path_data):
    self._contacts = self.recuperar_agenda(path_data)

  def recuperar_agenda(self, path_data):
    if not (os.path.exists(path_data)):
      return []

    with open(path_data, "r") as data: 
      datos = json.load(data)
      print("Recuperación exitosa...\n")
    return [Contacto.parsear_de_json(dic) for dic in datos]

  def guardar_agenda(self):
    contacts_pars = [contact.parsear_a_json() for contact in self._contacts]
    with open("./data/data.json", "w", encoding = "utf-8") as save:
      json.dump(contacts_pars, save, ensure_ascii=False, indent=2)
      print("Guardacion exitosa...\n")

  def getContact(self, pattern):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), pattern.lower())
        if isName:
          return contact
    return "No encontrado\n"

  def insertContact(self, newContact):
    for idx, saved in enumerate(self._contacts):
      if saved.nombre == newContact.nombre:
        self._contacts[idx] = newContact
        print("El contacto se sobreescribió exitosamente...\n")
        return

    self._contacts.append(newContact)
    print("El contacto se guardó exitosamente...\n")

\subsection{Método \texttt{updateContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def updateContact(self, newContact):
    for idx, saved in enumerate(self._contacts):
        if saved.nombre == newContact.nombre:
            self._contacts[idx] = newContact
            print("El contacto se actualizó exitosamente...\n")
            return
    print("No se encontró el contacto a actualizar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Actualizar un contacto existente en la lista \texttt{\_contacts}.
    \item \textbf{Parámetros:}
    \texttt{newContact}: Un objeto de contacto que contiene la nueva información que se desea actualizar.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts} usando \texttt{enumerate} para obtener tanto el índice como el objeto de contacto actual.
        \item \textbf{Comparación:} Dentro del bucle, compara el nombre (\texttt{nombre}) del contacto guardado (\texttt{saved}) con el nombre del nuevo contacto (\texttt{newContact}).
        \item \textbf{Actualización:} Si encuentra una coincidencia, reemplaza el contacto existente en la lista con el nuevo contacto (\texttt{newContact}).
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return} para evitar iteraciones innecesarias.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} El método es eficiente para listas pequeñas, pero en listas muy grandes podría ser mejorable dado que su complejidad es \(O(n)\) en el peor de los casos.
    \item \textbf{Mensajes de Usuario:} Los mensajes proporcionan retroalimentación inmediata al usuario sobre el estado de la operación.
\end{itemize}

\subsection{Método \texttt{deleteContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def deleteContact(self, pattern):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), pattern.lower())
        if isName:
            self._contacts.remove(contact)
            print("El contacto se eliminó exitosamente...\n")
            return
    print("No se encontró el contacto a eliminar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Eliminar un contacto de la lista \texttt{\_contacts} que coincida con un patrón dado.
    \item \textbf{Parámetros:}
    \texttt{pattern}: Un patrón de texto que se usará para buscar coincidencias en los nombres de los contactos.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts}.
        \item \textbf{Comparación:} Convierte los nombres de los contactos y el patrón a minúsculas para una comparación insensible a mayúsculas/minúsculas.
        \item \textbf{Coincidencia:} Utiliza un método auxiliar \texttt{\_match} para verificar si el nombre coincide con el patrón.
        \item \textbf{Eliminación:} Si encuentra una coincidencia, elimina el contacto de la lista \texttt{\_contacts}.
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return}.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} La complejidad de este método también es \(O(n)\) debido a la necesidad de recorrer toda la lista para encontrar una coincidencia.
    \item \textbf{Método \texttt{\_match}:} La efectividad del método depende de cómo se implemente \texttt{\_match}. Suponiendo que hace una comparación simple de patrones, podría mejorarse para patrones más complejos.
    \item \textbf{Mensajes de Usuario:} Similar al método \texttt{updateContact}, proporciona retroalimentación útil al usuario sobre el estado de la operación.
\end{itemize}
\subsection{Método \texttt{updateContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def updateContact(self, newContact):
    for idx, saved in enumerate(self._contacts):
        if saved.nombre == newContact.nombre:
            self._contacts[idx] = newContact
            print("El contacto se actualizó exitosamente...\n")
            return
    print("No se encontró el contacto a actualizar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Actualizar un contacto existente en la lista \texttt{\_contacts}.
    \item \textbf{Parámetros:}
    \texttt{newContact}: Un objeto de contacto que contiene la nueva información que se desea actualizar.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts} usando \texttt{enumerate} para obtener tanto el índice como el objeto de contacto actual.
        \item \textbf{Comparación:} Dentro del bucle, compara el nombre (\texttt{nombre}) del contacto guardado (\texttt{saved}) con el nombre del nuevo contacto (\texttt{newContact}).
        \item \textbf{Actualización:} Si encuentra una coincidencia, reemplaza el contacto existente en la lista con el nuevo contacto (\texttt{newContact}).
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return} para evitar iteraciones innecesarias.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} El método es eficiente para listas pequeñas, pero en listas muy grandes podría ser mejorable dado que su complejidad es \(O(n)\) en el peor de los casos.
    \item \textbf{Mensajes de Usuario:} Los mensajes proporcionan retroalimentación inmediata al usuario sobre el estado de la operación.
\end{itemize}

\subsection{Método \texttt{deleteContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def deleteContact(self, pattern):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), pattern.lower())
        if isName:
            self._contacts.remove(contact)
            print("El contacto se eliminó exitosamente...\n")
            return
    print("No se encontró el contacto a eliminar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Eliminar un contacto de la lista \texttt{\_contacts} que coincida con un patrón dado.
    \item \textbf{Parámetros:}
    \texttt{pattern}: Un patrón de texto que se usará para buscar coincidencias en los nombres de los contactos.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts}.
        \item \textbf{Comparación:} Convierte los nombres de los contactos y el patrón a minúsculas para una comparación insensible a mayúsculas/minúsculas.
        \item \textbf{Coincidencia:} Utiliza un método auxiliar \texttt{\_match} para verificar si el nombre coincide con el patrón.
        \item \textbf{Eliminación:} Si encuentra una coincidencia, elimina el contacto de la lista \texttt{\_contacts}.
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return}.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} La complejidad de este método también es \(O(n)\) debido a la necesidad de recorrer toda la lista para encontrar una coincidencia.
    \item \textbf{Método \texttt{\_match}:} La efectividad del método depende de cómo se implemente \texttt{\_match}. Suponiendo que hace una comparación simple de patrones, podría mejorarse para patrones más complejos.
    \item \textbf{Mensajes de Usuario:} Similar al método \texttt{updateContact}, proporciona retroalimentación útil al usuario sobre el estado de la operación.
\end{itemize}
 \subsection{Método \texttt{updateContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def updateContact(self, newContact):
    for idx, saved in enumerate(self._contacts):
        if saved.nombre == newContact.nombre:
            self._contacts[idx] = newContact
            print("El contacto se actualizó exitosamente...\n")
            return
    print("No se encontró el contacto a actualizar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Actualizar un contacto existente en la lista \texttt{\_contacts}.
    \item \textbf{Parámetros:}
    \texttt{newContact}: Un objeto de contacto que contiene la nueva información que se desea actualizar.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts} usando \texttt{enumerate} para obtener tanto el índice como el objeto de contacto actual.
        \item \textbf{Comparación:} Dentro del bucle, compara el nombre (\texttt{nombre}) del contacto guardado (\texttt{saved}) con el nombre del nuevo contacto (\texttt{newContact}).
        \item \textbf{Actualización:} Si encuentra una coincidencia, reemplaza el contacto existente en la lista con el nuevo contacto (\texttt{newContact}).
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return} para evitar iteraciones innecesarias.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} El método es eficiente para listas pequeñas, pero en listas muy grandes podría ser mejorable dado que su complejidad es \(O(n)\) en el peor de los casos.
    \item \textbf{Mensajes de Usuario:} Los mensajes proporcionan retroalimentación inmediata al usuario sobre el estado de la operación.
\end{itemize}

\subsection{Método \texttt{deleteContact}}
\subsubsection{Definición del Método}
\begin{verbatim}
\begin{lstlisting}[language=python]
def deleteContact(self, pattern):
    for contact in self._contacts:
        name = contact.nombre
        isName = self._match(name.lower(), pattern.lower())
        if isName:
            self._contacts.remove(contact)
            print("El contacto se eliminó exitosamente...\n")
            return
    print("No se encontró el contacto a eliminar...\n")
\end{lstlisting}
\end{verbatim}

\subsubsection{Descripción del Funcionamiento}
\begin{itemize}
    \item \textbf{Propósito:}
    Eliminar un contacto de la lista \texttt{\_contacts} que coincida con un patrón dado.
    \item \textbf{Parámetros:}
    \texttt{pattern}: Un patrón de texto que se usará para buscar coincidencias en los nombres de los contactos.
    \item \textbf{Flujo de Control:}
    \begin{itemize}
        \item \textbf{Iteración:} El método recorre la lista \texttt{\_contacts}.
        \item \textbf{Comparación:} Convierte los nombres de los contactos y el patrón a minúsculas para una comparación insensible a mayúsculas/minúsculas.
        \item \textbf{Coincidencia:} Utiliza un método auxiliar \texttt{\_match} para verificar si el nombre coincide con el patrón.
        \item \textbf{Eliminación:} Si encuentra una coincidencia, elimina el contacto de la lista \texttt{\_contacts}.
        \item \textbf{Salida:} Imprime un mensaje de éxito y sale del método con \texttt{return}.
        \item \textbf{No Encontrado:} Si no se encuentra una coincidencia tras iterar toda la lista, imprime un mensaje indicando que no se encontró el contacto.
    \end{itemize}
\end{itemize}

\subsubsection{Análisis}
\begin{itemize}
    \item \textbf{Eficiencia:} La complejidad de este método también es \(O(n)\) debido a la necesidad de recorrer toda la lista para encontrar una coincidencia.
    \item \textbf{Método \texttt{\_match}:} La efectividad del método depende de cómo se implemente \texttt{\_match}. Suponiendo que hace una comparación simple de patrones, podría mejorarse para patrones más complejos.
    \item \textbf{Mensajes de Usuario:} Similar al método \texttt{updateContact}, proporciona retroalimentación útil al usuario sobre el estado de la operación.
\end{itemize}
 def  updateContact(self, newContact):
    for idx, saved in enumerate(self._contacts):
      if saved.nombre == newContact.nombre:
        self._contacts[idx] = newContact
        print("El contacto se actualizó exitosamente...\n")
        return
    print("No se encontró el contacto a actualizar...\n")
    
  def deleteContact(self, pattern):
    for contact in self._contacts:
      name = contact.nombre
      isName = self._match(name.lower(), pattern.lower())
      if isName:
        self._contacts.remove(contact)
        print("El contacto se eliminó exitosamente...\n")
        return
    print("No se encontró el contacto a eliminar...\n")

  def listAgenda(self):
    for contact in self._contacts:
      print(contact)

  def __repr__(self) -> str:
    return self.__str__()

  def __str__(self) -> str:
    return '\n'.join([str(contact) for contact in self._contacts])

  # Algoritmo Knuth-Morris-Pratt (KMP)
  def _match(self, name, pattern):
    lps = self._compute_lps(pattern)
    i = 0
    j = 0

    while i < len(name):
      if pattern[j] == name[i]:
        i += 1
        j += 1

      if j == len(pattern):
        j = lps[j - 1]
        return True
      elif i < len(name) and pattern[j] != name[i]:
        if j != 0:
          j = lps[j - 1]
        else:
          i += 1
    return False

  # Generación de la funcion π
  def _compute_lps(self, pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
      if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
      else:
        if length != 0:
          length = lps[length - 1]
        else:
          lps[i] = 0
          i += 1
    return lps
