# Grupo 9 — FarmTech Solutions — Fase 6

Projeto acadêmico de Inteligência Artificial da FIAP: demonstração de visão computacional para pessoas e carros em acessos a propriedades.

**Integrantes:**

| Nome | RM |
|---|---|
| Kauan Maciel Forgiarini | 574005 |
| Wagner Adriano de Souza Silva Junior | 569431 |

**Status:** experimentos concluídos no Google Colab com GPU T4. O notebook foi executado de ponta a ponta com 80 imagens. Falta apenas consolidar os links públicos finais e inserir o vídeo de demonstração.

## Acessos

- [Notebook principal](./KauanMacielForgiarini_rm574005_pbl_fase6.ipynb)
- [Abrir no Colab](https://colab.research.google.com/github/KauanForgiarini/farmtech-fase6/blob/main/KauanMacielForgiarini_rm574005_pbl_fase6.ipynb)
- Dataset no Google Drive: **PREENCHER com link público**
- Vídeo não listado no YouTube (até 5 minutos): **PREENCHER depois que o Wagner enviar**

## Dataset

Foram utilizadas **80 imagens**, divididas em:

- treino: 64 imagens — 32 de pessoa e 32 de carro;
- validação: 8 imagens — 4 de pessoa e 4 de carro;
- teste: 8 imagens — 4 de pessoa e 4 de carro.

As imagens foram obtidas a partir do **Open Images V7** com anotações de detecção, organizadas no formato YOLO e revisadas antes da execução. O repositório inclui `preparar_dataset_openimages.py` para reproduzir a coleta e a divisão.

## Resultados principais

Na validação, o modelo personalizado de **30 épocas** foi selecionado pelo maior mAP50–95:

| Modelo | Precision | Recall | mAP50 | mAP50–95 | Treino |
|---|---:|---:|---:|---:|---:|
| YOLO 30 | 0,431 | 0,379 | 0,335 | **0,244** | 73,0 s |
| YOLO 60 | 0,639 | 0,306 | 0,328 | 0,231 | 110,8 s |

Na classificação por imagem no teste:

| Modelo | Acurácia | F1 macro | Abstenções | Inferência mediana |
|---|---:|---:|---:|---:|
| YOLO padrão | 87,5% | 0,873 | 0 | 16,8 ms |
| **YOLO 30** | **100% (8/8)** | **1,000** | 0 | 15,6 ms |
| YOLO 60 | 87,5% | 0,929 | 1 | 15,0 ms |
| CNN do zero | 0% (0/8) | 0,000 | 0 | 12,5 ms |

Na avaliação de detecção do teste:

| Modelo | Precision | Recall | mAP50 | mAP50–95 |
|---|---:|---:|---:|---:|
| **YOLO 30** | **0,912** | 0,556 | **0,609** | **0,455** |
| YOLO 60 | 0,557 | **0,611** | 0,570 | 0,378 |

O YOLO 30 apresentou mAP50–95 de aproximadamente **0,673 para carro** e **0,237 para pessoa** no teste. A CNN teve sua melhor época de validação na época 20 e mostrou sinais de sobreajuste depois desse ponto.

> O conjunto de teste contém apenas oito imagens. Cada erro altera a acurácia em 12,5 pontos percentuais, portanto os resultados não demonstram prontidão para produção.

Uma discussão mais completa está em [RESULTADOS.md](./RESULTADOS.md). A origem e o licenciamento do dataset estão documentados em [FONTES.md](./FONTES.md).

## Execução

1. Abrir o notebook no Colab e selecionar GPU.
2. Manter a pasta `FarmTech_Fase6` em `MyDrive/FarmTech_Fase6`.
3. Executar as células em ordem.
4. Os pesos, CSVs, gráficos e imagens processadas são gravados em `FarmTech_Fase6/resultados` no Drive.

O notebook compara YOLO personalizado com 30/60 épocas, YOLO pré-treinado sem adaptação e CNN construída do zero. Os extras “Ir Além” não fazem parte deste pacote.

## Referências

- [Ultralytics YOLOv8](https://docs.ultralytics.com/models/yolov8/)
- [Open Images V7](https://storage.googleapis.com/openimages/web/index.html)
- [Make Sense AI](https://www.makesense.ai/)

## Continuidade acadêmica

A [Fase 5](https://github.com/KauanForgiarini/farmtech-fase5-ml) abordou clusterização, regressão de produtividade e custos em nuvem. A Fase 6 mantém o contexto FarmTech e introduz visão computacional em um repositório independente.
