# Roteiro detalhado de demonstração — FarmTech Fase 6

Este roteiro foi feito para que qualquer integrante da dupla consiga gravar o vídeo mesmo sem ter acompanhado a implementação desde o início.

**Integrantes:** Kauan Maciel Forgiarini — RM 574005; Wagner Adriano de Souza Silva Junior — RM 569431.  
**Grupo:** 9.  
**Duração recomendada:** entre 4min30s e 5min.

---

## 1. Antes de gravar

### O que abrir

Deixar abertas estas abas:

1. Repositório GitHub: `KauanForgiarini/farmtech-fase6`.
2. Notebook `KauanMacielForgiarini_rm574005_pbl_fase6.ipynb`.
3. Google Drive, pasta `FarmTech_Fase6`.
4. Dentro do Drive, se possível, deixar aberta também `FarmTech_Fase6/resultados`.

### Como abrir o notebook

No GitHub, abrir:

`KauanMacielForgiarini_rm574005_pbl_fase6.ipynb`

e clicar em **Open in Colab / Abrir no Colab**, ou usar o link do README.

### Se for somente mostrar os resultados

Não é necessário treinar tudo novamente durante o vídeo. O notebook salvo já contém as saídas dos experimentos. Basta abrir, rolar pelas células e mostrar os gráficos, tabelas e imagens.

### Se quiser executar novamente

1. No Colab, ir em **Ambiente de execução > Alterar tipo de ambiente de execução**.
2. Selecionar **GPU T4**.
3. Garantir que a pasta esteja em:
   `MyDrive/FarmTech_Fase6`
4. Executar as células em ordem.
5. A primeira célula instala as bibliotecas e monta o Google Drive.
6. A segunda confirma a GPU. O esperado é:
   `Dispositivo: cuda:0`
7. A terceira valida o dataset. O esperado é:
   - treino: 32 pessoas + 32 carros;
   - validação: 4 pessoas + 4 carros;
   - teste: 4 pessoas + 4 carros.

**Importante:** para o vídeo, não vale a pena esperar os treinamentos de 30 e 60 épocas rodarem novamente. Mostre as saídas já salvas.

---

# 2. Roteiro de fala e tela

## 0:00–0:25 — Apresentação

### O que mostrar
Abrir o README do GitHub e deixar o título e os integrantes visíveis.

### Fala sugerida

“Olá, nós somos Kauan Maciel Forgiarini, RM 574005, e Wagner Adriano de Souza Silva Junior, RM 569431, do Grupo 9. Nesta fase do projeto FarmTech Solutions trabalhamos com visão computacional para reconhecer pessoas e carros em imagens de acesso a propriedades.”

“Nosso objetivo foi comparar um YOLO personalizado, treinado com 30 e 60 épocas, um YOLO padrão pré-treinado e uma CNN construída do zero.”

---

## 0:25–0:55 — Estrutura do projeto

### O que mostrar
No GitHub, mostrar rapidamente:
- README;
- notebook;
- `RESULTADOS.md`;
- `ROTEIRO_VIDEO.md`;
- script `preparar_dataset_openimages.py`.

### Fala sugerida

“O repositório reúne o notebook principal, a documentação da entrega, os resultados e um script utilizado para preparar o dataset.”

“O trabalho é uma continuação da FarmTech em termos de contexto, mas esta fase é uma implementação nova voltada para visão computacional.”

---

## 0:55–1:25 — Dataset

### O que mostrar
No Drive:
`FarmTech_Fase6/dataset/images`

Mostrar as pastas:
- `train`
- `val`
- `test`

Se der tempo, abrir uma imagem de pessoa e uma de carro.

### Fala sugerida

“O dataset utilizado possui 80 imagens, divididas de forma balanceada entre duas classes: pessoa e carro.”

“Temos 64 imagens para treinamento, 8 para validação e 8 para teste. Em cada divisão existe a mesma quantidade de imagens das duas classes.”

“Os rótulos seguem o formato YOLO, com caixas delimitadoras indicando a localização dos objetos.”

“Para evitar vazamento entre os conjuntos, as imagens foram separadas antes do treinamento e o notebook também faz uma validação automática da estrutura e dos arquivos.”

