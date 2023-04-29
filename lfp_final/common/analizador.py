class Scanner:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_pos = 0
    
    def scan(self):
        tokens = []
        while self.current_pos < len(self.input_string):
            if self.input_string[self.current_pos:].startswith("CrearBD"):
                tokens.append("use('" + self.get_database_name() + "');")
            elif self.input_string[self.current_pos:].startswith("EliminarBD"):
                tokens.append("db.dropDataBase('" + self.get_database_name_for_deletion() + "');")
            elif self.input_string[self.current_pos:].startswith("CrearColeccion"):
                tokens.append("db.createCollection(" + self.get_collection_name() + ");")
            elif self.input_string[self.current_pos:].startswith("EliminarColeccion"):
                tokens.append("db." + self.get_collection_name_for_deletion() + ".drop();")
            elif self.input_string[self.current_pos:].startswith("BuscarTodo"):
                tokens.append("db." + self.get_buscarTodo_name() + ".find();")
            elif self.input_string[self.current_pos:].startswith("BuscarUnico"):
                tokens.append("db." + self.get_buscarTodo_name() + ".findOne();")
            else:
                raise ValueError("Token no reconocido")
            self.skip_to_next_token()
        resultado = "\n".join(tokens)
        return resultado
    
    def get_database_name(self):
        self.current_pos += len("CrearBD")
        self.skip_spaces()
        name = self.get_identifier()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("nueva CrearBD()"):
            raise ValueError("Sintaxis incorrecta")
        self.current_pos += len("nueva CrearBD()")
        return name
    
    def get_database_name_for_deletion(self):
        self.current_pos += len("EliminarBD")
        self.skip_spaces()
        name = self.get_identifier()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta para EliminarBD")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("nueva EliminarBD()"):
            raise ValueError("Sintaxis incorrecta para nueva EliminarBD()")
        self.current_pos += len("nueva EliminarBD()")
        return name
    
    def get_collection_name(self):
        self.current_pos += len("CrearColeccion")
        self.skip_spaces()
        name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta para CrearColeccion")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+5] != "nueva":
            raise ValueError("Sintaxis incorrecta para CrearColeccion")
        self.current_pos += len("nueva")
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("CrearColeccion("):
            raise ValueError("Sintaxis incorrecta para CrearColeccion")
        self.current_pos += len("CrearColeccion(")
        self.skip_spaces()  
        collection_name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ")":
            raise ValueError("Sintaxis incorrecta para CrearColeccion")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ";":
            raise ValueError("Sintaxis incorrecta para CrearColeccion")
        self.current_pos += 1
        return collection_name
    
    def get_collection_name_for_deletion(self):
        self.current_pos += len("EliminarColeccion")
        self.skip_spaces()
        name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta para EliminarColeccion")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+5] != "nueva":
            raise ValueError("Sintaxis incorrecta para EliminarColeccion")
        self.current_pos += len("nueva")
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("EliminarColeccion("):
            raise ValueError("Sintaxis incorrecta para EliminarColeccion")
        self.current_pos += len("EliminarColeccion(")
        self.skip_spaces()  
        collection_name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ")":
            raise ValueError("Sintaxis incorrecta para EliminarColeccion")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ";":
            raise ValueError("Sintaxis incorrecta para EliminarColeccion")
        self.current_pos += 1
        return collection_name

    def get_buscarTodo_name(self):
        self.current_pos += len("BuscarTodo")
        self.skip_spaces()
        name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta para BuscarTodo")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+5] != "nueva":
            raise ValueError("Sintaxis incorrecta para BuscarTodo")
        self.current_pos += len("nueva")
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("BuscarTodo("):
            raise ValueError("Sintaxis incorrecta para BuscarTodo")
        self.current_pos += len("BuscarTodo(")
        self.skip_spaces()  
        collection_name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ")":
            raise ValueError("Sintaxis incorrecta para BuscarTodo")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ";":
            raise ValueError("Sintaxis incorrecta para BuscarTodo")
        self.current_pos += 1
        return collection_name
    
    def get_buscarUnico_name(self):
        self.current_pos += len("BuscarUnico")
        self.skip_spaces()
        name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != "=":
            raise ValueError("Sintaxis incorrecta para BuscarUnico")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+5] != "nueva":
            raise ValueError("Sintaxis incorrecta para BuscarUnico")
        self.current_pos += len("nueva")
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or not self.input_string[self.current_pos:].startswith("BuscarUnico("):
            raise ValueError("Sintaxis incorrecta para BuscarUnico")
        self.current_pos += len("BuscarUnico(")
        self.skip_spaces()  
        collection_name = self.get_identifier2()
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ")":
            raise ValueError("Sintaxis incorrecta para BuscarUnico")
        self.current_pos += 1
        self.skip_spaces()
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos:self.current_pos+1] != ";":
            raise ValueError("Sintaxis incorrecta para BuscarUnico")
        self.current_pos += 1
        return collection_name

    def get_quoted_string(self):
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos] not in ('"', "'"):
            raise ValueError("Sintaxis incorrecta")
        quote_char = self.input_string[self.current_pos]
        self.current_pos += 1
        string_start = self.current_pos
        while self.current_pos < len(self.input_string) and self.input_string[self.current_pos] != quote_char:
            self.current_pos += 1
        if self.current_pos >= len(self.input_string) or self.input_string[self.current_pos] != quote_char:
            raise ValueError("Sintaxis incorrecta")
        string_end = self.current_pos
        self.current_pos += 1
        return self.input_string[string_start:string_end]
        
    def get_identifier(self):
        identifier = ""
        while self.current_pos < len(self.input_string) and (self.input_string[self.current_pos].isalnum() or self.input_string[self.current_pos] == "_"):
            identifier += self.input_string[self.current_pos]
            self.current_pos += 1
        if not identifier:
            raise ValueError("Sintaxis incorrecta")
        return identifier
    
    def get_identifier2(self):
        identifier = ""
        while self.current_pos < len(self.input_string) and (self.input_string[self.current_pos].isalnum() or self.input_string[self.current_pos] == "_" or self.input_string[self.current_pos] == '"'):
            identifier += self.input_string[self.current_pos]
            self.current_pos += 1
        if not identifier:
            raise ValueError("Sintaxis incorrecta")
        if self.current_pos < len(self.input_string) and self.input_string[self.current_pos] == "(":
            self.current_pos -= 1
        return identifier
    
    def skip_spaces(self):
        while self.current_pos < len(self.input_string) and self.input_string[self.current_pos].isspace():
            self.current_pos += 1
    
    def skip_to_next_token(self):
        while self.current_pos < len(self.input_string) and not self.input_string[self.current_pos].isspace():
            self.current_pos += 1
        self.skip_spaces()
        
    def tokens(self):
        return self.scan()
