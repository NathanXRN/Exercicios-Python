# Escreva um programa em Python para exibir o cronograma de exames. (extraia a data de exam_st_date).
from datetime import date 

exame_st_date1 = (11, 12, 2024)

exame_st_date = date(exame_st_date1[2], exame_st_date1[1], exame_st_date1[0])

format_exame_st_date = exame_st_date.strftime("%d/%m/%Y")

print(f"Data Original: {exame_st_date1}")
print(f"Data Criada: {exame_st_date}")
print(f"Data formatada: {format_exame_st_date}")