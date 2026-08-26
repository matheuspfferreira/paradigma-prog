### 1. A genealogia das linguagens não é uma escada de progresso. Explique essa afirmação e apresente dois fatores históricos que fazem uma linguagem influenciar outra sem necessariamente substituí-la.

A afirmação de que a genealogia das linguagens de programação não é uma “escada de progresso” está correta porque o desenvolvimento das linguagens não ocorre de forma linear, em que uma linguagem nova necessariamente substitui e torna obsoleta sua antecessora. Na realidade, diferentes linguagens podem continuar sendo utilizadas ao mesmo tempo, enquanto conceitos, recursos e características de uma linguagem são incorporados ou adaptados por outras.

É apresentado por Robert Sebesta, uma genealogia na qual é possível observar que várias linguagens surgiram a partir da influência de linguagens anteriores. Por exemplo, linguagens como Java, C#, ANSI C e Python possuem, de diferentes maneiras, influências de linguagens que as antecederam.

O gráfico mostrado por Sebesta demonstra relações históricas entre linguagens como FORTRAN I e FLOW-MATIC, evidenciando que a evolução ocorre por ramificações e influências, e não simplesmente pela substituição de uma linguagem por outra.
O primeiro fator histórico que explica isso é a incorporação de conceitos e características de linguagens anteriores. Quando uma nova linguagem é criada, seus projetistas podem aproveitar ideias que já foram testadas e consideradas úteis em outras linguagens. Dessa forma, uma linguagem antiga pode continuar existindo enquanto seus conceitos são reutilizados em uma linguagem mais recente.
O segundo fator é a necessidade de compatibilidade e continuidade histórica. Linguagens que já possuem programas, bibliotecas, profissionais e sistemas desenvolvidos criam um forte motivo para continuarem sendo utilizadas.

---

### 2. Plankalkül não foi implementada em sua época. Ainda assim, por que ela é relevante para a história das linguagens? Cite três recursos antecipados por seu projeto e explique o valor de um deles.

O Plankalkül é relevante para a história das linguagens de programação porque, apesar de ter sido projetado por Konrad Zuse em 1945 e nunca ter sido implementado em sua época, seu projeto já apresentava diversos recursos que posteriormente se tornariam comuns em linguagens de programação. Além disso, sua descrição só foi publicada em 1972, o que significa que muitas de suas ideias permaneceram desconhecidas por vários anos. Sebesta destaca, portanto, o caráter bastante avançado do Plankalkül para o período em que foi concebido.

Três recursos antecipados pelo Plankalkül foram:
1.	Números de ponto flutuante, inclusive utilizando uma representação com complemento de dois e o esquema de “bit oculto”;

2.	Vetores (arrays) e registros (records), sendo possível inclusive utilizar registros aninhados;

3.	Invariantes ou asserções, representadas por expressões matemáticas que indicavam quais relações entre as variáveis deveriam ser verdadeiras durante a execução do programa.

---

### 7. COBOL foi desenhada para processamento comercial. Mostre como domínio e público influenciaram sua legibilidade, seus registros e sua relação com FLOW-MATIC.

O domínio e o público orientaram os desenvolvedores da linguagem COBOL em dois (2) pontos principais: utilização máxima do inglês (legibilidade por usuários não-técnicos), fácil de utilizar (mesmo sendo menos poderosa computacionalmente). Além disso, no período, estavam surgindo outras iniciativas de desenvolvimento de linguagens de programação para aplicações comerciais, partindo de empresas como: RCA e Sylvania. Sendo assim, o levantamento de informações e características estruturas da linguagem COBOL foram feitos rapidamente, com intuito de acelerar o desenvolvimento e criação de projetos baseados nessa tecnologia universal. Quanto à relação com o FLOW-MATIC, essa é uma tecnologia de notação de matemática para execução de instruções por computadores. Na época, Grace Hopper sugeriu que, ao invés de utilizar notação matemática para solicitar operações às máquinas, processamentos de dados poderiam ser orquestrados por sentenças em inglês. Durante o processo de aceitação dessa abordagem, foram feitos testes de compilação e execução de pequenos programas usando termos-chaves em inglês. Posteriormente, essa abordagem foi utilizada na criação da linguagem COBOL.

---

### 8. Compare Basic e PL/I como respostas ao desejo de ampliar o acesso ou o alcance da programação. Qual compromisso de projeto aparece em cada caso?

