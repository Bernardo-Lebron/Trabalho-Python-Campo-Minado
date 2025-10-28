# Trabalho-Python-Campo-Minado
## Simulação de Campo Minado

Projeto acadêmico em **Python** que implementa uma simulação do clássico jogo **Campo Minado**, com geração dinâmica do mapa, posicionamento aleatório de bombas e contagem de células vizinhas.
Desenvolvido para praticar lógica de programação, uso de matrizes, tratamento de exceções e outros conceitos de programação vistos em sala de aula.

---

### Funcionalidades

1. **Criação do Campo**
   - Geração de uma matriz de tamanho definido pelo usuário.
   - Posicionamento aleatório das bombas no campo.
   - Cálculo automático do número de bombas vizinhas para cada célula.

2. **Jogabilidade**
   - O jogador escolhe coordenadas para revelar.
   - Caso revele uma bomba, o jogo termina.
   - Se todas as células seguras forem abertas, o jogador vence.

3. **Exibição do Campo**
   - O mapa é atualizado a cada jogada.
   - Células ocultas e reveladas são representadas por símbolos diferentes.

4. **Níveis de Dificuldade**
   - Quantidade de bombas varia conforme o nível escolhido.

---

### Tecnologias e Conceitos

- **Linguagem:** Python  
- **Conceitos:**  
  - Estruturas de repetição e decisão  
  - Manipulação de matrizes (listas aninhadas)  
  - Geração aleatória com `random`  
  - Funções e modularização de código  

---

### Como Executar

```bash
python campo_minado.py
