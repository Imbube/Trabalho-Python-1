cadastro = []

for i in range(3):
    nome = input('Digite seu nome: ').strip()
    filme = input('Digite o nome do filme: ').strip()

    while True:
        try:
            nota = float(input('Digite a nota do filme (0 a 10): '))
            if 0 <= nota <= 10:
                break  # vai fechar o looping
            else:
                print('Nota inválida! Somente aceito entre 0 a 10. Tente novamente.')
        except ValueError:
            print('Digite um número válido!')

    # mostrar os dados aqui embaixo
    cadastro.append({
        'nome': nome,
        'filme': filme,
        'nota': nota
    })
    
# aqui vai mostrar os dados finais finalmente kkkkkkk
print('\nCadastro finalizado:')
for item in cadastro:
    print(f"Nome: {item['nome']}, Filme: {item['filme']}, Nota: {item['nota']}")