Baseado no livro de Sebesta, para ampliar o acesso a programação, Basic foi criado com o objetivo de ser fácil para estudantes que não estudavam ciências básicas, amigável, ágil para resolver os deveres e considerar o tempo do usuário mais que o tempo do computador. Já o PL/I buscava ampliar o alcance da programação em relação às áreas de aplicação, reunindo em uma única linguagem recursos para aplicações científicas, comerciais e de sistemas.  
O compromisso de projeto de Basic foi priorizar a simplicidade e ser fácil de aprender, mesmo tornando a linguagem limitada e com problemas de legibilidade e confiabilidade, enquanto o PL/I fez o oposto priorizando a abrangência de áreas e a versatilidade, possuindo muitos recursos de diferentes linguagens, porém diversas construções passaram a ser consideradas deficientes devido a forma que fazia tratamento de exceções e ponteiros, por exemplo.

---

### 9. APL, SNOBOL e SIMULA 67 seguiram direções distintas. Associe cada linguagem ao seu foco e identifique uma contribuição duradoura de cada uma.

-> Com base na evolução das principais linguagens de programação descritas pelo autor, APL, SNOBOL e SIMULA67 de fato tomaram rumos tecnológicos completamente distintos. A associação de cada uma ao seu foco e sua respectíva contribuição duradoura é a seguinte: 

##### APL (A programming language):
- Seu foco original: Ela foi desenvolvida por Kenneth E. Iverson na IBM por volta dos anos 60, ela não foi planejada inicialmente para ser uma linguagem de programação implementada, mas sim como um veículo para descrever arquiteturas de computadores. Caracteriza-se por ser uma linguagem dinãmico com tipagem e alocação dinâmica de armazenamento. 

- Contribuição: Sua grande contribuição é a inclusão de operadores extremamente poderosos voltados para operações unitárias em vetores e matrizes, isso da para a APL uma altíssima expressividade, pois permite realizar computações matemáticas complexas com programas pequenos. 

##### SNOBOL
- Foco principal: A linguagem foi projetada nos anos 60  por três pesquisadores nos Labaratórios Bell com o propósito claro e específico de fazer processamento de textos. Assim com a APL, ela compartilha uma característica de tipagem dinâmica de armazenamento. 

- Contribuição: SNOBOL foi a primeira linguagem aplamente conhecido a introduzir e popularir o pattern matching (casamento de padrões) de cadeias de caracteres de maneira integrada à linguagem. Embora tenha caído em desuso para editores de texto por ser lenta, suas operações de manipulação de strings influenciaram fortemente as linguagens de scripting modernas. 

##### SIMULA 67
- Foco principal:Desenvolvida pelos noruegueses Kristen Nygaard e Ole-Johan Dahl, o foco exclusivo de sua primeira versão (SIMULA I) era a simulação de sistemas complexos e a pesquisa operacional.

- Contribuição duradoura: Para permitir que subprogramas de simulação pudessem ser pausados e reiniciados de onde pararam (mecanismo conhecido como corrotinas), a linguagem introduziu a construção de classes. Essa inovação deu início ao conceito de abstração de dados e estabeleceu as fundações fundamentais para o surgimento da programação orientada a objetos

---

### 11. Construa uma cadeia de influência que passe por ALGOL, Pascal e C. Depois contraste essa linhagem imperativa com a proposta declarativa de Prolog.

A evolução das linguagens de programação imperativas possui uma árvore genealógica em que o ALGOL 60 atua como o ancestral comum mais significativo de sofisticação técnica. A partir dele, estabeleceu-se uma linhagem que moldou o desenvolvimento de Pascal e C:

- ALGOL 60: Introduziu conceitos revolucionários para o paradgma imperativo, como a estrutura em blocos (criação de escopos globais), subprogramas recursivos, passagem de parâmetros(por valor e nome) e vetores dinâmicos na pilha. Praticamente todas as linguagens imperativas subsequêntes herdam direta ou indiretamente suas características.

