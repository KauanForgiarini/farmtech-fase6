# Roteiro de demonstração — até 5 minutos

Usar somente depois de executar o notebook e substituir os trechos entre colchetes pelos resultados reais.

**0:00–0:30 — Contexto:** “Sou Kauan Maciel Forgiarini, RM [RM], do Grupo 9. Nesta fase, a FarmTech Solutions demonstra visão computacional para detectar pessoas e carros em acessos a propriedades.”

**0:30–1:10 — Dados:** mostrar as pastas do Drive, as 80 imagens, a divisão 64/8/8 e uma rotulação no Make Sense. Explicar a separação de cenas e a variação de iluminação.

**1:10–2:10 — Treinamento:** mostrar as células executadas e os gráficos de 30 e 60 épocas. Dizer “[modelo] foi selecionado pela validação, usando mAP50–95”. Explicar a diferença entre perda e acurácia. Não esperar treinamento em tempo real no vídeo.

**2:10–3:20 — Comparação:** mostrar tabela do YOLO padrão, personalizado e CNN do zero. Comentar acertos sobre oito imagens, erros, treinamento e latência. Explicar que a CNN não gera caixas e que a comparação comum é por classe da imagem.

**3:20–4:20 — Demonstração:** executar a inferência em uma imagem de teste e mostrar as caixas; apresentar também uma falha ou abstenção, se existir. Mostrar os prints salvos e as matrizes de confusão.

**4:20–4:55 — Conclusão:** explicar vantagens e limitações observadas. Destacar a amostra pequena e a necessidade de mais dados. Mostrar o README com links e encerrar.
