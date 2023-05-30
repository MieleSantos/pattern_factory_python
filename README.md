# pattern_factory_python

Estudando padrão de projeto Factory

## O que é?

- Uma classe é responsável por criar objetos de outros tipos
- A classe que atua como fábrica tem um objeto e métodos associados a ela, que
  permite ser chamado por clientes, passando parâmentros e os objetos do tipo desejados são criados e devolvidos ao cliente pela fábrica.

## Vantagens de usar o padrão Fábrica

- Baixo acomplamento pois a criação de um objeto pode ser independente da implementação da classe;
- O cliente não precisa conhecer a classe que cria o objeto.

  - É necessário conhecer apenas a interface, métodos e parâmentros que devem ser passados para criar os objetos do tipo desajado. Isso simplifica as implementações para o cliente

- Adiconar outra classe à fábrica para criar objetos de outro tipo pode ser facilmente implementado sem que o cliente altere o código
- A fábrica pode reutilizar objetos existentes. Por outro lado, se o cliente criar objetos diretamente, um novo objeto sempre seá criado

## Variantes do Padrão Factory

- Simples Factory

<br>Diagrama de funcionamento
![media\simples_factory.png](media\simples_factory.png)

  - Permite que as interfaces criem objetos sem expor a lógica de sua criação
- Factory Method
<br>Diagrama de funcionamento
![media\factory_method.png](media\factory_method.png)

  - Permite que as interfaces criem objetos, mas adia a decisão para que as subclasses determinem a classe para a criação do objeto
- Abstract Method
  - Uma interface para criar objetos relacionados sem especificar/expor suas classes;
    - o padrão fornece objetos de outra que, internamente, cria outros objetos

