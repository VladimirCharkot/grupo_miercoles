// servidor-interactivo.ts
let contadorAccesos = 0;

const servidor = Bun.serve({
  port: 3000,

  fetch(peticion) {
    contadorAccesos++;

    const url = new URL(peticion.url);
    console.log(`[${contadorAccesos}] ${peticion.method} ${url.pathname}`);

    // Diferentes respuestas según la ruta
    if (url.pathname === '/') {
      return new Response(`
        <h1>Servidor Interactivo</h1>
        <p>Esta es el acceso número ${contadorAccesos}</p>
        <p>Prueba visitar:</p>
        <ul>
          <li><a href="/hola">/hola</a></li>
          <li><a href="/contador">/contador</a></li>
          <li><a href="/hora">/hora</a></li>
        </ul>
      `, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' }
      });
    }

    if (url.pathname === '/hola') {
      return new Response('¡Hola! 👋');
    }

    if (url.pathname === '/contador') {
      return new Response(`Accesos totales: ${contadorAccesos}`);
    }

    if (url.pathname === '/hora') {
      return new Response(`Hora actual: ${new Date().toLocaleString()}`);
    }

    return new Response('404 - No encontrado', { status: 404 });
  }
});

console.log(`🚀 Servidor en http://localhost:${servidor.port}`);