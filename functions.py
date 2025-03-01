inicio = """CREATE TABLE IF NOT EXISTS APLICACION(
ID_APP INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre TEXT NOT NULL UNIQUE
);
CREATE TABLE TAREA(
ID_TASK INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre TEXT NOT NULL,
Peso BIGINT NOT NULL,
ID_APP INTEGER REFERENCES APLICACION(ID_APP) NOT DEFERRABLE
);
CREATE TABLE IF NOT EXISTS REGISTRO(
ID_REGISTRO INTEGER primary KEY autoincrement,
ID_APP INTEGER NOT NULL references APLICACION(ID_APP) NOT deferrable,
ID_TASK INTEGER NOT NULL references TAREA(ID_TASK) NOT deferrable,
CANTIDAD BIGINT NOT null);

insert into aplicacion(nombre) values
('Whatsapp'),
('Telegram'),
('Messenger'),
('X'),
('Instagram'),
('Facebook'),
('Youtube'),
('TikTok'),
('Google Drive'),
('OneDrive'),
('Dropbox'),
('Amazon'),
('Mercado Libre'),
('PayPal'),
('Play Store'),
('App Store'),
('Netflix'),
('Disney+'),
('HBO Max'),
('Spotify'),
('Apple Music'),
('Google Chrome'),
('Bing'),
('Gmail'),
('Outlook'),
('Siri'),
('LinkedIn'),
('Meet'),
('SmartWatch'),
('DoorDash'),
('Slack'),
('Twitch'),
('Google Gemini'),
('SnapChat');

insert into tarea(nombre, peso, id_app) values
('Enviar mensaje de texto', 1024, 1),
('Enviar mensaje multimedia', 2000000, 1),
('Enviar mensaje de texto', 1024, 2),
('Enviar mensaje multimedia', 2000000, 2),
('Enviar mensaje de texto', 1024, 3),
('Enviar mensaje multimedia', 2000000, 3),
('Publicar un tweet', 3000, 4),
('Subir una foto', 5000000, 5),
('Subir/Ver video corto', 10000000, 5),
('Subir una foto', 3000000, 6),
('Subir/Ver video corto', 5000000, 6),
('Ver video de 1 minuto', 5000000, 7),
('Ver video de 1 minuto', 5000000, 8),
('Subir un archivo de 1 MB', 1000000, 9),
('Subir un archivo de 1 MB', 1000000, 10),
('Subir un archivo de 1 MB', 1000000, 11),
('Realizar una compra', 150000, 12),
('Realizar una compra', 150000, 13),
('Realizar una transferencia', 10000, 14),
('Descargar una aplicación', 10000000, 15),
('Descargar una aplicación', 10000000, 16),
('Ver una serie de 1 hora', 500000000, 17),
('Ver una serie de 1 hora', 500000000, 18),
('Ver una serie de 1 hora', 500000000, 19),
('Reproducir una canción', 5000000, 20),
('Reproducir una canción', 5000000, 21),
('Realizar una búsqueda', 5000, 22),
('Realizar una búsqueda', 5000, 23),
('Enviar correo sin adjuntos', 10000, 24),
('Enviar correo sin adjuntos', 10000, 25),
('Enviar correo con archivo adjunto (1 MB)', 1010000, 26),
('Enviar correo con archivo adjunto (1 MB)', 1010000, 27),
('Llamada de voz', 500000, 1), -- Whatsapp
('Llamada de voz', 500000, 2), -- Telegram
('Enviar sticker', 50000, 2), -- Telegram
('Reaccionar a un mensaje', 1000, 3), -- Messenger
('Enviar un GIF', 300000, 3), -- Messenger
('Editar un tweet', 5000, 4), -- X
('Seguir a un usuario', 2000, 4), -- X
('Ver historia', 3000000, 5), -- Instagram
('Enviar un mensaje privado', 5000, 5), -- Instagram
('Reaccionar a una publicación', 5000, 6), -- Facebook
('Compartir un enlace', 10000, 6), -- Facebook
('Subir un video de 10 minutos', 100000000, 7), -- YouTube
('Comentar un video', 5000, 7), -- YouTube
('Hacer una transmisión en vivo', 50000000, 8), -- TikTok
('Descargar un video', 20000000, 8), -- TikTok
('Descargar un archivo de 10 MB', 10000000, 9), -- Google Drive
('Compartir un enlace de acceso', 5000, 9), -- Google Drive
('Sincronizar archivos', 5000000, 10), -- OneDrive
('Ver historial de versiones', 10000, 10), -- OneDrive
('Eliminar un archivo', 5000, 11), -- Dropbox
('Restaurar un archivo eliminado', 5000, 11), -- Dropbox
('Cancelar una compra', 20000, 12), -- Amazon
('Dejar una reseña de producto', 5000, 12), -- Amazon
('Agregar producto a favoritos', 5000, 13), -- Mercado Libre
('Solicitar reembolso', 20000, 13), -- Mercado Libre
('Vincular cuenta bancaria', 10000, 14), -- PayPal
('Ver historial de transacciones', 5000, 14), -- PayPal
('Actualizar una aplicación', 5000000, 15), -- Play Store
('Comentar una aplicación', 5000, 15), -- Play Store
('Ver lista de apps en tendencia', 5000, 16), -- App Store
('Descargar una actualización', 20000000, 16), -- App Store
('Agregar a lista "Ver más tarde"', 5000, 17), -- Netflix
('Cambiar la calidad de reproducción', 5000, 17), -- Netflix
('Ver trailer de película', 5000000, 18), -- Disney+
('Agregar perfil nuevo', 5000, 18), -- Disney+
('Ver una película en grupo', 5000000, 19), -- HBO Max
('Configurar subtítulos', 5000, 19), -- HBO Max
('Crear una lista de reproducción', 5000, 20), -- Spotify
('Descargar una canción', 5000000, 20), -- Spotify
('Seguir a un artista', 5000, 21), -- Apple Music
('Compartir una canción', 5000, 21), -- Apple Music
('Ver el pronóstico del tiempo', 10000, 22), -- Google Chrome
('Traducir una página web', 50000, 22), -- Google Chrome
('Hacer búsqueda por voz', 20000, 23), -- Bing
('Configurar búsqueda segura', 5000, 23), -- Bing
('Marcar correo como spam', 5000, 24), -- Gmail
('Programar un correo', 10000, 24), -- Gmail
('Crear una regla de filtrado', 5000, 25), -- Outlook
('Adjuntar imagen a correo', 300000, 25), -- Outlook
('Responder', 5000, 26),
('Aplicar a trabajo', 1500000, 27),
('Grabar reunión', 50000000, 28),
('Comunicación por minuto con la red', 10000, 29),
('Órdenes en línea', 500000, 30),
('Enviar mensaje', 1024, 31),
('Ver una hora de transmisión', 5000000000, 32),
('Realizar pregunta', 50000, 33),
('Enviar un snap', 3000000, 34);
"""

