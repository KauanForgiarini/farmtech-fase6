# Interpretação do enunciado e preparação

É a continuidade narrativa da FarmTech Solutions. A empresa está expandindo para visão computacional. A implementação desta fase é nova e não integra Oracle, sensores, dashboard ou modelos das fases anteriores.

O pacote contempla as Entregas 1 e 2. ESP32/Webcam e transfer learning com segmentação são opções extras sem nota.

Prazo informado: 13/10/2026 às 23h59. Até três dias de atraso: teto de 70% da nota. Não fazer commits depois da entrega final.

## Estado atual

- Dupla: Kauan Maciel Forgiarini (RM 574005) e Wagner Adriano de Souza Silva Junior (RM 569431).
- Dataset: 80 imagens, com 64 treino, 8 validação e 8 teste.
- Classes: pessoa e carro.
- YOLO 30 e YOLO 60 treinados.
- YOLO padrão avaliado como baseline.
- CNN do zero treinada por 60 épocas; melhor validação na época 20.
- Avaliação final e prints das oito imagens executados.
- Discussão crítica consolidada em `RESULTADOS.md`.
- Vídeo: pendente.

## Resultados conferidos

### Validação
- YOLO 30: mAP50–95 = 0,244.
- YOLO 60: mAP50–95 = 0,231.
- Modelo selecionado antes do teste: YOLO 30.

### Teste por imagem
- YOLO padrão: 87,5%.
- YOLO 30: 100% (8/8).
- YOLO 60: 87,5% (7/8, uma abstenção).
- CNN do zero: 0% (0/8).

### Detecção no teste
- YOLO 30: precision 0,912; recall 0,556; mAP50 0,609; mAP50–95 0,455.
- YOLO 60: precision 0,557; recall 0,611; mAP50 0,570; mAP50–95 0,378.

## Revisão antes de enviar

- [x] RM 574005 no notebook e no nome do arquivo.
- [x] 64 imagens treino, 8 validação, 8 teste.
- [x] Classes e rótulos YOLO validados pelo notebook.
- [x] Todos os códigos executados sem erro.
- [x] Treinamentos de 30 e 60 épocas completos.
- [x] Comparação de precisão, erros, tempos e facilidade das abordagens.
- [x] Gráficos de perda e prints dos oito testes gerados.
- [x] Discussão crítica com resultados reais.
- [x] Repositório público criado.
- [x] README atualizado com os resultados.
- [ ] Salvar/confirmar no GitHub o notebook executado com as saídas visíveis.
- [ ] Publicar e inserir no README o link público do dataset/Drive.
- [ ] Conferir o arquivo de fontes/origens e permissões de leitura.
- [ ] Conferir se Wagner está incluído no grupo no portal da FIAP.
- [ ] Vídeo não listado de até cinco minutos.
- [ ] Inserir o link do vídeo no README.
- [ ] Conferir todos os links em janela anônima.
- [ ] Enviar o link do GitHub no portal.
- [ ] Não fazer commits depois da entrega.

## Observação sobre o repositório

O repositório atual é `KauanForgiarini/farmtech-fase6`. Se o professor exigir literalmente o número/nome do grupo no nome do repositório, renomear antes da entrega e atualizar o link do Colab/README.
