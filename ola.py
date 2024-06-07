import streamlit as st
import random

# Lista de perguntas
perguntas = [
    "Como as Assembleias de Deus veem a autonomia das igrejas locais?",
    "De acordo com o Capítulo 5, como as Assembleias de Deus veem a santificação?",
    "Qual é a missão da igreja de acordo com o Capítulo 5?",
    "Qual é a posição das Assembleias de Deus em relação à inerrância das Escrituras?",
    "Como as Assembleias de Deus interpretam as Escrituras?",
    "Qual é a crença das Assembleias de Deus sobre a natureza da Trindade?",
    "Como as Assembleias de Deus entendem a obra do Espírito Santo na Trindade?",
    "Qual é a visão das Assembleias de Deus sobre a origem do pecado humano?",
    "Como as Assembleias de Deus veem a expiação de Cristo?",
    "Qual é a visão das Assembleias de Deus sobre o chamado para o ministério?",
    "Como as Assembleias de Deus veem a responsabilidade dos ministros em relação ao ensino da Palavra?",
    "De acordo com o Capítulo 5, qual é o papel do Espírito Santo na vida cristã?",
    "Como as Assembleias de Deus veem o crescimento espiritual dos crentes?",
    "Qual é a visão das Assembleias de Deus sobre a autoridade das Escrituras?",
    "Como as Assembleias de Deus veem Jesus Cristo?"
]

# Lista de alternativas e respostas corretas
alternativas = [
    ["a) As igrejas locais devem estar sujeitas a um controle centralizado",
     "b) As igrejas locais devem ter total liberdade sem nenhuma responsabilidade",
     "c) As igrejas locais devem ser autônomas em questões de governo e administração",
     "d) As igrejas locais devem ser controladas por líderes políticos"],

    ["a) A santificação é uma obra do Espírito Santo na vida dos crentes",
     "b) A santificação é um processo opcional para os crentes",
     "c) A santificação é uma obra humana baseada em boas obras",
     "d) A santificação é uma prática antiquada sem relevância moderna"],

    ["a) A missão da igreja é apenas promover seus próprios interesses",
     "b) A missão da igreja é pregar o Evangelho e fazer discípulos em todas as nações",
     "c) A missão da igreja é ajudar apenas os membros da comunidade religiosa",
     "d) A missão da igreja é uma questão secundária e não prioritária"],

    ["a) As Escrituras são suscetíveis a erros humanos",
     "b) As Escrituras são inerrantes em questões espirituais, mas não em questões históricas",
     "c) As Escrituras são apenas parcialmente inspiradas e sujeitas a interpretação humana",
     "d) As Escrituras são inerrantes em todas as suas afirmações"],

    ["a) As Escrituras devem ser interpretadas literalmente em todos os casos",
     "b) As Escrituras devem ser interpretadas somente à luz da tradição religiosa",
     "c) As Escrituras devem ser interpretadas apenas por líderes religiosos autorizados",
     "d) As Escrituras devem ser interpretadas à luz do contexto histórico, cultural e literário"],

    ["a) A Trindade é composta por três pessoas divinas em uma única essência",
     "b) A Trindade é composta por três deuses distintos",
     "c) A Trindade é uma invenção teológica sem base bíblica",
     "d) A Trindade é uma metáfora para descrever diferentes aspectos de Deus"],

    ["a) O Espírito Santo é uma força impessoal",
     "b) O Espírito Santo é uma manifestação temporária de Deus",
     "c) O Espírito Santo é uma pessoa divina ativa na redenção e na santificação",
     "d) O Espírito Santo é irrelevante para a compreensão da Trindade"],

    ["a) O pecado humano é apenas um conceito psicológico",
     "b) O pecado humano é inerente à condição humana",
     "c) O pecado humano é uma ilusão sem base na realidade",
     "d) O pecado humano é uma escolha voluntária contrária à vontade de Deus"],

    ["a) A expiação de Cristo é uma teoria ultrapassada sem relevância",
     "b) A expiação de Cristo é uma obra parcial para alguns indivíduos",
     "c) A expiação de Cristo é uma obra completa e suficiente para toda a humanidade",
     "d) A expiação de Cristo é uma invenção teológica sem base nas Escrituras"],

    ["a) O chamado para o ministério é uma questão meramente humana",
     "b) O chamado para o ministério é uma obra divina reconhecida pela igreja",
     "c) O chamado para o ministério é reservado apenas para alguns indivíduos especiais",
     "d) O chamado para o ministério é uma questão de escolha pessoal sem intervenção divina"],

    ["a) Os ministros têm a responsabilidade de ensinar e pregar a Palavra de Deus com fidelidade",
     "b) Os ministros têm responsabilidade apenas por questões práticas da igreja",
     "c) Os ministros têm responsabilidade apenas por questões administrativas",
     "d) Os ministros não têm responsabilidade em relação ao ensino da Palavra"],

    ["a) O Espírito Santo não tem papel na vida cristã",
     "b) O Espírito Santo é apenas uma influência positiva",
     "c) O papel do Espírito Santo na vida cristã é desconhecido e insondável",
     "d) O Espírito Santo capacita os crentes para uma vida de santidade e serviço"],

    ["a) O crescimento espiritual é opcional e irrelevante",
     "b) O crescimento espiritual é uma busca pessoal sem intervenção divina",
     "c) O crescimento espiritual é uma jornada contínua capacitada pelo Espírito Santo",
     "d) O crescimento espiritual é uma conquista pessoal baseada apenas em esforços humanos"],

    ["a) As Escrituras são autoritativas em questões de fé e prática",
     "b) As Escrituras têm autoridade apenas em assuntos espirituais",
     "c) As Escrituras têm autoridade apenas para certos grupos religiosos",
     "d) As Escrituras não são autoritativas para a vida cotidiana"],

     ["a) Jesus Cristo é apenas um grande líder religioso",
      "b) Jesus Cristo é o Filho de Deus encarnado",
      "c) Jesus Cristo é uma figura mítica inventada pela igreja",
      "d) Jesus Cristo é uma manifestação divina temporária"]
    
]


# Respostas corretas
respostas_certas = [
    "c", "a", "b", "d", "d", "a", "c", "d", "c", "b", "a", "d", "c", "a", "b"
]

# Função principal do quiz
def jogar_quiz():
    st.title("Quiz das Assembleias de Deus")

    # Inicializando a pontuação
    if 'score' not in st.session_state:
        st.session_state.score = 0

    # Inicializando o índice da pergunta
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0

    # Inicializando a lista de respostas do usuário
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

    # Função para atualizar a pontuação e ir para a próxima pergunta
    def proxima_pergunta():
        st.session_state.user_answers.append(st.session_state.resposta)
        if st.session_state.resposta.startswith(respostas_certas[st.session_state.current_question]):
            st.session_state.score += 1
        st.session_state.current_question += 1

    # Checar se o quiz acabou
    if st.session_state.current_question < len(perguntas):
        st.subheader(f"Pergunta {st.session_state.current_question + 1}: {perguntas[st.session_state.current_question]}")
        st.session_state.resposta = st.radio("Escolha uma alternativa:", alternativas[st.session_state.current_question], key=f"q{st.session_state.current_question}")

        if st.button("Próxima"):
            proxima_pergunta()
    else:
        st.success(f"Você completou o quiz! Sua pontuação final foi: {st.session_state.score}/{len(perguntas)}")
        if st.button("Reiniciar Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.user_answers = []

# Executar o quiz
if __name__ == "__main__":
    jogar_quiz()
