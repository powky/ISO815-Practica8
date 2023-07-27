import cx_Oracle
import os
import sys

def insert_into_documentos(factura, condicion, cliente, fecha, monto, estado):
    os.environ['TNS_ADMIN'] = '/path/to/instantclient_19_8/network/admin'
    connection = cx_Oracle.connect('user', 'pass', 'tns')
    cursor = connection.cursor()

    try:
        insert_sql = "INSERT INTO documentos (factura, Condicion, Cliente, fecha, Monto, Estado) VALUES (:1, :2, :3, :4, :5, :6)"
        data = (factura, condicion, cliente, fecha, monto, estado)

        cursor.execute(insert_sql, data)
        connection.commit()
        print("¡Guardado correctamente!")
    except cx_Oracle.Error as error:
        print("Error:", error)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso: python insert.py factura condicion cliente fecha monto estado")
    else:
        factura = int(sys.argv[1])
        condicion = sys.argv[2]
        cliente = sys.argv[3]
        fecha = sys.argv[4]
        monto = float(sys.argv[5])
        estado = sys.argv[6]

        insert_into_documentos(factura, condicion, cliente, fecha, monto, estado)