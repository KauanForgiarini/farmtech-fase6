# Grupo 9 — FarmTech Solutions — Fase 6

Projeto acadêmico de Inteligência Artificial da FIAP: demonstração de visão computacional para pessoas e carros em acessos a propriedades.

**Integrantes:**

| Nome | RM |
|---|---|
| Kauan Maciel Forgiarini | 574005 |
| Wagner Adriano de Souza Silva Junior | 569431 |

**Status:** implementação preparada, sem dataset e sem execução experimental. Não entregar como concluído neste estado.

## Acessos

- [Notebook principal](./KauanMacielForgiarini_rm574005_pbl_fase6.ipynb) — metodologia, código, avaliações e conclusões.
- [Abrir no Colab](https://colab.research.google.com/github/KauanForgiarini/farmtech-fase6/blob/main/KauanMacielForgiarini_rm574005_pbl_fase6.ipynb).
- Dataset no Google Drive: PREENCHER com link acessível à correção.
- Vídeo não listado no YouTube (até 5 minutos): PREENCHER.

## Executar

1. Ler `GUIA_ENTREGA.md` e preparar o dataset conforme a seção 2 do notebook.
2. Abrir o notebook no Colab e selecionar um ambiente com GPU.
3. Copiar `FarmTech_Fase6` para Meu Drive, conferir o caminho BASE e executar as células em ordem.
4. Analisar os resultados, preencher a discussão crítica e salvar as saídas do notebook.

O notebook cobre YOLO personalizado com 30/60 épocas, YOLO pré-treinado sem adaptação e CNN do zero. Os extras “Ir Além” estão fora deste pacote.

## Estrutura

O arquivo principal contém a implementação. `GUIA_ENTREGA.md` organiza preparação, revisão e entrega; `ROTEIRO_VIDEO.md` orienta a demonstração; `fontes.csv` registra a origem das fotografias. Após executar, os pesos, CSVs, gráficos e imagens processadas serão salvos em `FarmTech_Fase6/resultados` no Drive.

Resultados numéricos e conclusões experimentais só podem ser apresentados após a execução. O código foi verificado sintaticamente, mas o treinamento não foi validado de ponta a ponta.

## Referências

[Ultralytics](https://docs.ultralytics.com/models/yolov8/) · [Make Sense AI](https://www.makesense.ai/)

## Continuidade acadêmica

A [Fase 5](https://github.com/KauanForgiarini/farmtech-fase5-ml) abordou clusterização, regressão de produtividade e custos em nuvem. A Fase 6 mantém o contexto FarmTech e introduz um dataset de imagens e redes neurais em um repositório independente.