- ALGOL 60 → Pascal: Niklaus Wirth, que participou do comitê de evolução do ALGOL, propôs modificações à linguagem (como o ALGOL-W, criado em conjunto com Tony Hoare) que introduziram a estrutura de seleção múltipla case. Posteriormente, utilizando o ALGOL 60 como base de projeto direto, Wirth desenvolveu o Pascal. Pascal incorporou a estrutura case do ALGOL-W, registros similares aos de COBOL/PL/I e adotou a definição de tipos de dados definidos pelo usuário que havia sido pioneira no ALGOL 68.

- ALGOL 60 → C: Embora a linhagem sintática do C passe por seus ancestrais diretos CPL, BCPL e B, a linguagem C foi profundamente influenciada de forma direta pelo ALGOL 68. Essa herança do ALGOL 68 é claramente visível no C através do projeto de suas sentenças de controle for e switch, em seus operadores de atribuição acumulada e em seu mecanismo de tratamento de ponteiros.

#### ***Contraste: Linhagem Imperativa vs. Proposta Declarativa do Prolog:***
O contraste entre a linhagem imperativa (representada por ALGOL, Pascal e C) e a proposta declarativa (representada por Prolog) baseia-se em filosofias computacionais radicalmente opostas:

- ***Modelo Físico / Teórico:***
    - Linhagem Imperativa (ALGOL, Pascal, C):
        Baseada diretamente na arquitetura de von Neumann. As variáveis modelam as células físicas de memória, e as computações ocorrem por meio de alterações sequenciais desses estados

    - Proposta Declarativa (Prolog):
        Baseada em lógica simbólica (especificamente no cálculo de predicados de primeira ordem e nas cláusulas de Horn). Não depende de um modelo de máquina com estados físicos.

- ***Abordagem de Programação:***
    - Linhagem Imperativa (ALGOL, Pascal, C):
        Procedural (orientada a procedimentos). O programador precisa especificar detalhadamente como o computador deve processar os dados e em qual ordem exata as instruções e sentenças devem ser executadas

    - Proposta Declarativa (Prolog):
        Não procedural (declarativa). O programador não exprime o passo a passo da computação, mas define as características e a forma necessária que o resultado final deve possuir.

- ***Estrutura de Código:***
    - Linhagem Imperativa (ALGOL, Pascal, C):
        O programa é uma sequência lógica de instruções algorítmicas, atribuições e estruturas de controle (como laços while ou for).

    - Proposta Declarativa (Prolog):
        O programa é uma coleção estática de fatos (asserções que se assume verdadeiras) e regras (implicações lógicas entre proposições).

- ***Mecanismo de Execução:***
    - Linhagem Imperativa (ALGOL, Pascal, C):
        O compilador ou interpretador apenas traduz e executa as instruções e laços fornecidos pelo programador na ordem descrita.

    - Proposta Declarativa (Prolog):
        O computador utiliza um sistema de inferência lógico interno (baseado no princípio de resolução e unificação) para responder a consultas/objetivos de forma automática, buscando correspondências na base de dados.

Enquanto na linhagem imperativa o programador dita as ações passo a passo para alterar estados de memória, no Prolog o programador fornece o conhecimento lógico sobre o problema e deixa que o motor de inferência da linguagem encontre o caminho para a solução.

---

### 12. Modele em linguagem natural uma pequena base Prolog com dois fatos, uma regra e uma consulta. Explique por que isso representa programação lógica, não apenas armazenamento de dados.

- 1. Fatos Lógicos: 
    - Em linguagem natural:
        - "Vern é pai de Joana"
        - "Joana é mão de Jake"
    - Em prolog:
    ``father(vern, joanne).``
    ``mother(joanne, jake).``

- 2. Uma Regra (Cláusula de Horn com Cabeça): 
    - Em Linguagem Natural: 
        - "X é avô de Z se X for pai de um indivíduo Y e esse Y for mãe de Z."
    - Em Prolog:
        - ``grandparent(X, Z) :- father(X, Y), mother(Y, Z)``

- 3. Uma Consulta (Sentença-Objetivo):
    - Em Linguagem Natural:
        - "Vern é avô de Jake?"
    - Em Prolog:
        - ``grandparent(vern, jake).``

