## Explicação do Código: Sistema de Reservas 📝

Este código automatiza o processo de reservas de uma pousada, validando as solicitações com base nos quartos disponíveis.

A lógica principal é a seguinte:

1.  **Leitura dos Dados**:

      * O programa primeiro lê uma linha com os números dos **quartos disponíveis** e os armazena em um `set`. A estrutura `set` é usada porque permite verificar a existência de um quarto (`in`) e removê-lo de forma muito rápida e eficiente.
      * Em seguida, lê a lista de **reservas solicitadas** pelos clientes e a mantém como uma `list`, preservando a ordem original dos pedidos.

2.  **Processamento das Reservas**:

      * O código itera sobre cada `reserva` na lista de solicitações.
      * Para cada solicitação, ele verifica se o número do quarto está no `set` de quartos disponíveis.

3.  **Confirmação e Recusa**:

      * **Se o quarto está disponível**, a reserva é **confirmada**. O número do quarto é adicionado à lista `confirmadas` e, o mais importante, é **removido** do `set` de quartos disponíveis. Isso garante que o mesmo quarto não seja reservado mais de uma vez.
      * **Se o quarto não está disponível** (seja por nunca ter existido ou por já ter sido reservado), a reserva é **recusada** e seu número é adicionado à lista `recusadas`.

4.  **Saída Formatada**:

      * Ao final do processo, o programa imprime as listas de reservas confirmadas e recusadas no formato exato exigido, com os números separados por espaços.

-----

## Testes do Código 🧪

Aqui estão três exemplos de testes para validar o funcionamento do programa em diferentes cenários.

| Teste | Entrada | Saída Esperada |
| :--- | :--- | :--- |
| **1. Cenário Padrão** | `501 502 503`\<br\>`502 504 501` | `Reservas confirmadas: 502 501`\<br\>`Reservas recusadas: 504` |
| **2. Sem Quartos Disponíveis** | *(linha em branco)*\<br\>`10 20 30`| `Reservas confirmadas:`\<br\>`Reservas recusadas: 10 20 30` |
| **3. Solicitação Duplicada** | `701 702`\<br\>`701 702 701` | `Reservas confirmadas: 701 702`\<br\>`Reservas recusadas: 701` |
