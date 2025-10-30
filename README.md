<h1> Trabalho Python - Campo Minado </h1>

<h2> Como executar </h2>  

   Para executar o jogo, é necessário ter o **Python 3** instalado.  
   Na pasta do projeto, utilize o seguinte comando no terminal:
   
   ```bash
   python campo_minado.py
   ```

<h2> Descrição Geral </h2>  

   Este projeto consiste em uma **implementação do jogo Campo Minado em Python**, desenvolvida como parte da disciplina **Programação em Python**.  O sistema permite a criação de um campo com bombas posicionadas aleatoriamente e a interação do jogador por meio do terminal.  O objetivo é **abrir todas as posições seguras** sem acionar nenhuma bomba.
   
   O projeto foi desenvolvido com foco em:
   - **Lógica de programação**
   - **Manipulação de matrizes (listas aninhadas)**
   - **Estruturas condicionais e de repetição**
   - **Funções**
   - **Tratamento de exceções e interação via terminal**

<h2> Opções Oferecidas</h2>

   O sistema oferece opções em dois estágios: Configuração e Jogo.
   
   Configuração Inicial
   Digitar a dimensão do campo minado (MÁX: 10): Permite ao usuário definir o tamanho do tabuleiro (N x N). O valor deve ser entre 1 e 10.
   Digitar o número de bombas: Permite ao usuário definir a dificuldade, escolhendo quantas bombas estarão escondidas. O valor máximo é (N * N - 1).
   
   Menu de Ações (Durante o Jogo)
   Após a configuração, o usuário entra no loop principal do jogo, onde as seguintes opções são oferecidas:
   
   1 - Revelar uma posição:
   - O sistema solicitará que o usuário digite a linha e a coluna que deseja revelar.
   - Se a posição for uma bomba, o jogo acaba (Derrota).
   - Se a posição for segura, ela será substituída pelo número de bombas que existem nas 8 células vizinhas.
   
   2 - Marcar/Desmarcar uma bandeira:
   - O sistema solicitará a linha e a coluna onde o usuário deseja colocar ou remover uma bandeira.
   - Se a célula estiver oculta (*), ela receberá uma bandeira (M).
   - Se a célula já tiver uma bandeira (M), ela será removida e voltará a ser (*).
   
   0 - Sair do jogo:
   - Encerra a partida e finaliza a execução do script.

<h2> Principais Telas </h2>

   A interface do sistema é baseada em texto no terminal.
   
   Tela 1: Configuração Inicial
   - O usuário define o tamanho do campo e a quantidade de bombas.
     
   Tela 2: Tabuleiro Inicial e Menu de Ações
   - Após a configuração, o tabuleiro "visível" (totalmente oculto) é mostrado, seguido pelo menu de ações.
     
   Tela 3: Durante o Jogo (Após Revelar e Marcar)
   - O tabuleiro é atualizado a cada ação do jogador.
     
   Tela 4: Fim de Jogo (Derrota)
   - Ao revelar uma bomba, o jogo acaba e o mapa real é mostrado.
     
   Tela 5: Fim de Jogo (Vitória)
   - Ao marcar todas as bombas corretamente, o jogo parabeniza o usuário e mostra o mapa real.

<h2> Conclusão </h2>

   O sistema implementa uma versão funcional e simples do jogo Campo Minado para terminal, seguindo as regras básicas de revelar células e marcar bombas.
   
   Limitações
   - Interface: O jogo é restrito ao terminal, não possuindo interface gráfica. A interação é feita pela digitação de números.
   - Dimensão: O campo é limitado a um tamanho máximo de 10x10.
   - Revelação: O jogo não implementa a "revelação em cascata". Ou seja, se o usuário revelar uma célula com '0' bombas vizinhas, o jogo não revela automaticamente as células adjacentes. O usuário deve revelar cada célula manualmente.
   - Condição de Vitória: A vitória não é alcançada ao revelar todas as células seguras (como em muitas versões do Campo Minado). A vitória neste sistema é estritamente baseada em marcar com bandeiras (M) todas as células de bomba (B) e nenhuma célula segura.

<h4> Projeto desenvolvido por Bernardo Lebron – Estudante de Engenharia de Computação (CEFET-MG) </h4> 
