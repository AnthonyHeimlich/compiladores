# Gramática Anotada para Análise de Comandos de Jogo

Este documento descreve a gramática utilizada para processar comandos no jogo, incluindo regras de derivação e anotações semânticas.

## **Tabela de Derivação Anotada**
| Produção                | Regra | Ação Semântica |
|-------------------------|--------------------------------|-----------------------------------------------------------|
| **aposta**             | `"aposta"` jogador valor      | `aposta.val = processar_aposta(jogador.val, valor.val)`   |
| **jogador**            | `"jogador"`                  | `jogador.val = "jogador"`                                |
|                        | `"banqueiro"`                | `jogador.val = "banqueiro"`                              |
|                        | `"empate"`                   | `jogador.val = "empate"`                                 |
| **valor**              | `NUMERO`                     | `valor.val = int(NUMERO.val)`                            |
| **mao**                | `"mão"` jogador carta carta  | `mao.val = processar_mao(jogador.val, carta1.val, carta2.val)` |
| **carta**              | `STRING`                     | `carta.val = STRING.val.strip('"')`                      |
| **resultado**          | `"resultado"` jogador        | `resultado.val = processar_resultado(jogador.val)`       |
| **comando**            | `aposta`                     | `comando.val = aposta.val`                               |
|                        | `mao`                        | `comando.val = mao.val`                                  |
|                        | `resultado`                  | `comando.val = resultado.val`                            |
| **comandos**           | `comando comandos`           | `comandos.val = processar_comando(comando.val) + comandos.val` |
|                        | `comando`                    | `comandos.val = processar_comando(comando.val)`         |

## **Explicação**
- Cada produção representa uma **regra gramatical** para os comandos do jogo.
- As **ações semânticas** indicam como os valores são processados para cada regra.
- Os valores `.val` são propagados conforme as regras especificadas.

---