Essa estrutura representa a programação lógica por três razões fundamentais descritas pelo autor:
Capacidade de Dedução Ativa (Inferência): Em um sistema convencional de armazenamento de dados (como um SGBD relacional clássico), o sistema só consegue retornar informações que foram explicitamente gravadas nele, pois ele contém apenas fatos isolados
. Se perguntássemos a um banco de dados tradicional se "Vern é avô de Jake" sem que essa linha exata estivesse escrita nas tabelas, ele diria que não
. No Prolog, há uma capacidade de dedução predefinida
. A relação de avô nunca foi explicitamente armazenada na memória; ela é deduzida dinamicamente combinando os fatos existentes através da regra lógica
.
Uso de Resolução e Unificação: Quando a consulta grandparent(vern, jake) é executada, o sistema Prolog aciona seu motor de inferência baseado no princípio de resolução
. O sistema realiza a unificação (um casamento de padrões) para instanciar temporariamente a variável X como vern e Z como jake
. A partir daí, ele procura na base de dados se existe um Y intermediário que satisfaça as duas condições simultaneamente (father(vern, Y) e mother(Y, jake))
. Ao encontrar Y=joanne nos fatos, ele prova o objetivo como verdadeiro (yes/true)
.
Abordagem Declarativa (Não Procedural): Diferente da programação imperativa ou de consultas puras a bancos de dados, o programador Prolog não escreve o algoritmo (o passo a passo de como buscar, fazer laços ou ponteiros em memória)
. O programa é declarativo: você apenas define as regras de lógica matemática que caracterizam as relações entre as entidades e deixa que o próprio motor de inferência da linguagem determine o caminho para solucionar e responder às consultas
.

---

### 15. A primeira aplicação de Java não foi a Web, mas a Web impulsionou sua adoção. Explique como mudanças de contexto podem reposicionar uma linguagem.

Java foi inicialmente criado com o objetivo de ser utilizado em sistemas embarcados, especialmente em dispositivos eletrônicos, pois seus criadores buscavam uma linguagem que atendesse a requisitos como confiabilidade, segurança e portabilidade. Portanto, sua primeira finalidade não estava relacionada ao desenvolvimento de aplicações para a Web.

Entretanto, com o crescimento da World Wide Web, o contexto tecnológico mudou e as características do Java passaram a ser muito adequadas às novas necessidades. A capacidade de executar programas em diferentes plataformas por meio da Máquina Virtual Java (JVM), associada à portabilidade e aos mecanismos de segurança da linguagem, contribuiu para sua rápida adoção no desenvolvimento Web.

Isso demonstra que uma linguagem de programação não precisa ser criada especificamente para determinada finalidade para se tornar importante nesse contexto. Mudanças tecnológicas podem criar novas necessidades e fazer com que características que já existiam em uma linguagem sejam valorizadas em uma nova área.

---

### 17. C# foi apresentada como evolução no ambiente .NET. Compare duas decisões de C# com suas correspondentes em Java ou C++ e explique o problema que pretendem resolver.

Algumas diferenças que a linguagem C# implementa em relação à Java e C++ são: utilização mais segura de enum e adição de referências (por ponteiros) a subprogramas. Sobre a primeira diferença, a linguagem C# não transforma o enum (estrutura de valores definidos) em tipo inteiro, garantindo que não ocorra erros inesperados na execução do programa. Além disso, sobre a segunda diferença, a linguagem C# permite que ponteiros referenciem funções/métodos por meio de Delegates. Portanto, é possível implementar manipuladores de evento, controlando a execução de processos em paralelo (geralmente chamados de threads).

---

### 18. Diferencie XSLT e JSP quanto a entrada, processamento e saída. Por que ambas podem ser chamadas de linguagens híbridas de marcação e programação?

O XSLT recebe como entrada um documento XML de dados e um documento XSLT, que contém as regras de transformação. O processador procura padrões no XML e aplica as transformações definidas no XSLT. A saída é outro documento, geralmente XML, HTML ou texto. Já o JSP recebe um documento JSP, normalmente formado por HTML, Java e elementos JSTL, além de poder trabalhar com dados enviados pelo usuário, como formulários. O servidor processa o JSP, transforma-o em um servlet Java e o executa. A saída é normalmente um documento HTML enviado ao navegador.  
Ambas são chamadas de linguagens híbridas de marcação e programação porque combinam elementos de marcação, usados para estruturar o documento, com elementos que permitem realizar ações típicas de programação, como condicionais, repetições e processamento de dados. A diferença é que no XSLT essas ações são voltadas principalmente para transformar documentos XML, enquanto no JSP são usadas principalmente para gerar páginas Web dinâmicas.
