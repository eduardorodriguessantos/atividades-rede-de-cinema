# 1. Requisitos Funcionais 

RF01 - Manter Filmes: O sistema deve permitir o cadastro, edição e exclusão de filmes com título, duração e classificação indicativa.

 RF02 - Gerenciar Sessões: O sistema deve permitir criar sessões vinculando um filme a uma sala e um horário específico.

 RF03 - Venda de Ingressos: O sistema deve registrar a venda de assentos para uma determinada sessão.

 RF04 - Consulta de Programação: O sistema deve exibir para o espectador os filmes e horários disponíveis.

# 2. Regras de Negócio 
 RN01 - Disponibilidade de Sala: Não é permitido cadastrar duas sessões simultâneas na mesma sala (conflito de horário).

 RN02 - Limite de Lotação: A quantidade de ingressos vendidos para uma sessão não pode ultrapassar a capacidade total da sala.

 RN03 - Cálculo de Preço: O valor final do ingresso pode variar conforme o tipo de sala (2D, 3D ou VIP).

 RN04 - Classificação Etária: O sistema deve alertar ou restringir a venda de ingressos caso a idade do espectador seja inferior à classificação do filme.

