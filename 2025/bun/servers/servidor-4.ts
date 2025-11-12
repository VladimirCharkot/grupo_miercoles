// servidor-estudiantes.ts
interface Visita {
  numero: number;
  nombre: string;
  hora: string;
}

const visitas: Visita[] = [];

const servidor = Bun.serve({
  port: 3000,

  fetch(peticion) {
    const url = new URL(peticion.url);

    // Página principal
    if (url.pathname === '/' && peticion.method === 'GET') {
      return new Response(`
        <html>
          <head>
            <title>Servidor de Visitas</title>
            <style>
              body { font-family: Arial; max-width: 600px; margin: 50px auto; }
              input, button { padding: 10px; margin: 5px; }
            </style>
          </head>
          <body>
            <h1>Registro de Visitas</h1>
            <form action="/registrar" method="GET">
              <input type="text" name="nombre" placeholder="Tu nombre" required>
              <button type="submit">Registrarme</button>
            </form>
            <h2>Visitas recientes:</h2>
            <ul>
              ${visitas.map(v => `
                <li>#${v.numero}: ${v.nombre} a las ${v.hora}</li>
              `).join('')}
            </ul>
          </body>
        </html>
      `, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' }
      });
    }

    // Registrar visita
    if (url.pathname === '/registrar' && peticion.method === 'GET') {
      const nombre = url.searchParams.get('nombre') || 'Anónimo';

      const visita: Visita = {
        numero: visitas.length + 1,
        nombre: nombre,
        hora: new Date().toLocaleTimeString()
      };

      visitas.push(visita);
      console.log(`✅ Nueva visita: ${nombre}`);

      // Redirigir a la página principal
      return Response.redirect('http://localhost:3000/', 302);
    }

    return new Response('404', { status: 404 });
  }
});

console.log(`🚀 Servidor en http://localhost:${servidor.port}`);
console.log('Abre el navegador y registra visitas!');