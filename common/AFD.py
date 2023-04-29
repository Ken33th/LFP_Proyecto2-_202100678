class AFD:
    def __init__(self):
        self.estado_actual = 'q0'
        self.salida = ''

    def transicion(self, simbolo):
        if self.estado_actual == 'q0':
            if simbolo == 'CrearBD':
                self.estado_actual = 'q1'
            elif simbolo == 'EliminarBD':
                self.estado_actual = 'q2'
            elif simbolo == 'CrearColeccion':
                self.estado_actual = 'q3'
            elif simbolo == 'EliminarColeccion':
                self.estado_actual = 'q4'
            elif simbolo == 'InsertarUnico':
                self.estado_actual = 'q5'
            elif simbolo == 'ActualizarUnico':
                self.estado_actual = 'q6'
            elif simbolo == 'EliminarUnico':
                self.estado_actual = 'q7'
            elif simbolo == 'BuscarTodo':
                self.estado_actual = 'q8'
            elif simbolo == 'BuscarUnico':
                self.estado_actual = 'q9'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q1':
            if simbolo.startswith('ejemplo'):
                self.salida = 'use(\'' + simbolo.split('=')[0].strip() + '\');'
                self.estado_actual = 'q0'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q2':
            if simbolo.startswith('elimina'):
                self.salida = 'db.dropDatabase();'
                self.estado_actual = 'q0'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q3':
            if simbolo.startswith('colec'):
                nombre_coleccion = simbolo.split('(')[1].split(')')[0].strip().replace('"', '')
                self.salida = 'db.createCollection(\'' + nombre_coleccion + '\');'
                self.estado_actual = 'q0'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q4':
            if simbolo.startswith('eliminacolec'):
                nombre_coleccion = simbolo.split('(')[1].split(')')[0].strip().replace('"', '')
                self.salida = 'db.' + nombre_coleccion + '.drop();'
                self.estado_actual = 'q0'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q5':
            if simbolo.startswith('insertadoc'):
                nombre_coleccion = simbolo.split('(')[1].split(',')[0].strip().replace('"', '')
                json_texto = simbolo.split('(", "')[-1].split('")')[0]
                self.salida = 'db.' + nombre_coleccion + '.insertOne(' + json_texto + ');'
                self.estado_actual = 'q0'
            else:
                self.estado_actual = 'qerror'
        elif self.estado_actual == 'q6':
            if simbolo.startswith('actualizadoc'):
                nombre_coleccion =
