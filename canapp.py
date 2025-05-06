def criar_pagina_html():
    html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canivete Suíço Digital</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #d40000;
            color: white;
            padding: 20px 0;
            text-align: center;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        
        .subtitle {
            font-style: italic;
            margin-top: 5px;
        }
        
        .creator-section {
            display: flex;
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin: 30px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .creator-photo {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid #d40000;
            margin-right: 20px;
        }
        
        .creator-info {
            flex: 1;
        }
        
        .tools-section {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .tool-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .tool-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .tool-card h3 {
            color: #d40000;
            border-bottom: 2px solid #d40000;
            padding-bottom: 10px;
            margin-top: 0;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            background-color: #333;
            color: white;
            border-radius: 10px 10px 0 0;
        }
        
        @media (max-width: 768px) {
            .creator-section {
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            
            .creator-photo {
                margin-right: 0;
                margin-bottom: 20px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Canivete Suíço Digital</h1>
            <p class="subtitle">Ferramentas úteis para o dia a dia</p>
        </div>
    </header>
    
    <div class="container">
        <section class="creator-section">
            <img src="foto_criador.jpg" alt="Foto do Criador" class="creator-photo">
            <div class="creator-info">
                <h2>Sobre o Criador</h2>
                <p>Olá! Meu nome é [Seu Nome], sou [sua profissão/área de atuação] e criei este Canivete Suíço Digital para compartilhar ferramentas úteis que desenvolvi ao longo do tempo.</p>
                <p>Esta página foi criada com o objetivo de [seu objetivo/motivação]. Espero que as ferramentas aqui disponibilizadas possam ser úteis para você!</p>
                <p><strong>Localização:</strong> [Sua Cidade/Estado/País]</p>
            </div>
        </section>
        
        <h2>Ferramentas Disponíveis</h2>
        <section class="tools-section">
            <div class="tool-card">
                <h3>Conversor de Unidades</h3>
                <p>Converta entre diferentes unidades de medida: comprimento, peso, temperatura e mais.</p>
                <button onclick="location.href='conversor.html'">Acessar</button>
            </div>
            
            <div class="tool-card">
                <h3>Calculadora Científica</h3>
                <p>Uma calculadora completa com funções científicas para seus cálculos complexos.</p>
                <button onclick="location.href='calculadora.html'">Acessar</button>
            </div>
            
            <div class="tool-card">
                <h3>Gerenciador de Tarefas</h3>
                <p>Organize suas tarefas diárias e aumente sua produtividade.</p>
                <button onclick="location.href='tarefas.html'">Acessar</button>
            </div>
            
            <div class="tool-card">
                <h3>Editor de Texto Online</h3>
                <p>Escreva e formate textos sem precisar de um processador instalado.</p>
                <button onclick="location.href='editor.html'">Acessar</button>
            </div>
            
            <div class="tool-card">
                <h3>Conversor de Moedas</h3>
                <p>Converta valores entre diferentes moedas com cotações atualizadas.</p>
                <button onclick="location.href='moedas.html'">Acessar</button>
            </div>
            
            <div class="tool-card">
                <h3>Gerador de Senhas</h3>
                <p>Crie senhas seguras e aleatórias para proteger suas contas.</p>
                <button onclick="location.href='senhas.html'">Acessar</button>
            </div>
        </section>
    </div>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 Canivete Suíço Digital - Todos os direitos reservados</p>
            <p>Desenvolvido com ❤️ por [Seu Nome]</p>
        </div>
    </footer>
</body>
</html>
"""

    with open("canivete_suico.html", "w", encoding="utf-8") as file:
        file.write(html)
    
    print("Página HTML criada com sucesso: canivete_suico.html")

if __name__ == "__main__":
    criar_pagina_html()