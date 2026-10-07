# Roteiro de demonstração — até 5 minutos

Roteiro atualizado com os resultados reais. O vídeo pode ser apresentado pelo Wagner ou pelo Kauan.

**0:00–0:30 — Contexto**  
“Somos Kauan Maciel Forgiarini, RM 574005, e Wagner Adriano de Souza Silva Junior, RM 569431, do Grupo 9. Nesta fase, a FarmTech Solutions aplica visão computacional para detectar pessoas e carros.”

**0:30–1:05 — Dataset**  
Mostrar a pasta do Drive e explicar que foram utilizadas 80 imagens: 64 para treino, 8 para validação e 8 para teste, sempre balanceadas entre pessoa e carro. Mostrar rapidamente uma imagem e seu rótulo.

**1:05–2:00 — YOLO personalizado**  
Mostrar os gráficos de 30 e 60 épocas. Explicar que o modelo foi escolhido pela validação antes de olhar o teste.  
- YOLO 30: mAP50–95 de validação = 0,244.  
- YOLO 60: mAP50–95 de validação = 0,231.  
Por isso, o YOLO 30 foi selecionado.

**2:00–3:05 — Comparação dos modelos**  
Mostrar a tabela de comparação por imagem:
- YOLO padrão: 87,5% (7/8);
- YOLO 30: 100% (8/8);
- YOLO 60: 87,5% (7/8), com uma abstenção;
- CNN do zero: 0% (0/8).

Comentar que a CNN teve melhor validação na época 20 e depois apresentou sinais de sobreajuste. O conjunto de teste é muito pequeno: cada erro altera a acurácia em 12,5 pontos percentuais.

**3:05–3:50 — Detecção**  
Mostrar a tabela de detecção:
- YOLO 30: precision 0,912; recall 0,556; mAP50 0,609; mAP50–95 0,455.
- YOLO 60: precision 0,557; recall 0,611; mAP50 0,570; mAP50–95 0,378.

Comentar que o YOLO 30 teve melhor resultado geral, embora o YOLO 60 tenha recall um pouco maior.

**3:50–4:30 — Evidências visuais**  
Mostrar duas ou três das oito imagens processadas e as caixas previstas. Se possível, mostrar uma situação mais difícil. Explicar que o modelo localizou carros melhor do que pessoas neste pequeno teste.

**4:30–4:55 — Conclusão**  
“A personalização com 30 épocas apresentou o melhor equilíbrio neste experimento. Porém, 80 imagens são insuficientes para afirmar desempenho em produção. O próximo passo seria ampliar o dataset, usar imagens próprias mais variadas e repetir o experimento com diferentes sementes.”

**4:55–5:00 — Encerramento**  
Mostrar rapidamente o README com os links do notebook, dataset e vídeo.
