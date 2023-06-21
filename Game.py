# primeiro criamos as variaveis
# depoois a logica

# VARIAVEL QUE PRECISO DESCOBRIR
secret_word = "giraffe"
#MEU INPUT
guess = ""
#INICIO DO PREENCHIMENTO
guess_count = 0
#LIMITE
guess_limit = 3
#PARA SABER FALSE OU TRUE
guess_fxf = False

while guess != secret_word and not(guess_fxf):
    if guess_count < guess_limit:
       guess = input("seja criativo...")
       guess_count += 1
    else:
        guess_fxf = True
if guess_fxf:
    print("Game over")
else:
    print("Uhuuuuu Parabéns")


