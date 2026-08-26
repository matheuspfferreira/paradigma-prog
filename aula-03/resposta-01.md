1. Fonte da Gramática
Optaremos pela linguagem Rust, uma linguagem de programação multiparadigma, compilada e desenvolvida originalmente pela Mozilla.

Rust é projetada com foco em segurança, concorrência e desempenho (https://pt.wikipedia.org/wiki/Rust_(linguagem_de_programação)).

Para uma descrição oficial da linguagem, é recomendado utilizar a documentação oficial do Rust (https://doc.rust-lang.org/stable/).

A gramática oficial do Rust utiliza uma notação gramatical própria, baseada em conceitos de EBNF, mas com extensões relacionadas ao processo de parsing e inspiradas em PEG (Parsing Expression Grammar).

Por exemplo, a notação utiliza construções semelhantes às encontradas em EBNF:

| — representa uma alternativa;
? — indica zero ou uma ocorrência;
* — indica zero ou mais ocorrências;
+ — indica uma ou mais ocorrências;
( ... ) — indica agrupamento.
Além dessas construções, a notação do Rust possui operadores específicos relacionados ao parsing. Um exemplo é:

^ — chamado de hard cut, indica um ponto após o qual o parser não deve voltar atrás (backtrack) para tentar uma alternativa diferente.
Assim, a notação da gramática de Rust não pode ser caracterizada simplesmente como BNF, EBNF ou PEG puro.