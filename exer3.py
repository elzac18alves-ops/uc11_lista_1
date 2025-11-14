from biblioteca.matematica import soma

# validação de cenários de teste
assert soma( 4, 5) == 9, "cenário 1 falhou." 
assert soma( 10, 15) == 25, "cenário 2 falhou."
assert soma( -3, "7") == 4, "cenário 4 falhou."
 
 # Imprimir mensagem apenas se todos os casos de testes forem satisfeitos
print("Todos os testes passaram com sucesso!")

