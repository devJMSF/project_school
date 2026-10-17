1. Aluno
Entidade: Aluno
- id: identificador único
- nome: nome completo
- cpf: documento
- data_nascimento: data de nascimento
- email: e-mail
- telefone: telefone
- data_cadastro: data do cadastro




2. Professor
Entidade: Professor
- id: identificador único
- nome: nome completo
- cpf: documento
- email: e-mail profissional
- especialidade: área de atuação
- data_contratacao: data de contratação
- ativo: indica se está ativo




3. Disciplina
Entidade: Disciplina
- id: identificador único
- nome: Matemática, Português etc.
- descricao: descrição da disciplina
- carga_horaria: total de horas




4. Turma
Entidade: Turma
- id: identificador único
- nome: 1º ano A, 2º ano B etc.
- ano_letivo: ano escolar
- turno: manhã, tarde ou noite
- capacidade: quantidade máxima de alunos




5. Matrícula
Entidade: Matricula
- id: identificador único
- aluno_id: aluno matriculado
- turma_id: turma escolhida
- data_matricula: data da matrícula
- status: ativa, trancada, cancelada ou concluída




6. Nota
Entidade: Nota
- id: identificador único
- aluno_id: aluno avaliado
- disciplina_id: disciplina avaliada
- professor_id: professor responsável
- valor: nota obtida
- tipo_avaliacao: prova, trabalho ou atividade
- data_avaliacao: data da avaliação