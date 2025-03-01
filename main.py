import databases as db
import functions as q

conn = db.conectar()
db.crear_tablas(conn)

print(q.bienvenida) 
while True:
    try:
        op: int = int(input(q.seleccion))
        if op == 1:
            db.ingresar_registro(conn)
        elif op == 2:
            db.suma(conn)
            print("¡Gracias por usar nuestro servicio!")
            if dc := (input("¿Desea salir? (Si / No) ")).lower() == 'si':
                break
            else:
                pass
        elif op == 3:
            db.eliminar_reg(conn, 0)
        elif op == 4:
            db.eliminar_un_reg(conn)
        elif op == 6:
            break
        elif op == 5:
            db.mostrar_reg(conn)
        else:
            print("Ingrese una opción válida")
    except ValueError:
        print("Ingrese el numeral que acompaña la opción")
    print("_" * 100)
