import ply.lex as lex
reserved = {
    'default': 'DEFAULT',
    'let': 'LET',
    'void': 'VOID',
    'switch': 'SWITCH',
    'debugger': 'DEBUGGER',
    'implements': 'IMPLEMENTS',
    'protected': 'PROTECTED',
    'true': 'TRUE',
    'delete': 'DELETE',
    'this': 'THIS',
    'while': 'WHILE',
    'for': 'FOR',
    'catch': 'CATCH',
    'throw': 'THROW',
    'enum': 'ENUM',
    'interface': 'INTERFACE',
    'public': 'PUBLIC',
    'with': 'WITH',
    'break': 'BREAK',
    'try': 'TRY',
    'finally': 'FINALLY',
    'function': 'FUNCTION',
    'continue': 'CONTINUE',
    'await': 'AWAIT',
    'export': 'EXPORT',
    'null': 'NULL',
    'super': 'SUPER',
    'yield': 'YIELD',
    'case': 'CASE',
    'typeof': 'TYPEOF',
    'instanceof': 'INSTANCEOF',
    'else': 'ELSE',
    'in': 'IN',
    'class': 'CLASS',
    'extends': 'EXTENDS',
    'package': 'PACKAGE',
    'abstract': 'ABSTRACT',
    'if': 'IF',
    'var': 'VAR',
    'new': 'NEW',
    'do': 'DO',
    'return': 'RETURN',
    'const': 'CONST',
    'false': 'FALSE',
    'private': 'PRIVATE',
    'static': 'STATIC',
    'arguments': 'ARGUMENTS'
}

tokens = (
    'NUMBER',
    'STRING',
    'MAS',
    'MENOS',
    'MULTIPLICAR',
    'DIVIDIR',
    'LPAREN',
    'RPAREN',
    'ASIGNACION',
    'PORCENTAJE',
    'MAS_IGUAL',
    'MENOS_IGUAL',
    'MULTIPLICAR_IGUAL',
    'DIVIDIR_IGUAL',
    'ESTRICTA_IGUALDAD',
    'NO_ES_IGUAL',
    'MENOR_QUE',
    'MAYOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'AND',
    'OR',
    'NEGACION',
    'NUEVA_LINEA'
) + tuple(reserved.values())

# Ignorar saltos y espacios
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'
t_ignore_NEWLINE = r'\n'

# Simbolos Operadores/Delimitadores
t_NUMBER = r'\d+'
t_MENOS = r'-'
t_MAS = r'\+'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASIGNACION = r'='
t_PORCENTAJE = r'%'
t_MAS_IGUAL = r'+='
t_MENOS_IGUAL = r'-='
t_MULTIPLICAR_IGUAL = r'*='
t_DIVIDIR_IGUAL= r'/='
t_ESTRICTA_IGUALDAD = r'==='
t_NO_ES_IGUAL = r'!=='
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_AND = r'&&'
t_OR = r'OR'
t_NEGACION = r'!'

# NUEVA LINEA
def t_NEWLINE(t):
    r'\\n'
    t.value = t.value
    return t

# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_CARACTERSPECIAL(t):
    r'\\.'
    t.value = t.value
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]  # PARA REMOVER ""
    return t

# Build the lexer
lexer = lex.lex()
# Test it out
data = '''42929% IF for4sas class await != >=
22121-2 null'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)