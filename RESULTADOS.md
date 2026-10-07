# Resultados experimentais — FarmTech Fase 6

## Seleção do modelo

O critério definido antes do teste foi selecionar, entre os modelos personalizados, aquele com maior **mAP50–95 na validação**.

| Épocas | Precision | Recall | mAP50 | mAP50–95 | Tempo de treino |
|---:|---:|---:|---:|---:|---:|
| 30 | 0,431 | 0,379 | 0,335 | **0,244** | 73,0 s |
| 60 | 0,639 | 0,306 | 0,328 | 0,231 | 110,8 s |

Assim, o modelo de **30 épocas** foi selecionado antes de consultar o conjunto de teste.

## Comparação por imagem no teste

| Modelo | Acurácia | Erro | Precision macro | Recall macro | F1 macro | Abstenções | Inferência mediana |
|---|---:|---:|---:|---:|---:|---:|---:|
| YOLO padrão | 0,875 | 0,125 | 0,900 | 0,875 | 0,873 | 0 | 16,8 ms |
| **YOLO 30** | **1,000** | **0,000** | **1,000** | **1,000** | **1,000** | 0 | 15,6 ms |
| YOLO 60 | 0,875 | 0,125 | 1,000 | 0,875 | 0,929 | 1 | 15,0 ms |
| CNN do zero | 0,000 | 1,000 | 0,000 | 0,000 | 0,000 | 0 | 12,5 ms |

O teste tem somente oito imagens. Cada erro muda a acurácia em 12,5 pontos percentuais, portanto o resultado de 100% significa apenas 8/8 nesta amostra.

## Métricas de detecção

| Épocas | Precision | Recall | mAP50 | mAP50–95 |
|---:|---:|---:|---:|---:|
| **30** | **0,912** | 0,556 | **0,609** | **0,455** |
| 60 | 0,557 | **0,611** | 0,570 | 0,378 |

No YOLO 30, a classe carro obteve mAP50–95 de aproximadamente **0,673**, enquanto pessoa ficou em aproximadamente **0,237**.

## CNN do zero

A menor perda de validação ocorreu na **época 20**. Depois disso, a perda de treinamento tendeu a cair enquanto a perda de validação aumentou, indicando sinais de sobreajuste. No teste final, a CNN classificou incorretamente as oito imagens.

## Discussão crítica

O YOLO de 60 épocas elevou a precision na validação, mas reduziu o recall e não melhorou o mAP50–95. No teste de detecção, também ficou abaixo do YOLO 30 em precision, mAP50 e mAP50–95. Logo, aumentar o treinamento de 30 para 60 épocas não trouxe ganho geral neste experimento.

O YOLO 30 também superou o YOLO padrão na classificação das oito imagens de teste. Ainda assim, não é possível concluir que o modelo personalizado seja universalmente superior, porque o conjunto é muito pequeno e imagens públicas podem compartilhar características com dados usados em pré-treinamento.

A CNN foi mais rápida na inferência, mas seu desempenho foi insuficiente. Isso reforça a vantagem prática do uso de pesos pré-treinados quando há poucos dados disponíveis.

## Limitações

- apenas 80 imagens no total;
- somente 8 imagens de teste;
- uma única semente de treinamento;
- imagens públicas podem gerar sobreposição indireta com dados de pré-treinamento;
- diferenças de cenário, iluminação, oclusão e distância ainda são pouco representadas;
- detectar pessoa ou carro não permite inferir identidade, intenção ou invasão.

## Próximos passos

Aumentar o dataset, usar imagens próprias e independentes, variar condições de captura, repetir experimentos com diferentes sementes e avaliar em um conjunto de teste maior e separado desde o início.