---

## 1:25–1:45 — Validação do dataset

### O que mostrar
No notebook, mostrar a tabela:

- test: 4 pessoa / 4 carro
- train: 32 pessoa / 32 carro
- val: 4 pessoa / 4 carro

### Fala sugerida

“Aqui o próprio notebook confirma que a divisão ficou correta: 32 imagens de cada classe no treino e 4 de cada classe tanto na validação quanto no teste.”

“Também são verificadas imagens duplicadas, arquivos de rótulo ausentes e coordenadas inválidas.”

---

## 1:45–2:20 — YOLO personalizado: 30 x 60 épocas

### O que mostrar
Mostrar os gráficos dos treinamentos e depois a tabela de validação.

Valores:

YOLO 30:
- precision: 0,431
- recall: 0,379
- mAP50: 0,335
- mAP50-95: 0,244
- treino: aproximadamente 73 segundos

YOLO 60:
- precision: 0,639
- recall: 0,306
- mAP50: 0,328
- mAP50-95: 0,231
- treino: aproximadamente 111 segundos

### Fala sugerida

“Foram feitos dois treinamentos independentes do YOLO, um com 30 e outro com 60 épocas.”

“O critério de escolha foi definido antes de olhar o conjunto de teste: selecionar o modelo com maior mAP50-95 na validação.”

“O modelo de 30 épocas obteve mAP50-95 de aproximadamente 0,244, enquanto o de 60 épocas ficou em aproximadamente 0,231.”

“Mesmo que o modelo de 60 épocas tenha apresentado precision maior na validação, ele não melhorou o mAP geral. Por isso o modelo escolhido foi o de 30 épocas.”

---

## 2:20–2:50 — CNN do zero

### O que mostrar
Mostrar os gráficos “Perda CNN” e “Acurácia CNN”.

Apontar:
`Melhor época CNN pela validação: 20`

### Fala sugerida

“Além do YOLO, implementamos uma CNN do zero em PyTorch, sem carregar pesos pré-treinados.”

“A melhor época pela validação foi a época 20.”

“Depois desse ponto, a perda de treinamento continuou diminuindo enquanto a perda de validação começou a aumentar, o que indica sinais de sobreajuste.”

“Isso é coerente com a principal limitação deste experimento: o dataset é muito pequeno para treinar uma rede do zero com boa capacidade de generalização.”

---

## 2:50–3:30 — Comparação final no teste

### O que mostrar
Mostrar a tabela com os quatro modelos.

Resultados por imagem:

- YOLO padrão: 87,5% — 7 de 8 imagens
- YOLO 30: 100% — 8 de 8 imagens
- YOLO 60: 87,5% — 7 de 8 imagens, com uma abstenção
- CNN do zero: 0% — 0 de 8 imagens

### Fala sugerida

“No teste final, fizemos também uma comparação comum por classificação de imagem.”

“O YOLO padrão acertou 7 de 8 imagens, correspondendo a 87,5%.”

“O YOLO personalizado de 30 épocas acertou as 8 imagens, chegando a 100% nesta pequena amostra.”

“O YOLO de 60 épocas acertou 7 de 8 e teve uma imagem sem detecção.”

“A CNN do zero não classificou corretamente nenhuma das oito imagens.”

“Esse resultado não significa que o YOLO 30 tenha 100% de acurácia em qualquer cenário. Nosso conjunto de teste possui somente oito imagens e cada erro muda a acurácia em 12,5 pontos percentuais.”

---

## 3:30–4:05 — Métricas de detecção

### O que mostrar
Mostrar a tabela:

YOLO 30:
- precision: 0,912
- recall: 0,556
- mAP50: 0,609
- mAP50-95: 0,455

YOLO 60:
- precision: 0,557
- recall: 0,611
- mAP50: 0,570
- mAP50-95: 0,378

### Fala sugerida

“Quando avaliamos especificamente a qualidade da detecção e da localização das caixas, o YOLO de 30 épocas também apresentou o melhor resultado geral.”

