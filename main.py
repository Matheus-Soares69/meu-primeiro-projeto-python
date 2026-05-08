#o programa deve pedir o nome, 3 notas / calcular a média / mostrar situação( usando float(), if, elif, else)

aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = ( nota1 + nota2 + nota3 ) / 3

maior = max( nota1, nota2, nota3)
menor = min( nota1, nota2, nota3)

print(f"Aluno {aluno} teve a média {media:.1f}")

if media >=7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

print(f"A maior nota foi: {maior}")
print(f"A menor nota foi: {menor}")








