import sqlite3 as sql
import functions as q


def conectar():
    return sql.connect("HT4.db")


def crear_tablas(conn):
    with conn:
        try:
            conn.executescript(q.inicio)
        except sql.OperationalError:
            eliminar_reg(conn, 1)


def ingresar_registro(conn):
    print("\n" * 100 + "_" * 100)
    with conn:
        # tabla = ["aplicacion", "tarea"]
        # app, tk = 0, 0
        # var = [app, tk]
        # for i in range(0, 2):
        #     while True:
        #         try:
        #             resultados = conn.execute(f"SELECT * FROM {tabla[i]}")
        #             print(f"Por favor, seleccione la respectiva {tabla[i]}:")
        #             l_resultados = list(resultados)
        #             for r in l_resultados:
        #                 print(f"{r[0]}. {r[1]}")
        #             var[i] = int(input())
        #             print(len(l_resultados))
        #             if var[i]-1 not in range(0, len(l_resultados)):
        #                 print(var[i])
        #                 print("Ingrese una opción válida.")
        #             else:
        #                 break
        #         except ValueError:
        #             print("Ingrese el número que antecede a la opción\n\n")
        while True:
            app: int = lista_app(conn)
            tk = lista_tk(conn, app)
            try:
                cantidad = int(input("Ingrese la cantidad de veces que se ejecutó esta tarea: "))
                break
            except ValueError:
                print("Ingrese únicamente números enteros")
        conn.execute(q.insert, (app, tk, cantidad))


def lista_app(conn):
    with conn:
        resultados = conn.execute(q.select_lista_app)
        l_r = list(resultados)
        while True:
            try:
                print("Por favor, seleccione la respectiva aplicación: (#)")
                for r in l_r:
                    print(f"{r[0]}. {r[1]}")
                app = int(input()) - 1
                if app not in range(0, len(l_r)):
                    print("Ingrese un número válido")
                else:
                    app = l_r[app][0]
                    break
            except ValueError:
                print("Ingrese solo el número que antecede a la opción\n")
        return app


def lista_tk(conn, app: int):
    with conn:
        resultados = conn.execute(q.select_lista_tarea, (app,))
        l_r = list(resultados)
        while True:
            try:
                print("Seleccione la respectiva tarea: (#)")
                for r in range(0, len(l_r)):
                    print(f"{r+1}. {l_r[r][1]} - ({q.clasificacion(l_r[r][2])})")
                tk = int(input()) - 1
                if tk not in range(0, len(l_r)):
                    print("Ingrese una opción válida.")
                else:
                    tk = l_r[tk][0]
                    break
            except ValueError:
                print("Ingrese solo el número que antecede a la opción\n")
        return tk


def eliminar_reg(conn, modo):
    with conn:
        while True:
            if modo == 0:
                res = input("¿Está seguro que desea eliminar TODOS los registros? (Si/No)\n")
            else:
                res = input("El programa ya posee un registro, ¿Desea eliminarlo? (Si/No)\n")
            if res.lower() == 'si':
                conn.execute(q.eliminar_reg)
                print("Eliminado con éxito\n" + "_" * 100 + "\n")
                break
            elif res.lower() == 'no':
                if modo != 0:
                    print("\n" * 100)
                print("_"*100+"\n")
                break
            else:
                print("Por favor, ingrese 'Si' o 'No' únicamente")


def eliminar_un_reg(conn):
    with conn:
        while True:
            try:
                print("Indique el índice del valor a eliminar.")
                print("Para abortar la operación escriba algún texto")
                mostrar_reg(conn)
                l_r = list(conn.execute(q.select_lista_reg))
                el = int(input()) - 1
                if el not in range(0, len(l_r)):
                    print("Ingrese una opción válida.")
                else:
                    el = l_r[el][0]
                    conn.execute(q.eliminar_un_reg, (el,))
                    print("Registro eliminado con éxito\n")
                    break
            except ValueError:
                print("Ha abortado la operación\n")
                break


def mostrar_reg(conn):
    with conn:
        resultados = conn.execute(q.select_lista_reg)
        l_r = list(resultados)
        for r in range(0, len(l_r)):
            print(f"{r+1}. {l_r[r][1]} - {l_r[r][2]} [{l_r[r][4]} veces] ({q.clasificacion(l_r[r][3])})")


def suma(conn):
    total = 0
    with conn:
        l_r = list(conn.execute(q.select_lista_reg))
        print("\n" * 100 + "_" * 100)
        for r in l_r:
            print(f"{r[1]}:\n{r[2]}\n{q.clasificacion(r[3])} x {r[4]} veces = {q.clasificacion(r[3] * r[4])}\n")
            total = total + r[3] * r[4]
        print(" " * 47 + "+\n"+"_" * 50 + f"\n{q.clasificacion(total)}")