“Ele alcançou precision de aproximadamente 0,912, mAP50 de 0,609 e mAP50-95 de 0,455.”

“O YOLO 60 teve recall um pouco maior, mas perdeu bastante em precision e ficou abaixo no mAP50 e no mAP50-95.”

“Por isso, neste experimento, aumentar de 30 para 60 épocas não trouxe benefício geral.”

---

## 4:05–4:30 — Mostrar as imagens detectadas

### O que mostrar
No notebook ou em:
`FarmTech_Fase6/resultados/prints_teste`

Mostrar 2 ou 3 imagens com as bounding boxes.

### Fala sugerida

“Aqui podemos ver alguns exemplos das detecções produzidas pelo modelo escolhido.”

“As caixas mostram onde o modelo encontrou a pessoa ou o carro na imagem.”

“Dentro deste pequeno conjunto, a classe carro teve desempenho de localização melhor que pessoa. O mAP50-95 ficou em cerca de 0,673 para carro e 0,237 para pessoa.”

“Como existem somente quatro imagens de teste de cada classe, isso deve ser tratado apenas como uma observação deste experimento.”

---

## 4:30–4:55 — Conclusão

### O que mostrar
Voltar para `RESULTADOS.md` ou para a seção de conclusão do notebook.

### Fala sugerida

“A principal conclusão é que o YOLO personalizado com 30 épocas apresentou o melhor equilíbrio entre desempenho e custo de treinamento para este experimento.”

“O YOLO padrão também teve bom desempenho, mostrando a vantagem do uso de pesos pré-treinados quando temos poucos dados.”

“A CNN do zero apresentou sinais de sobreajuste e desempenho muito inferior no teste.”

“A principal limitação é o tamanho do dataset. Com apenas 80 imagens, esses resultados não são suficientes para afirmar que o sistema está pronto para uso real.”

“Como próximos passos, ampliaríamos o dataset, utilizaríamos mais imagens próprias, variaríamos iluminação, distância, ângulo e oclusão e repetiríamos os treinamentos com diferentes sementes.”

---

## 4:55–5:00 — Encerramento

### O que mostrar
README do GitHub.

### Fala sugerida

“O repositório contém o notebook, os resultados, a documentação e os links necessários para reprodução do projeto. Obrigado.”

---

# 3. Perguntas que podem surgir

### “Por que escolheram 30 épocas se 60 teve precision maior na validação?”

Porque o critério definido antes do teste foi o **mAP50-95**, que avalia melhor o desempenho global da detecção em diferentes limiares de IoU. O YOLO 30 teve 0,244 contra 0,231 do YOLO 60.

### “Por que a CNN foi tão mal?”

Ela foi treinada do zero usando somente 64 imagens de treinamento. O gráfico também mostra sinais de sobreajuste após a época 20. Redes treinadas do zero normalmente precisam de muito mais dados para generalizar bem.

### “O YOLO 30 realmente tem 100% de acurácia?”

Somente neste conjunto de **oito imagens**. O vídeo deve deixar isso claro. Não afirmar que o modelo possui 100% de acurácia geral.

### “Por que YOLO e CNN não são comparados diretamente por mAP?”

Porque o YOLO é um detector de objetos e produz caixas. A CNN implementada é um classificador da imagem inteira e não produz localização. Por isso foi usada uma tarefa comum de classificação por imagem para comparar os modelos.

### “Qual modelo seria usado se o projeto continuasse?”

O YOLO de 30 épocas seria o candidato desta etapa, mas antes de qualquer uso real seria necessário ampliar bastante o dataset e repetir a avaliação em dados independentes.

---

# 4. O que NÃO falar

- Não dizer que o sistema está pronto para produção.
- Não dizer que o YOLO 30 “tem 100% de precisão” de forma geral.
- Não dizer que 60 épocas necessariamente causaram overfitting no YOLO; os resultados apenas mostram que não houve ganho geral.
- Não dizer que detectar uma pessoa significa detectar invasão.
- Não afirmar que a CNN é uma arquitetura ruim; o resultado está ligado principalmente ao protocolo e à quantidade de dados.
- Não inventar quantidade de imagens além das 80 utilizadas.
