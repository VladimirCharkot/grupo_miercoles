// servidor-simple.ts
const servidor = Bun.serve({
  port: 3000,

  // Este "fetch" es el loop - se ejecuta cada vez que llega una petición
  fetch(peticion) {
    console.log('📥 Petición recibida:', peticion.url);

    // Procesar y responder
    const respuesta = new Response('¡Hola desde el servidor!');

    console.log('📤 Respuesta enviada');
    return respuesta;
  }
});

console.log(`🚀 Servidor escuchando en http://localhost:${servidor.port}`);
console.log('El servidor está en un loop infinito esperando peticiones...');