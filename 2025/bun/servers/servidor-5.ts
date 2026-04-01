// servidor-pokemon.ts
interface Pokemon {
  name: string;
  id: number;
  height: number;
  weight: number;
  types: Array<{
    type: {
      name: string;
    };
  }>;
  sprites: {
    front_default: string;
  };
  stats: Array<{
    base_stat: number;
    stat: {
      name: string;
    };
  }>;
}

async function buscarPokemon(nombre: string): Promise<Pokemon | null> {
  try {
    const respuesta = await fetch(`https://pokeapi.co/api/v2/pokemon/${nombre.toLowerCase()}`)
    
    if (!respuesta.ok) {
      return null;
    }
    
    const pokemon = await respuesta.json();
    return pokemon as Pokemon;
  } catch (error) {
    console.error('Error buscando Pokemon:', error);
    return null;
  }
}

const servidor = Bun.serve({
  port: 3000,
  hostname: '0.0.0.0',
  
  async fetch(peticion) {
    const url = new URL(peticion.url);
    
    // Página principal con formulario
    if (url.pathname === '/' && peticion.method === 'GET') {
      return new Response(`
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>PokéDex</title>
            <style>
              body {
                font-family: 'Arial', sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
              }
              .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 30px;
              }
              h1 {
                text-align: center;
                font-size: 3em;
                margin: 0;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
              }
              form {
                display: flex;
                gap: 10px;
                margin: 30px 0;
              }
              input {
                flex: 1;
                padding: 15px;
                font-size: 18px;
                border: none;
                border-radius: 10px;
              }
              button {
                padding: 15px 30px;
                font-size: 18px;
                background: #ffd700;
                color: #333;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                font-weight: bold;
              }
              button:hover {
                background: #ffed4e;
              }
              .ejemplos {
                text-align: center;
                margin-top: 20px;
                opacity: 0.8;
              }
              .ejemplos a {
                color: #ffd700;
                text-decoration: none;
                margin: 0 10px;
              }
            </style>
          </head>
          <body>
            <div class="container">
              <h1>🔴 PokéDex</h1>
              <form action="/pokemon" method="GET">
                <input 
                  type="text" 
                  name="nombre" 
                  placeholder="Nombre del Pokémon..." 
                  required
                  autocomplete="off"
                >
                <button type="submit">Buscar</button>
              </form>
              <div class="ejemplos">
                Prueba con: 
                <a href="/pokemon?nombre=pikachu">Pikachu</a>
                <a href="/pokemon?nombre=charizard">Charizard</a>
                <a href="/pokemon?nombre=mewtwo">Mewtwo</a>
                <a href="/pokemon?nombre=ditto">Ditto</a>
              </div>
            </div>
          </body>
        </html>
      `, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' }
      });
    }
    
    // Buscar Pokemon
    if (url.pathname === '/pokemon' && peticion.method === 'GET') {
      const nombre = url.searchParams.get('nombre');
      
      if (!nombre) {
        return Response.redirect('/', 302);
      }
      
      console.log(`🔍 Buscando: ${nombre}`);
      const pokemon = await buscarPokemon(nombre);
      
      if (!pokemon) {
        return new Response(`
          <html>
            <head>
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <title>Pokémon no encontrado</title>
              <style>
                body {
                  font-family: Arial;
                  max-width: 600px;
                  margin: 100px auto;
                  padding: 20px;
                  text-align: center;
                  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                  color: white;
                }
                .error {
                  background: rgba(255, 255, 255, 0.1);
                  backdrop-filter: blur(10px);
                  border-radius: 20px;
                  padding: 40px;
                }
                a {
                  color: #ffd700;
                  text-decoration: none;
                  font-size: 18px;
                }
              </style>
            </head>
            <body>
              <div class="error">
                <h1>😢 Pokémon no encontrado</h1>
                <p>No pudimos encontrar: <strong>${nombre}</strong></p>
                <p><a href="/">← Volver a buscar</a></p>
              </div>
            </body>
          </html>
        `, {
          status: 404,
          headers: { 'Content-Type': 'text/html; charset=utf-8' }
        });
      }
      
      console.log(`✅ Encontrado: ${pokemon.name} (#${pokemon.id})`);
      
      // Construir HTML con los datos del Pokemon
      const tipos = pokemon.types.map(t => t.type.name).join(', ');
      const stats = pokemon.stats.map(s => `
        <div class="stat">
          <span class="stat-name">${s.stat.name}</span>
          <div class="stat-bar">
            <div class="stat-fill" style="width: ${(s.base_stat / 255) * 100}%">
              ${s.base_stat}
            </div>
          </div>
        </div>
      `).join('');
      
      return new Response(`
        <html>
          <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>${pokemon.name} - PokéDex</title>
            <style>
              body {
                font-family: Arial;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
              }
              .card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 30px;
              }
              .header {
                text-align: center;
                margin-bottom: 30px;
              }
              h1 {
                font-size: 3em;
                margin: 0;
                text-transform: capitalize;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
              }
              .id {
                font-size: 1.5em;
                opacity: 0.8;
              }
              .content {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
              }
              .imagen {
                text-align: center;
              }
              .imagen img {
                width: 200px;
                height: 200px;
                image-rendering: pixelated;
              }
              .info {
                display: flex;
                flex-direction: column;
                gap: 15px;
              }
              .info-item {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 10px;
              }
              .info-item strong {
                color: #ffd700;
              }
              .stats {
                margin-top: 20px;
              }
              .stat {
                margin: 10px 0;
              }
              .stat-name {
                display: inline-block;
                width: 150px;
                text-transform: capitalize;
              }
              .stat-bar {
                display: inline-block;
                width: calc(100% - 160px);
                height: 25px;
                background: rgba(0,0,0,0.3);
                border-radius: 10px;
                overflow: hidden;
              }
              .stat-fill {
                height: 100%;
                background: linear-gradient(90deg, #4caf50, #8bc34a);
                display: flex;
                align-items: center;
                justify-content: flex-end;
                padding-right: 10px;
                font-weight: bold;
              }
              .volver {
                text-align: center;
                margin-top: 30px;
              }
              .volver a {
                color: #ffd700;
                text-decoration: none;
                font-size: 18px;
              }
              @media (max-width: 600px) {
                .content {
                  grid-template-columns: 1fr;
                }
              }
            </style>
          </head>
          <body>
            <div class="card">
              <div class="header">
                <h1>${pokemon.name}</h1>
                <div class="id">#${pokemon.id.toString().padStart(3, '0')}</div>
              </div>
              
              <div class="content">
                <div class="imagen">
                  <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
                </div>
                
                <div class="info">
                  <div class="info-item">
                    <strong>Tipo:</strong> ${tipos}
                  </div>
                  <div class="info-item">
                    <strong>Altura:</strong> ${pokemon.height / 10} m
                  </div>
                  <div class="info-item">
                    <strong>Peso:</strong> ${pokemon.weight / 10} kg
                  </div>
                </div>
              </div>
              
              <div class="stats">
                <h2>Estadísticas</h2>
                ${stats}
              </div>
              
              <div class="volver">
                <a href="/">← Buscar otro Pokémon</a>
              </div>
            </div>
          </body>
        </html>
      `, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' }
      });
    }
    
    return new Response('404 - No encontrado', { status: 404 });
  }
});

console.log(`🚀 PokéDex corriendo en http://localhost:${servidor.port}`);
console.log(`📱 Desde móvil: http://<TU-IP>:${servidor.port}`);