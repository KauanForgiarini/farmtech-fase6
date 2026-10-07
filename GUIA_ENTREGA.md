# Interpretação do enunciado e preparação

É a continuidade narrativa da FarmTech Solutions. A empresa está expandindo para visão computacional. A implementação desta fase é nova e o enunciado exige um NOVO repositório com o nome do grupo; não é pedido integrar Oracle, sensores, dashboard ou modelos das fases anteriores.

O cabeçalho introdutório é ambíguo, mas o barema explicita “Entregas 1 e 2” como obrigatórias. Assim, o pacote contempla ambas. ESP32/Webcam e transfer learning com segmentação são opções extras sem nota.

Prazo informado: 13/10/2026 às 23h59. Até três dias de atraso: teto de 70% da nota. Não fazer commits depois da entrega. Grupo mostrado no portal: Grupo 9, apenas Kauan cadastrado. Se houver colega, regularizar o grupo no portal antes de enviar.

## O que falta fornecer

- Dupla confirmada: Kauan (RM 574005) e Wagner (RM 569431). Conferir inclusão dos dois no portal.
- 80 imagens e rótulos YOLO produzidos no Make Sense AI (ou um dataset existente que cumpra o enunciado).
- Conteúdo do capítulo 3 se for necessário reproduzir exatamente a implementação de “YOLO tradicional” da disciplina. O pacote usa YOLOv8n padrão como baseline, interpretação que precisa ser conferida com o material da aula.
- Endereço do novo GitHub e links do Colab/Drive.
- Vídeo real da demonstração, até cinco minutos.

## Dataset

Classes iniciais: pessoa e carro. Não misturar as duas classes-alvo na mesma foto, porque a CNN classifica uma classe por imagem. Podem existir várias pessoas em uma imagem ou vários carros em outra; rotular todas as instâncias da classe. Se quiser outras classes, ajustar CLASSES e o mapeamento COCO do baseline — não basta renomear os rótulos.

No Drive, criar FarmTech_Fase6/dataset. Dentro, criar images/train, images/val, images/test, labels/train, labels/val e labels/test. Colocar 32 fotos de cada classe no treino, quatro de cada na validação e quatro de cada no teste. Os TXT devem ter o mesmo nome-base das fotos.

Registrar origem e licença em fontes.csv. Fotografias próprias de cenas distintas reduzem risco de sobreposição com o treinamento prévio do COCO. Não usar a mesma cena em splits diferentes. A validação automática detecta duplicatas exatas, não fotografias quase iguais; revisar manualmente.

## Revisão antes de enviar

- [x] RM 574005 no notebook e no nome do arquivo.
- [ ] Arquivo de fontes e dataset completo, com permissões de leitura adequadas.
- [ ] 64 imagens treino, 8 validação, 8 teste; nenhuma cena compartilhada.
- [ ] Rótulos feitos no Make Sense e salvos no Drive.
- [ ] Todos os códigos executados, sem erros, e saídas mantidas.
- [ ] Treinamentos de 30 e 60 épocas completos.
- [ ] Comparação de precisão, erros, tempos e facilidade das três abordagens.
- [ ] Gráficos de perda e prints dos oito testes visíveis.
- [ ] Discussão crítica preenchida com os resultados reais.
- [ ] Novo repositório público, sugestão de nome: grupo-9-farmtech-fase6.
- [ ] README atualizado com nome final do notebook, Colab, dataset e vídeo.
- [ ] Vídeo não listado com duração de até cinco minutos.
- [ ] Links conferidos em janela anônima.
- [ ] Link do GitHub enviado no portal até o prazo.
- [ ] Nenhum commit depois de enviar.

Não há dataset, pesos treinados, números experimentais ou vídeo incluídos neste pacote. Estes itens dependem da preparação e execução real. Não presumir que o código passou por treinamento completo: houve apenas validação sintática/estrutural local.

## Identificação conferida no GitHub

O README da Fase 5 informa Kauan Maciel Forgiarini, RM 574005, e Wagner Adriano de Souza Silva Junior, RM 569431, no Grupo 7 daquela fase. O enunciado atual mostra Grupo 9 com somente Kauan. A identificação desta entrega segue o portal atual; Wagner foi confirmado pelo Kauan como integrante desta fase em 07/10/2026. Conferir o cadastro da dupla no portal.

## Criar o novo repositório

Repositório criado pelo usuário: https://github.com/KauanForgiarini/farmtech-fase6 (público). O enunciado pede o nome do grupo no nome do repositório; para aderência literal, renomear para grupo-9-farmtech-fase6 e atualizar os links do Colab. Não usar o repositório da Fase 5 para esta nova entrega.