bienvenida = """¡Bienvenido al sistema de registro de tareas!

Este programa indicará el tamaño total resultante de cierta cantidad de tareas, 
de multiples tareas de múltiples aplicaciones

Para comenzar seleccione:"""
seleccion = """1. Ingresar un registro de tarea
2. Realizar el calculo del tamaño total
3. Eliminar el registro actual
4. Eliminar UN registro actual
5. Mostrar el registro actual
6. Salir\n"""

insert = """insert into registro(ID_APP, ID_TASK, CANTIDAD) VALUES (?, ?, ?)"""

select_lista_app = "select id_app, nombre from aplicacion"

select_lista_tarea = "select ID_TASK, NOMBRE, PESO FROM TAREA WHERE ID_APP = (?)"

eliminar_reg = "DELETE FROM REGISTRO"

select_lista_reg = """select
A.ID_REGISTRO,
APLICACION.NOMBRE AS APLICACION,
TAREA.NOMBRE AS TAREA,
TAREA.PESO AS BYTES,
A.CANTIDAD
FROM REGISTRO A
INNER JOIN APLICACION ON A.ID_APP = APLICACION.ID_APP
INNER JOIN TAREA ON A.ID_TASK = TAREA.ID_TASK"""

eliminar_un_reg = """DELETE FROM REGISTRO WHERE ID_REGISTRO = ?"""


def clasificacion(c: float):
    mag = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    cant = c
    m = 0
    try:
        for i in range(0, len(mag)):
            if (c / 10 ** (3 * i)) >= 1000:
                m = i + 1
                cant = (c / 10 ** (3 * (i + 1)))
        return f"{cant:.2f} {mag[m]}"
    except IndexError:
        cant = (c / 10 ** (3 * (len(mag) - 1)))
        m = len(mag) - 1
        return f"{cant:.2f} {mag[m]}"
