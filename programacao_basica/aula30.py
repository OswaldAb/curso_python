
# Constantes & Variaveis

velocidade = 61 # velocidade do carro
local_carro = 99 # localização do carro

RADAR_1  = 60 # velocidade maxima
LOCAL_1 = 100 # localização do radar
RADAR_RANGE = 1 # faixa que o radar pega

carro_ultrapassou_velocidade_radar_1 = velocidade > RADAR_1
local_1_carro = local_carro >= (LOCAL_1 - RADAR_RANGE)
locar_2_carro = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_esta_no_radar_1 =  local_1_carro and locar_2_carro
    

carro_multado = carro_ultrapassou_velocidade_radar_1 and carro_esta_no_radar_1

if local_1_carro:
    print('Carro passou no radar 1')
if carro_multado:
    print('Carro foi MULTADO no radar 1')

